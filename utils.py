from enum import Enum


class WindowType(Enum):
    HAMMING = 1
    BLACKMANN = 2
    HANNING = 3
    RECTANGULAR = 4


class InstructionType(Enum):
    SETTINGS = 1
    CALIBRATION = 2
    EXIT = 3
    CONNECT = 4


class Settings():
    def __init__(self, use_calibration=None, time_averages=None, space_averages=None, decimation=None, window=None, frequency=None, span=None):
        self.use_calibration = use_calibration
        self.time_averages = time_averages
        self.space_averages = space_averages
        self.decimation = decimation
        self.window = window
        self.frequency = frequency
        self.span = span
