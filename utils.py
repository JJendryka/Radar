class Window(Enum):
    HAMMING = 1
    BLACKMANN = 2
    HANNING = 3


class InstructionType(Enum):
    SETTINGS = 1
    CALIBRATION = 2
    EXIT = 3
    CONNECT = 4


class Settings():
    def __init__(self):
        self.use_calibration = None
        self.time_averages = None
        self.space_averages = None
        self.decimation = None
        self.window = None
        self.frequency = None

    def use_calibration(self, val):
        self.use_calibration = val
        return self

    def time_averages(self, val):
        self.time_averages = val
        return self

    def space_averages(self, val):
        self.space_averages = val
        return self

    def decimation(self, val):
        self.decimation = val
        return self

    def window(self, val):
        self.window = val
        return self

    def frequency(self, val):
        self.frequency = val
        return self
