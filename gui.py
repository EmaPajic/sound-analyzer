#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: EmaPajic
"""

from tkinter import *
from obrada import Obrada
from tkinter.filedialog import askopenfilename


def donothing():
   filewin = Toplevel(root)
   button = Button(filewin, text="Do nothing button")
   button.pack()

def plot_time_window():
    window1 = Toplevel(root)
    window2 = Toplevel(root)
    analyzer.plot_time(window1, window2)
    
def plot_fft_window():
    window1 = Toplevel(root)
    window2 = Toplevel(root)
    analyzer.plot_fft(window1, window2)

if __name__ == '__main__':
    
    root = Tk() 
    root.title('Song analyzer')
    analyzer = Obrada()
    
    menu = Menu(root)
    
    # Adding File menu and commands 
    file_menu = Menu(menu, tearoff = 0) 
    menu.add_cascade(label='File', menu=file_menu) 
    file_menu.add_command(label='Open...', command = analyzer.open_file) 
    file_menu.add_command(label ='Save as', command = analyzer.save_data) 
    
    # Adding Analyze menu and commands
    analyze_menu = Menu(menu, tearoff = 0) 
    menu.add_cascade(label='Analyze', menu=analyze_menu) 
    analyze_menu.add_command(label='Plot signal',
                             command = plot_time_window) 
    analyze_menu.add_command(label='Plot FFT',
                             command = plot_fft_window) 
    analyze_menu.add_command(label ='Filter', command = analyzer.filter_data)  
    
    # Adding Help menu 
    help_menu = Menu(menu, tearoff = 0) 
    menu.add_cascade(label='Help', menu=help_menu, command = donothing) 
    help_menu.add_command(label='About') 
    
    # Adding Edit Menu and commands 
    root.config(menu=menu)
    mainloop() 