import csv
import random
import os
class DataLoader():
    # def __init__(self):
    #     self.vocabulary = self.load_vocabulary()
        
    def load_vocabulary(self, lecture = 0):
        vocabulary_data = []
        # print(os.getcwd())
        with open('./data/vocabulary.csv','r',encoding="utf-8") as vocabulary:
            
            csvreader = csv.DictReader(vocabulary)
            for row in csvreader:
                if lecture == 0:
                    vocabulary_data.append(row)
                elif row["lecture"] == lecture:
                    vocabulary_data.append(row)
                
        
        return vocabulary_data