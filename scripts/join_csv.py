import os
import glob
import pandas as pd

# Script to concat all csvs.

"""
Tweets obtidos de https://www.kaggle.com/ayhmrba/elon-musk-tweets-2010-2021
"""

os.chdir("..")
df = pd.read_csv("./data/2010.csv", delimiter=",")
print(df.shape)


os.chdir("data")

file_extension = ".csv"
all_filenames = [i for i in glob.glob(f"*{file_extension}")]


# there were a few tweets that were exactly the same, published at the same time, on the
# 2021 and 2020 csvs.
combined_csv_data = pd.concat([pd.read_csv(f, delimiter=",") for f in all_filenames])


combined_csv_data = combined_csv_data.drop_duplicates(subset="tweet")

combined_csv_data.to_csv("elon.csv")
os.chdir("..")