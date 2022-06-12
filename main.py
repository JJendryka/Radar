import sys

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtUiTools import QUiLoader

from ui.main_window import Ui_MainWindow
from multiprocessing import Queue, Process
import processor
from utils import InstructionType, Settings, WindowType


class Window(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.instruction_queue = Queue()
        self.unprocessed_queue = Queue()
        self.processed_queue = Queue()
        self.forwarding_queue = Queue()

        self.processor_process = Process(
            target=processor.run,
            args=(self.unprocessed_queue, self.processed_queue,
                  self.instruction_queue),
        )
        self.processor_process.daemon = True
        self.processor_process.start()

        self.small2DPlot.queue = self.processed_queue
        self.input2DPlot.queue = self.unprocessed_queue
        self.smallWaterfallPlot.queue = self.forwarding_queue
        self.small2DPlot.output_queue = self.forwarding_queue

        self.connect_signals()

    def connect_signals(self):
        self.calibrateButton.clicked.connect(self.calibrate)
        self.tabWidget.currentChanged.connect(self.tab_changed)
        self.windowFunctionCombobox.currentIndexChanged.connect(
            self.window_changed)
        self.calibrationCheckbox.stateChanged.connect(self.calibration_changed)
        self.frequencyBox.valueChanged.connect(self.frequency_changed)
        self.timeAverageBox.valueChanged.connect(self.time_averages_changed)
        self.spaceAverageBox.valueChanged.connect(self.space_averages_changed)
        self.decimationBox.valueChanged.connect(self.decimation_changed)
        self.spanBox.valueChanged.connect(self.span_changed)
        self.waterfallSpeedSlider.valueChanged.connect(
            self.waterfall_speed_changed)
        self.rangeSlider.valueChanged.connect(self.range_changed)
        self.verticalScaleSlider.valueChanged.connect(self.scale_changed)

    def time_averages_changed(self, value):
        self.instruction_queue.put(
            (InstructionType.SETTINGS, Settings(time_averages=value)))

    def space_averages_changed(self, value):
        self.instruction_queue.put(
            (InstructionType.SETTINGS, Settings(space_averages=value)))

    def decimation_changed(self, value):
        self.instruction_queue.put(
            (InstructionType.SETTINGS, Settings(decimation=value)))

    def calibration_changed(self, state):
        if state == 0:
            self.instruction_queue.put(
                (InstructionType.SETTINGS, Settings(use_calibration=False)))
        elif state == 2:
            self.instruction_queue.put(
                (InstructionType.SETTINGS, Settings(use_calibration=True)))

    def tab_changed(self, index):
        if index == 0:
            self.small2DPlot.queue = self.processed_queue
            self.small2DPlot.output_queue = self.forwarding_queue
            self.smallWaterfallPlot.queue = self.forwarding_queue

            self.big2Dplot.queue = None
            self.big2Dplot.output_queue = None
            self.bigWaterfallPlot.queue = None
        if index == 2:
            self.small2DPlot.queue = None
            self.small2DPlot.output_queue = None
            self.smallWaterfallPlot.queue = None

            self.big2Dplot.queue = self.processed_queue
            self.big2Dplot.output_queue = self.forwarding_queue
            self.bigWaterfallPlot.queue = self.forwarding_queue
        if index == 3:
            self.small2DPlot.queue = None
            self.small2DPlot.output_queue = None
            self.smallWaterfallPlot.queue = None

            self.big2Dplot.queue = self.processed_queue
            self.big2Dplot.output_queue = self.forwarding_queue
            self.bigWaterfallPlot.queue = self.forwarding_queue

    def frequency_changed(self, value):
        self.instruction_queue.put(
            (InstructionType.SETTINGS, Settings(frequency=value)))

    def window_changed(self, index):
        if index == 0:
            self.instruction_queue.put(
                (InstructionType.SETTINGS, Settings(window=WindowType.RECTANGULAR)))
        elif index == 1:
            self.instruction_queue.put(
                (InstructionType.SETTINGS, Settings(window=WindowType.HAMMING)))
        elif index == 2:
            self.instruction_queue.put(
                (InstructionType.SETTINGS, Settings(window=WindowType.BLACKMANN)))
        elif index == 3:
            self.instruction_queue.put(
                (InstructionType.SETTINGS, Settings(window=WindowType.HANNING)))

    def calibrate(self):
        self.instruction_queue.put((InstructionType.CALIBRATION, None))

    def span_changed(self, value):
        self.instruction_queue.put(
            (InstructionType.SETTINGS, Settings(span=value*1e6)))

    def waterfall_speed_changed(self, value):
        self.smallWaterfallPlot.buffer_lenght = value
        self.bigWaterfallPlot.buffer_lenght = value

    def range_changed(self, value):
        self.small2DPlot.max_x = value
        self.big2Dplot.max_x = value
        self.smallWaterfallPlot.max_x = value
        self.bigWaterfallPlot.max_x = value

    def scale_changed(self, value):
        self.small2DPlot.max_y = value
        self.big2Dplot.max_y = value


if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    app.exec_()
    win.instruction_queue.put((InstructionType.EXIT, None))
