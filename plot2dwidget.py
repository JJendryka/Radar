from PySide2.QtWidgets import QWidget, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.figure import Figure
import numpy as np
from multiprocessing.queues import Queue


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
        self.output_queue = None

        self.max_x = None
        self.max_y = None
        self.offset_y = None

    def _update_canvas(self):
        if self.queue is not None:
            if not self.queue.empty():
                x = None
                y = None
                while not self.queue.empty():
                    (x, y) = self.queue.get()
                    if self.output_queue is not None:
                        self.output_queue.put((x, y))

                self._line.set_data(x, y)
                self._axes.relim()
                self.scale()
                self.canvas.draw()

    def scale(self):
        if self.max_x is None:
            self._axes.autoscale_view(scaley=False)
        else:
            self._axes.set_xlim(0, 3000*self.max_x/100)

        if self.max_y is None:
            self._axes.autoscale_view(scalex=False)
        else:
            self._axes.set_ylim(-1*self.max_y/100, 10000*self.max_y/100)
