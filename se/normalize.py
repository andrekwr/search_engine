import re
from nltk.stem import LancasterStemmer

def remove_pontuation(text):
    text = re.sub(
        r"(https?://(?:www.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9].[^\s]{2,}|www.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9].[^\s]{2,}|https?://(?:www.|(?!www))[a-zA-Z0-9]+.[^\s]{2,}|www.[a-zA-Z0-9]+.[^\s]{2,})", "", text)
    text = re.sub(r"[^@#\w\s]", "", text)
    return text

def stemmer(text):
    lancaster=LancasterStemmer()
    new_text = []
    for i in text.split():
        new_text += [lancaster.stem(i)]
    return " ".join(new_text)

def clean_text(text):
    #text = remove_pontuation(text)
    text = stemmer(text)
    return text.lower()
    

  

