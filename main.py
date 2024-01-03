import csv
import random
from classes.data_loader import DataLoader
from classes.window_manager import WindowManager
import tkinter as tk
from tkinter import ttk
import os
import traceback




data_loader = DataLoader()
window_manager = WindowManager()



def select_random_vocabulary(vocabulary_data):
    vocabulary_length = len(vocabulary_data)
    index = random.randint(0,vocabulary_length-1)
    return vocabulary_data[index]

def validate_vocabulary(attempt, actual):
    if attempt == actual:
        return 

def run_main_window(vocabulary_data):
    random_vocabulary = select_random_vocabulary(vocabulary_data)
    
    window_manager.set_vocabulary(vocabulary_data)
    window_manager.run_window()
    # #Window configuration
    # window = tk.Tk()
    # window.title('Practice')
    # window.geometry('600x600')
    
    # #Widgets
    # #title
    # title_label = ttk.Label(master=window, text='Practica de vocabulario',font='Calibri 30')
    # title_label.pack()
    
    
    # #Kanji label
    # kanji_string = tk.StringVar()
    # kanji_string.set(random_vocabulary["kanji"])
    
    # kanji_label = ttk.Label(master=window, font='Calibri 50', textvariable=kanji_string)
    # kanji_label.pack()
    
    # #input field
    # input_frame = ttk.Frame(master=window)
    # entry_str = tk.StringVar()
    # entry = ttk.Entry(master=input_frame, textvariable=entry_str)
    # button = ttk.Button(master=input_frame, text='Validar')
    # entry.pack(side='left', padx = 10)
    # button.pack(side='left')
    # input_frame.pack(pady=10)
    
    # #Result label
    # result_label = ttk.Label(master=window,text='prueba')
    
    # #Run window
    # window.mainloop()

def main():
    vocabulary_data = data_loader.load_vocabulary()
    run_main_window(vocabulary_data)

    
try:
    main()
except Exception as e:
    with open("error.txt", "w", encoding='UTF-8') as f:
        f.write(str(e)+'\n')
        f.write(traceback.format_exc() +'\n\n')
        f.write(os.getcwd())  

# if __name__ == "__main__":
#     try:
#         main()
#     except Exception as e:
#         with open("error.txt", "w", encoding='UTF-8') as f:
#             f.write(str(e)+'\n')
#             f.write(traceback.format_exc() +'\n\n')
#             f.write(os.getcwd())
    