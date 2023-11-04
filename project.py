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






# Main Function

extract()
cleaning()