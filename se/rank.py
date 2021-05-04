import numpy as np

# Podemos remover?
def score_document(query, doc):
    score = 0
    for word in doc:
        if word in query:
            score += 1
    return score


def score_document_tf_idf(query, doc_number, doc, index):
    N = len(doc)
    tf_idf = 0
    for word in query:
        tf_idf += np.log2(1 + index[word][str(doc_number)]) * np.log2(
            N / len(index[word])
        )
    #print(tf_idf)
    return tf_idf


def rank_documents(query, docs, index_query, index):
    ranked_index = []
    for doc_number in index_query:
        doc_number = int(doc_number)
        doc = docs[doc_number]
        score = score_document_tf_idf(query, doc_number, doc, index)
        ranked_index.append((score, doc_number))
    ranked_index = sorted(ranked_index, key=lambda x: -x[0])
    return [item[1] for item in ranked_index]
