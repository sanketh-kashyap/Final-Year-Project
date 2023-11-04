import pandas as pd

data=pd.read_csv('combined_data.csv')

data=data.dropna(subset=['help_useful','help_not_useful','comments'])

data.to_csv('Cleaned_Data.csv',index=False)
