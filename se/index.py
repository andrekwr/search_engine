import json

from collections import defaultdict
from se.normalize import clean_text


class Index:
    def __init__(self, index):
        self.index = index

    def lookup(self, query_term):
        if query_term in self.index:
            return self.index[query_term]
        else:
            return []

    def wordCount(self, query_term, doc_number):
        if doc_number in self.index[query_term]:
            return self.index[query_term][doc_number]
        else:
            return 0


##Palavra: [doc1, doc2, doc3]
##Palavra: {doc1 : frequencia, doc2: frequencia, doc3: frequencia}
def make_index(docs):
    index = defaultdict(lambda: defaultdict(int))
    for k, doc in enumerate(docs):
        words = doc
        for word in words:
            word = clean_text(word)
            index[word][k] += 1

    return index


def save_index(index, path):
    with open(path, "w") as file:
        json.dump(index, file, indent=4)


def load_index(path):
    with open(path, "r") as file:
        return json.load(file)
