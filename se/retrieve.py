from se.index import Index


def retrieve(index, query):
    idx = Index(index)
    index_query = set(idx.lookup(query[0]))
    for query_term in query[1:]:
        index_query &= set(idx.lookup(query_term))
    return index_query
