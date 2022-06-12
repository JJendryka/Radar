from multiprocessing import Queue
from utils import WindowType, InstructionType, Settings
import scipy.signal as signal
import scipy
import numpy as np
import time
import queue

import unifiedlab.oscilloscopes as scopes


def run(unprocessed_queue: Queue, processed_queue: Queue, instruction_queue: Queue):
    processor = Processor(
        unprocessed_queue, processed_queue, instruction_queue)
    processor.run()


class Processor():
    def __init__(self, unprocessed_queue: Queue, processed_queue: Queue, instruction_queue: Queue):
        self.unprocessed_queue = unprocessed_queue
        self.processed_queue = processed_queue
        self.instruction_queue = instruction_queue

        self.use_calibration: bool = False
        self.time_averages: int = 1
        self.space_averages: int = 1
        self.decimation: int = 1
        self.window: WindowType = WindowType.HANNING
        self.frequency: int = 1000
        self.span: int = 500e6

        self.calibration_data: np.ndarray = None

        self.scope: scopes.oscilloscope.Oscilloscope = 1  # None

        self.history: Queue = None
        self.averaged: np.ndarray = None

    def run(self):
        while True:
            if not self.instruction_queue.empty():
                (instruction_type, instruction) = self.instruction_queue.get()
                if instruction_type == InstructionType.SETTINGS:
                    print("Changing settings")
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
        # acquisition = self.scope.get(1)
        acquisition = scopes.acquisition.Acquisition(1)
        acquisition.data = np.sin(np.linspace(
            0, 10000+20000*np.sin(int(time.time()*30)*np.pi/200)**2, 20000))
        acquisition.horizontal = scopes.acquisition.HorizontalProperties(
            1e-7, 20000, 0)

        data = acquisition.data

        data = self.cut_out(data, acquisition)
        data = self.decimate(data)
        data = self.apply_window(data)

        if self.unprocessed_queue.qsize() < 3:
            self.unprocessed_queue.put(
                (np.arange(0, len(data))*acquisition.horizontal.interval, data))

        data = self.fft(data)
        data = self.time_average(data)
        data = self.apply_calibration(data)
        data = np.absolute(data)
        data = self.space_average(data)

        if self.processed_queue.qsize() < 3:
            self.processed_queue.put(
                (np.arange(0, len(data))*self.calculate_x_axis(len(data), acquisition.horizontal.interval), data))

        time.sleep(0.1)

    def cut_out(self, data, acquisition):
        sample_period = acquisition.horizontal.interval
        signal_period = 1/self.frequency
        sample_count = int(signal_period/sample_period)
        trigger_sample_index = int(
            acquisition.horizontal.offset/acquisition.horizontal.interval)
        data = data[trigger_sample_index:trigger_sample_index+sample_count]
        return data

    def apply_window(self, data):
        if self.window is not None:
            window = None
            if self.window == WindowType.HAMMING:
                window = signal.windows.hamming(len(data))
            elif self.window == WindowType.BLACKMANN:
                window = signal.windows.blackman(len(data))
            elif self.window == WindowType.HANNING:
                window = signal.windows.hann(len(data))
            elif self.window == WindowType.RECTANGULAR:
                window = np.ones(len(data))

            data = np.multiply(data, window)
        return data

    def decimate(self, data):
        if self.decimation is not None and self.decimation > 1:
            data = signal.decimate(data, self.decimation)
        return data

    def fft(self, data):
        data = scipy.fft.rfft(data, workers=-1)
        return data

    def space_average(self, data):
        if self.space_averages > 1:
            data = np.convolve(data, np.ones(self.space_averages),
                               'valid') / self.space_averages
        return data

    def time_average(self, data):
        if self.time_averages > 1:
            # Initalize queue if empty
            if self.history is None or self.averaged is None:
                print("new")
                self.averaged = np.copy(data)
                self.history = queue.SimpleQueue()
                for i in range(self.time_averages-1):
                    self.history.put(data)

            self.history.put(data)
            self.averaged += (data / (self.time_averages-1))
            self.averaged -= (self.history.get() / (self.time_averages-1))
            data = self.averaged
        return data

    def apply_calibration(self, data):
        if self.use_calibration and self.calibration_data is not None:
            data = np.subtract(data, self.calibration_data)
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
        if settings.span is not None:
            self.span = settings.span

        if settings.use_calibration is None:
            self.calibration_data = None
            self.history = None
            self.averaged = None

    def calculate_x_axis(self, data_length, interval):
        distance_per_hertz = 299792458 / (2*self.span*self.frequency)

        hertz_per_bin = 1/(interval*self.decimation*data_length)

        distance_per_bin = distance_per_hertz * hertz_per_bin

        return distance_per_bin

    def calibrate(self):
        print("Calibration")
        calibration_data = None
        for i in range(self.time_averages):
            print("Calibration pass:", i)

            # acquisition = self.scope.get(1)
            acquisition = scopes.acquisition.Acquisition(1)
            acquisition.data = np.sin(np.linspace(
                0, 10000+20000*np.sin(int(time.time()*30)*np.pi/200)**2, 20000))
            acquisition.horizontal = scopes.acquisition.HorizontalProperties(
                1e-7, 20000, 0)

            data = acquisition.data

            data = self.cut_out(data, acquisition)
            data = self.decimate(data)
            data = self.apply_window(data)
            data = self.fft(data)

            if calibration_data is None:
                calibration_data = data / self.time_averages
            else:
                calibration_data += data / self.time_averages

            print("Finished calibration pass:", i)

        self.calibration_data = calibration_data
