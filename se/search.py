import json
from se.query import parse_raw_query, parse_json_query, build_query, parse_raw_query_or
from se.retrieve import retrieve
from se.rank import rank_documents
from se.index import Index


def search(raw_query, index, docs):
    jsonquery = parse_raw_query(raw_query)
    parsedAndBuiltQuery = parse_json_query(jsonquery)

    raw_query = raw_query.split()
    raw_query = [raw_query[i] for i in range(len(raw_query)) if i % 2 == 0]

    idx = Index(index)

    index_query = parsedAndBuiltQuery.evaluate(idx)
    ranked_index = rank_documents(raw_query, docs, index_query, idx)
    return [docs[k] for k in ranked_index]
