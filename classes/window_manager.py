import csv
import random
from classes.data_loader import DataLoader
import tkinter as tk
from tkinter import ttk

class WindowManager():
    def __init__(self):  
        self.vocabulary = None
        self.window = tk.Tk()
        self.title_label = ttk.Label(master=self.window, text='Practica de vocabulario',font='Calibri 30')
        self.kanji_string = tk.StringVar()
        self.kanji_label = ttk.Label(master=self.window, 
                                     font='Calibri 50', 
                                     textvariable=self.kanji_string)
        self.furigana_string = tk.StringVar()
        self.furigana_label = ttk.Label(master=self.window, 
                                        font = 'Calibri 24', 
                                        textvariable=self.furigana_string)
        self.input_frame = ttk.Frame(master=self.window)
        self.entry_string = tk.StringVar()
        self.entry = ttk.Entry(master=self.input_frame, textvariable=self.entry_string)
        self.button = ttk.Button(master=self.input_frame, 
                                 text='Validar',
                                 command=self.on_validate_vocabulary)
        self.random_vocabulary_word = None
        self.answer_string = tk.StringVar()
        self.answer_label = ttk.Label(master=self.window,
                                      font='Calibri 24',
                                      textvariable=self.answer_string)
     
    
        
    def select_random_vocabulary_word(self, vocabulary_data):
        vocabulary_length = len(vocabulary_data)
        index = random.randint(0,vocabulary_length-1)
        return vocabulary_data[index]
    
    def on_validate_vocabulary(self):
        if self.entry_string.get().lower() == self.random_vocabulary_word["lang_es"]:
            self.answer_string.set(f'Correcto {self.random_vocabulary_word["kanji"]}({self.random_vocabulary_word["furigana"]}) significa {self.entry_string.get()}')
        else:
            self.answer_string.set(f'Incorrecto {self.random_vocabulary_word["kanji"]}({self.random_vocabulary_word["furigana"]}) significa {self.random_vocabulary_word["lang_es"]}')
        
        self.update_vocabulary_word()
        
            
    def update_vocabulary_word(self):
        if self.vocabulary != None:
            self.random_vocabulary_word = self.select_random_vocabulary_word(self.vocabulary)
            self.kanji_string.set(self.random_vocabulary_word["kanji"])
            self.furigana_string.set(self.random_vocabulary_word["furigana"])
    
    def set_vocabulary(self,vocabulary):
        self.vocabulary = vocabulary
        
    
    def run_window(self):
        self.random_vocabulary_word = self.select_random_vocabulary_word(self.vocabulary)
        self.window.title('Practice')
        self.window.geometry('600x600')
        self.update_vocabulary_word()
        self.title_label.pack()
        self.kanji_label.pack()
        self.furigana_label.pack()
        
        self.entry.pack(side='left', padx=10)
        self.button.pack(side='left')
        self.input_frame.pack(pady=10)
        self.answer_label.pack()
        self.window.mainloop()