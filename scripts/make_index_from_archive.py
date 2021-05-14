#!/usr/bin/env python3
from argparse import ArgumentParser

from se.archive import load_archive
from se.index import make_index, save_index


MSG_DESCRIPTION = "Le docs e gera indice reverso."


def main():
    parser = ArgumentParser(description=MSG_DESCRIPTION)
    parser.add_argument("filename_docs", help="Os doc.")
    parser.add_argument("filename_index", help="Os indice.")
    args = parser.parse_args()

    docs = load_archive(args.filename_docs)
    index = make_index(docs)

    save_index(index, args.filename_index)


if __name__ == "__main__":
    main()
