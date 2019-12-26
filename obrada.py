#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 11:21:36 2019
@author: EmaPajic
"""

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from scipy.io import wavfile as wav
from scipy.fftpack import fft, fftshift
from scipy import signal
from tkinter.filedialog import askopenfilename
from tkinter.simpledialog import askstring, askinteger, askfloat
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
matplotlib.use("TkAgg")

class Obrada:
    def __init__(self):
        self.rate = 0
        self.data = []
        
    def open_file(self):
        file_name = askopenfilename()
        rate, data = wav.read(file_name) # Read from WAV file
        self.rate = rate
        self.data = data
    
    def plot_time(self, window1, window2):
        ch1 = self.data.T[0]
        ch2 = self.data.T[1]
        ch1 = ch1[0:1000000]
        ch2 = ch2[0:1000000]
        figure1 = Figure(figsize=(5, 4), dpi=100)
        plot1 = figure1.add_subplot(1, 1, 1, xlabel = 'Time [s]',
                                    ylabel = 'Amplitude',
                                    title = '1st channel of data')
        plot1.plot(ch1)
        canvas1 = FigureCanvasTkAgg(figure1, window1)
        canvas1.get_tk_widget().grid(row=0, column=0)
        
        figure2 = Figure(figsize=(5, 4), dpi=100)
        plot2 = figure2.add_subplot(1, 1, 1, xlabel = 'Time [s]',
                                    ylabel = 'Amplitude',
                                    title = '2nd channel of data')
        plot2.plot(ch2)
        canvas2 = FigureCanvasTkAgg(figure2, window2)
        canvas2.get_tk_widget().grid(row=0, column=0)
        
    
    def plot_fft(self, window1, window2):
        ch1 = self.data.T[0]
        ch2 = self.data.T[1]
        ch1 = ch1[0:1000000]
        ch2 = ch2[0:1000000]
        ch1b = [(ele/2**8.)*2-1 for ele in ch1]
        ch2b = [(ele/2**8.)*2-1 for ele in ch2]
        fft_ch1 = fftshift(fft(ch1b))
        fft_ch2 = fftshift(fft(ch2b))
        figure1 = Figure(figsize=(5, 4), dpi=100)
        plot1 = figure1.add_subplot(1, 1, 1, xlabel = 'Frequency [Hz]',
                                    ylabel = 'Magnitude a.u.',
                                    title = 'FFT of 1st channel of data')
        plot1.plot(np.abs(fft_ch1))
        canvas1 = FigureCanvasTkAgg(figure1, window1)
        canvas1.get_tk_widget().grid(row=0, column=0)
        
        figure2 = Figure(figsize=(5, 4), dpi=100)
        plot2 = figure2.add_subplot(1, 1, 1, xlabel = 'Frequency [Hz]',
                                    ylabel = 'Magnitude a.u.',
                                    title = 'FFT of 2nd channel of data')
        plot2.plot(np.abs(fft_ch2))
        canvas2 = FigureCanvasTkAgg(figure2, window2)
        canvas2.get_tk_widget().grid(row=0, column=0)
        #shiftuj x osu 
    
    def filter_data(self):
        order = askinteger('Red filtra', 'Unesite red filtra')
        filter_type = 'start'
        while filter_type != 'lowpass' and filter_type != 'highpass' and filter_type != 'bandpass' and filter_type != 'bandstop':
            filter_type = askstring('Tip filtra', 'Unesite tip filtra (opcije su: lowpass, highpass, bandpass, bandstop)')
        if filter_type == 'lowpass' or filter_type == 'highpass':
            freq = askfloat('Frekvencija odsecanja', 'Unesite frekvenciju odsecanja')
        elif filter_type == 'bandpass' or filter_type == 'bandstop':
            freq = []
            freq1 = askfloat('Frekvencija odsecanja', 'Unesite nizu frekvenciju odsecanja')
            freq2 = askfloat('Frekvencija odsecanja', 'Unesite visu frekvenciju odsecanja')
            freq.append(freq1)
            freq.append(freq2)
            #kako ovo?
        b, a = signal.butter(order, np.array(freq), filter_type)
        filtered_data = signal.filtfilt(b, a, self.data.T)
        self.data = filtered_data.T
        
    def save_data(self):
        file_name = askstring('Cuvanje wav fajla', 'Unesite ime novog wav fajla')
        print(file_name)
        wav.write(file_name, self.rate, self.data)  # Save as WAV file
    
if __name__ == '__main__':
    analyzer = Obrada()
    analyzer.open_file('QUEEN/Bohemian_Rhapsody.wav')
    '''print('Input start time (00:00 - 05:53)')
    start_time = input()
    start_min, start_sec = start_time.split(':') 
    start_sample = (int(start_min) * 60 + int(start_sec)) * analyzer.rate
    print('Input end time (00:00 - 05:53)')
    end_time = input()
    end_min, end_sec = end_time.split(':') 
    end_sample = (int(end_min) * 60 + int(end_sec)) * analyzer.rate
    data = data[start_sample:end_sample]'''
    analyzer.plot_fft()
    #analyzer.filter_data()
    print(filtered_data.shape)
    #analyzer.save_processed_data(rate, filtered_data)
