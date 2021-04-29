import json

from collections import defaultdict


def make_index(docs):
    index = defaultdict(lambda: defaultdict(int))
    for k, doc in enumerate(docs):
        words = doc
        for word in words:
            index[word][k] += 1

    return index


##Palavra: [doc1, doc2, doc3]
##Palavra: {doc1 : frequencia, doc2: frequencia, doc3: frequencia}


def save_index(index, path):
    with open(path, "w") as file:
        json.dump(index, file, indent=4)


def load_index(path):
    with open(path, "r") as file:
        return json.load(file)
