from rdflib import ConjunctiveGraph, Dataset, Graph, URIRef

##################################################
a = '''
PREFIX ex: <http://example.org/> 

ex:alice    ex:knows    ex:bob. 

'''

b = '''
PREFIX ex: <http://example.org/> 

ex:alice    ex:knows    ex:bob . 
ex:bob      ex:knows    ex:charlie, ex:daisy . 

'''

c = '''
PREFIX ex: <http://example.org/> 

ex:charlie    ex:knows    ex:bob, ex:daisy . 

'''

g_a = Graph().parse(data=a, format='ttl')
g_b = Graph().parse(data=b, format='ttl')
g_c = Graph().parse(data=c, format='ttl')


#################################################
## Triple count
# print('============ Graph Length ============')
# for i, g in enumerate([g_a, g_b, g_c]):
#     print(chr(65+i), len(g))


#################################################
## Graph Operations

# return new graph with union (triples on both)
# print('============ Addition ============')
# for i, triple in enumerate(g_a + g_c, start=1):
#     print(i, [x.n3() for x in triple])

# in place union / addition
# g_b += g_a
# print('============ In Place Addition ============')
# for i, triple in enumerate(g_b, start=1):
#     print(i, [x.n3() for x in triple])

# return new graph with difference (triples in G1, not in G2)
# print('============ Difference ============')
# for i, triple in enumerate(g_b - g_a, start=1):
#     print(i, [x.n3() for x in triple])

# in place difference / subtraction
# g_b -= g_a
# print('============ In Place Difference ============')
# for i, triple in enumerate(g_b, start=1):
#       print(i, [x.n3() for x in triple])

# intersection (triples in both graphs)
# print('============ Intersection ============')
# for i, triple in enumerate(g_b & g_a, start=1):
#     print(i, [x.n3() for x in triple])

# xor (triples in either G1 or G2, but not in both)
# print('============ XOR ============')
# for i, triple in enumerate(g_b ^ g_a, start=1):
#     print(i, [x.n3() for x in triple])


#################################################
## Conjunctive Graph


# g = ConjunctiveGraph()
# g.parse(data=a)
# g.parse(data=b)
# g.parse(data=c)


# print('============ CG: Identifiers ============')
# for i, x in enumerate(g.contexts()):
#     print(x.identifier, x)

# print('============ CG: Context by Identifier ============')
# identifier = [c.identifier for c in g.contexts()][1]
# for i, triple in enumerate(g.get_context(identifier)):
#     print(i, [x.n3() for x in triple])


#################################################
## Dataset

# g_a = Graph(identifier=URIRef('http://a.org/graph.ttl')).parse(data=a, format='ttl')
# g_b = Graph(identifier=URIRef('http://b.org/graph.ttl')).parse(data=b, format='ttl')
# g_c = Graph(identifier=URIRef('http://c.org/graph.ttl')).parse(data=c, format='ttl')


# d = Dataset()
# d.add_graph(g_a)
# d.add_graph(g_b)
# d.add_graph(g_c)


# print('============ Dataset: Identifiers ============')
# for i, x in enumerate(d.contexts()):
#     print(i, x.identifier, x)

# print('============ Dataset: Context by Identifier ============')
# for c in d.contexts():
#     if c.identifier == URIRef('http://a.org/graph.ttl'):
#         for i, triple in enumerate(c, start=1):
#             print(i, [x.n3() for x in triple])


# print('============ Dataset: Graph by Identifier ============')
# for g in d.graphs():
#     if g.identifier == URIRef('http://a.org/graph.ttl'):
#         for i, triple in enumerate(c, start=1):
#             print(i, [x.n3() for x in triple])


# d.remove_graph(URIRef('http://a.org/graph.ttl'))
# print('============ Dataset: Remove Graph ============')
# for i, x in enumerate(d.contexts(), start=1):
#     print(i, x.identifier, x)


