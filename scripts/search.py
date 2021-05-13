#!/usr/bin/env python3
from argparse import ArgumentParser

from numpy.lib.utils import safe_eval

from se.archive import load_archive
from se.index import load_index
from se.search import search
from se.normalize import clean_text, punctuationCorrection
from nltk.corpus import wordnet

MSG_DESCRIPTION = "Busca."


def main():
    parser = ArgumentParser(description=MSG_DESCRIPTION)
    parser.add_argument("filename_docs", help="Os doc.")
    parser.add_argument("filename_index", help="Os indice.")
    parser.add_argument("query", nargs="+", help="A query.")
    args = parser.parse_args()

    docs = load_archive(args.filename_docs)
    index = load_index(args.filename_index)


    terms = [args.query[i] for i in range(len(args.query)) if i % 2 == 0]

    ops = [args.query[i] for i in range(len(args.query)) if i % 2 != 0]



    counter = 0
    new_query = []
    for term in terms:
        new_query.append(term)
        synonyms = wordnet.synsets(term)
        if len(synonyms) != 0:
            new_query.append('or')
        for syn in wordnet.synsets(term):
            for l in syn.lemmas():
                if l.name() not in new_query:
                    new_query.append(l.name()) #syn
                    new_query.append('or')   

        if (counter + 1 == len(terms)):
            if new_query[-1] == "or":
                new_query.pop()
            continue
        
        if new_query[-1] == "or":
            new_query.pop()
        new_query.append(ops[counter])
        counter += 1        

    # [palavra1, operador, palavra2, operador, palavra3]
    list_query = list(map(clean_text, new_query))

    query = " ".join(list_query)

    docs_searched = search(query, index, docs)

    for doc in docs_searched:
        print(punctuationCorrection(" ".join(doc)))
        print("=" * 100)

    if len(docs_searched) == 0:
        print("No result found.")


if __name__ == "__main__":
    main()
