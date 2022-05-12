from re import X
from rdflib import FOAF, Graph, RDF, RDFS, URIRef, Literal, BNode
from rdflib.namespace import Namespace
from rdflib.query import Result, ResultRow
from rdflib.plugins.sparql import prepareQuery

#################################################
## Add triples to graph (see https://data.nobelprize.org/resource/laureate/1 for more information)[Wilhelm Conrad Röntgen]
g = Graph().parse('https://data.nobelprize.org/store/6/metadata/3743?recursive=laureate&format=text/turtle')


#################################################
## Iterating over all triples
# for triple in g:
#     print(*triple)

#################################################
## Iterating over all triple terms
# for s, p, o in g:
#     print(s,p,o)

#################################################
## Iterating over specific terms
# for s in g.subjects:
#     print(s)

#################################################
## Iterating over selective terms
# for s in g.subjects(predicate=RDFS.label, object=None):
#     print(s)

#################################################
## Iterating over selective term combinations
# for s, o in g.subject_objects(predicate=RDFS.label):
#     print(s, o)

#################################################
## Iterating over selective term combinations
# alice = URIRef('http://example.org/alice')
# a_name = Literal('Alice')
# g.add((alice, RDFS.label, a_name ))
# print(g.value(predicate=RDFS.label, object=a_name))



#################################################
## Transistive Closure (see <https://rdflib.readthedocs.io/en/stable/apidocs/rdflib.html?highlight=transitive#rdflib.transitiveClosure> for more information)
# data = """
# PREFIX foaf: <http://xmlns.com/foaf/0.1/>
# PREFIX ex: <http://example.org/>

# ex:alice foaf:knows  (ex:bob ex:charlie ex:daisy) .
# #ex:alice foaf:member  (ex:gym ex:club) .
# """

# g = Graph().parse(data=data)

# def topList(node,g):
#    for s in g.subjects(RDF.rest, node):
#       yield s
# l = []
# for bn in [bn for bn in g.transitiveClosure(topList, RDF.nil)][::-1]:
#      l.append(g.value(subject=bn, predicate=RDF.first))
# print(l)


#################################################
## Get items from single list
# def get_list_items(g:Graph, bn: BNode, l=list()) -> list:
#     next_bn = g.value(subject=bn, predicate=RDF.rest)
#     l.append(g.value(subject=bn, predicate=RDF.first))
#     if next_bn != RDF.nil: 
#         get_list_items(g, next_bn)
#     return l

# alice = URIRef('http://example.org/alice')
# bn = g.value(subject=alice, predicate=FOAF.knows)

# x = get_list_items(g,bn)
# print(x)


