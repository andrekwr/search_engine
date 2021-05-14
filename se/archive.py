import json


def save_archive(docs, path):
    with open(path, "w") as file:
        json.dump(docs, file, indent=4)


def load_archive(path):
    with open(path, "r") as file:
        return json.load(file)
