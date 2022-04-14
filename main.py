import sys

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtUiTools import QUiLoader

from ui.main_window import Ui_MainWindow
from multiprocessing import Queue, Process
import processor
from utils import InstructionType


class Window(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.instruction_queue = Queue()
        self.unprocessed_queue = Queue()
        self.processed_queue = Queue()

        self.processor_process = Process(
            target=processor.run,
            args=(self.unprocessed_queue, self.processed_queue,
                  self.instruction_queue),
        )
        self.processor_process.daemon = True
        self.processor_process.start()

        self.small2DPlot.queue = self.processed_queue


if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    app.exec_()
    win.instruction_queue.put((InstructionType.EXIT, None))
