# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 18:10:02 2023

@author: Sanketh Kashyap K R
"""

import pandas as pd
import glob


#Extraction from data set
def extract():
    csv_files = glob.glob('RateMyProfessor/*.csv')
    combined_data = pd.DataFrame()
    for csv_file in csv_files:
        df = pd.read_csv(csv_file)
        selected_columns = df[['help_useful', 'help_not_useful', 'comments']]
        combined_data = pd.concat([combined_data, selected_columns], ignore_index=True)
    combined_data.to_csv('combined_data.csv',index=False)
    
    
#Data Cleaning 
def cleaning():
    data=pd.read_csv('combined_data.csv')
    data=data.dropna(subset=['help_useful','help_not_useful','comments'])
    data.to_csv('Cleaned_Data.csv',index=False)
    
def preprocess():   #Here we will do Regex,Upper and Strip.
    data = pd.read_csv('cleaned_data.csv')
    def clean_comments(comment):
        pattern = r'[^a-zA-Z0-9\s]' 
        cleaned_comment = re.sub(pattern, ' ', str(comment))
        return cleaned_comment
    def toupper(sentence):
        upper_sentence=sentence.upper()
        return upper_sentence
    def stripenctence(sentence):
        sentence_strip= sentence.strip()
        return sentence_strip
    data['comments'] = data['comments'].apply(clean_comments)
    data['comments']=data['comments'].apply(toupper)
    data['comments']=data['comments'].apply(stripenctence)
    data.to_csv('Final_data.csv',index=False)

# Main Function

extract()
cleaning()
preprocess()