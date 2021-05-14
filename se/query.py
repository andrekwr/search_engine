from __future__ import annotations

import json

from se.index import Index


class Node:
    def evaluate(self, index: Index):
        return set()


class Term(Node):
    def __init__(self, term):
        super().__init__()
        self.term = term

    def evaluate(self, index: Index):
        return set(index.lookup(self.term))


class Operation(Node):
    def __init__(self, nodes: list[Node]):
        super().__init__()
        self.nodes = nodes

    def combine(self, result, new_results):
        return set()

    def evaluate(self, index: Index):
        result = self.nodes[0].evaluate(index)
        for node in self.nodes[1:]:
            result = self.combine(result, node.evaluate(index))
        return result


class OpAnd(Operation):
    def __init__(self, nodes):
        super().__init__(nodes)

    def combine(self, result, new_results):
        return result & new_results


class OpOr(Operation):
    def __init__(self, nodes):
        super().__init__(nodes)

    def combine(self, result, new_results):
        return result | new_results


def build_query(query):
    node_type = query[0]
    if node_type == "term":
        # ["term", "abelha"]
        return Term(query[1])
    else:
        # ["and", [or, ["term", "non"], ["term", not]], [or, ["term", "safe"], ["term", "condom"]]]
        arg_list = []
        for arg in query[1:]:
            arg_node = build_query(arg)
            arg_list.append(arg_node)
        if node_type == "and":
            return OpAnd(arg_list)
        elif node_type == "or":
            return OpOr(arg_list)
        else:
            raise KeyError(f"Operação {node_type} desconhecida.")


def parse_raw_query_or(q, i, n):
    result = f'["term", "{q[i]}"]'
    i += 1
    if i == n:
        return result, i
    if len(q) % 2 == 0:
        raise Exception("Query incompleta.")
    elif len(q) > 1:
        while q[i] == "or":
            res, i = parse_raw_query_or(q, i + 1, n)
            result = f'["or", {result}, {res}]'
            if i == n:
                return result, i

    return result, i


def parse_raw_query(raw_query: str):
    q = raw_query.split()
    n = len(q)
    result, i = parse_raw_query_or(q, 0, n)
    if i == n:
        return result
    while q[i] == "and":
        res, i = parse_raw_query_or(q, i + 1, n)
        result = f'["and", {result}, {res}]'
        if i == n:
            return result
    return result


def parse_json_query(json_query: str):
    q = json.loads(json_query)
    query = build_query(q)
    return query
