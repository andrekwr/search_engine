#!/usr/bin/env python3
from argparse import ArgumentParser

from se.archive import load_archive
from se.index import load_index
from se.search import search


MSG_DESCRIPTION = "Busca."


def main():
    parser = ArgumentParser(description=MSG_DESCRIPTION)
    parser.add_argument("filename_docs", help="Os doc.")
    parser.add_argument("filename_index", help="Os indice.")
    parser.add_argument("query", nargs="+", help="A query.")
    args = parser.parse_args()

    docs = load_archive(args.filename_docs)
    index = load_index(args.filename_index)

    query = " ".join(args.query)

    docs_searched = search(query.lower(), index, docs)

    for doc in docs_searched:
        print(" ".join(doc))
        print("=" * 80)


if __name__ == "__main__":
    main()
