from se.query import parse_raw_query
from se.retrieve import retrieve
from se.rank import rank_documents


def search(raw_query, index, docs):
    query = parse_raw_query(raw_query)
    index_query = retrieve(index, query)
    ranked_index = rank_documents(query, docs, index_query, index)
    return [docs[k] for k in ranked_index]
