from multiprocessing.queues import Queue
from utils import Window, InstructionType, Settings
import scipy.signal as signal
import numpy as np
import time

import unifiedlab.oscilloscopes as scopes


class Processor():
    def __init__(self, unprocessed_queue: Queue, processed_queue: Queue, instruction_queue: Queue):
        self.unprocessed_queue = unprocessed_queue
        self.processed_queue = processed_queue
        self.instruction_queue = instruction_queue

        self.use_calibration: bool = False
        self.time_averages: int = 0
        self.space_averages: int = 0
        self.decimation: int = 1
        self.window: Window = Window.HAMMING
        self.frequency: int = 1000

        self.calibration_data: np.ndarray = None

        self.scope: scopes.oscilloscope.Oscilloscope = None

        self.history: Queue = None
        self.averaged: np.ndarray = None

    def run(self):
        while True:
            if not self.instruction_queue.empty():
                (instruction_type, instruction) = self.instruction_queue.get()
                if instruction_type == InstructionType.SETTINGS:
                    self.change_settings(instruction)
                elif instruction_type == InstructionType.CALIBRATION:
                    if self.scope is not None:
                        self.calibrate()
                    else:
                        print("No scope connected to run calibration")
                elif instruction_type == InstructionType.EXIT:
                    break
                elif instruction_type == InstructionType.CONNECT:
                    self.connect(instruction)
            if self.scope is not None:
                self.acquire()
            else:
                time.sleep(0.1)

    def acquire(self):
        acquisition = self.scope.get(1)
        data = acquisition.data

        data = self.cut_out(data, acquisition)
        data = self.decimate(data)
        data = self.window(data)

        self.unprocessed_queue.put(data)

        data = self.fft(data)
        data = self.space_average(data)
        data = self.time_average(data)
        data = self.apply_calibration(data)

        self.processed_queue(data)

    def cut_out(self, data, acquisition):
        sample_period = acquisition.horizontal.interval
        signal_period = 1/self.frequency
        sample_count = int(signal_period/sample_period)
        trigger_sample_index = acquisition.horizontal.offset/acquisition.horizontal.interval
        data = data[trigger_sample_index:trigger_sample_index+sample_count]
        return data

    def window(self, data):
        if self.window is not None:
            window = None
            if self.window == Window.HAMMING:
                window = signal.windows.hamming(len(data))
            elif self.window == Window.BLACKMANN:
                window = signal.windows.blackman(len(data))
            elif self.window == Window.HANNING:
                window = signal.windows.hann(len(data))

            data = np.multiply(data, window)
        return data

    def decimate(self, data):
        if self.decimation is not None and self.decimation > 1:
            data = signal.decimate(data, self.decimation)
        return data

    def fft(self, data):
        data = signal.fft(data, workers=-1)
        return data

    def space_average(self, data):
        data = np.convolve(data, np.ones(self.space_averages),
                           'same') / self.space_averages
        return data

    def time_average(self, data):
        # Initalize queue if empty
        if self.history is None or self.averaged is None:
            self.averaged = data
            self.history = None
            for i in range(self.time_averages):
                self.history.put(data)

        self.history.put(data)
        self.averaged += data / self.time_averages
        self.averaged -= self.history.get() / self.time_averages
        data = self.averaged
        return data

    def apply_calibration(self, data):
        if self.use_calibration and self.calibration_data is not None:
            data = data - self.calibration_data
        return data

    def connect(self, address):
        if self.scope is not None:
            self.scope.close()

        self.calibration_data = None

        self.scope = scopes.SiglentOscilloscope.network_instance(address)
        self.scope.start_async(1)

    def change_settings(self, settings: Settings):
        if settings.use_calibration is not None:
            self.use_calibration = settings.use_calibration
        if settings.time_averages is not None:
            self.time_averages = settings.time_averages
        if settings.space_averages is not None:
            self.space_averages = settings.space_averages
        if settings.decimation is not None:
            self.decimation = settings.decimation
        if settings.window is not None:
            self.window = settings.window
        if settings.frequency is not None:
            self.frequency = settings.frequency

        self.calibration_data = None
        self.history = None
        self.averaged = None

    def calibrate(self):
        calibration_data = None
        for i in range(self.time_averages):
            acquisition = self.scope.get(1)
            data = acquisition.data

            data = self.cut_out(data, acquisition)
            data = self.decimate(data)
            data = self.window(data)

            self.unprocessed_queue.put(data)

            data = self.fft(data)
            data = self.space_average(data)

            if calibration_data is None:
                calibration_data = data / self.time_averages
            else:
                calibration_data += data / self.time_averages

            print("Finished calibration pass:", i)

        self.calibration_data = calibration_data
