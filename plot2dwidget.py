from PySide2.QtWidgets import QWidget, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.figure import Figure
import numpy as np


class Plot2DWidget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        self.canvas = FigureCanvas(Figure())
        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(self.canvas)

        self.setLayout(vertical_layout)

        self._axes = self.canvas.figure.add_subplot(111)
        (self._line,) = self._axes.plot([], [])
        self._axes.autoscale(enable=True, axis="both", tight=False)
        self._axes.margins(0, 0.1)

        self._timer = self.canvas.new_timer(1000 / 60)
        self._timer.add_callback(self._update_canvas)
        self._timer.start()

        self.queue = None

    def _update_canvas(self):
        if self.queue is not None:
            if not self.queue.empty():
                new = None
                while not self.queue.empty():
                    new = self.queue.get()

                self._line.set_data(np.linspace(0, 1, len(new)), new)
                self._axes.relim()
                self._axes.autoscale_view()
                self.canvas.draw()
