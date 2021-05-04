#!/usr/bin/env python3
import json

from argparse import ArgumentParser

import pandas as pd

from nltk.tokenize import TweetTokenizer

from se.archive import save_archive


MSG_DESCRIPTION = """Le arquivo de tweets e gera JSON com tweets tokenizados.
Tweets obtidos de https://www.kaggle.com/ayhmrba/elon-musk-tweets-2010-2021
"""


def read_donald_tweets(path):
    df = pd.read_csv(path)
    docs = []
    # preserve_case = False: tokenizer will downcase everything except for emoticons
    tokenizer = TweetTokenizer(preserve_case=False)
    for text in df["tweet"]:
        toks = tokenizer.tokenize(text)
        docs.append(toks)
    return docs


def main():
    parser = ArgumentParser(description=MSG_DESCRIPTION)
    parser.add_argument("filename_tweets", help="Os tweet.")
    parser.add_argument("filename_archive", help="Onde guarda.")
    args = parser.parse_args()

    docs = read_donald_tweets(args.filename_tweets)
    save_archive(docs, args.filename_archive)


if __name__ == "__main__":
    main()
