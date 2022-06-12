from PySide2.QtWidgets import QWidget, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.figure import Figure
import numpy as np
import matplotlib
import scipy

WIDTH = 128


class WaterfallWidget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        self.canvas = FigureCanvas(Figure())
        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(self.canvas)

        self.setLayout(vertical_layout)

        self._axes = self.canvas.figure.add_subplot(111)
        self.normalizer = matplotlib.colors.Normalize(vmin=0, vmax=1)
        self.im = self._axes.imshow(
            [[0]], norm=self.normalizer, aspect="auto", extent=[0, 3000, 0, 1])
        self._axes.autoscale(enable=True, axis="both", tight=False)
        self._axes.margins(0, 0.1)

        self._timer = self.canvas.new_timer(1000 / 10)
        self._timer.add_callback(self._update_canvas)
        self._timer.start()

        self.queue = None
        self.data = None

        self.buffer_lenght = 20

        self.max_x = None

    def decimate(self, data):
        factor = int(len(data)/WIDTH)
        data = scipy.signal.decimate(data, factor)
        return data

    def _update_canvas(self):
        if self.queue is not None:
            if not self.queue.empty():
                x = None
                y = None
                while not self.queue.empty():
                    (x, y) = self.queue.get()
                    if self.max_x is not None:
                        y = y[:int(len(y)*self.max_x/100)]
                    y = self.decimate(y)
                    if self.data is None or len(self.data[0]) != len(y):
                        self.data = np.array([y])
                    self.data = np.vstack([self.data, y])

                self.data = self.data[-self.buffer_lenght:]
                self.normalizer.autoscale(self.data)

                self.im.set_data(self.data)
                self._axes.relim()
                self._axes.autoscale_view()
                if self.max_x is not None:
                    self.im.set_extent([0, max(x)*self.max_x/100, 0, 1])
                else:
                    self.im.set_extent([0, max(x), 0, 1])
                self.canvas.draw()
