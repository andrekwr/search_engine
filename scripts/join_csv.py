import os
import glob
import pandas as pd

#Script to concat all csvs.

 '''
Tweets obtidos de https://www.kaggle.com/ayhmrba/elon-musk-tweets-2010-2021
'''


df = pd.read_csv('./archive/2011.csv', delimiter=',')
print(df.shape)


os.chdir("archive")

file_extension = '.csv'
all_filenames = [i for i in glob.glob(f"*{file_extension}")]


combined_csv_data = pd.concat([pd.read_csv(f, delimiter=',') for f in all_filenames])

os.chdir("..")

combined_csv_data.to_csv('combined_csv_data.csv')