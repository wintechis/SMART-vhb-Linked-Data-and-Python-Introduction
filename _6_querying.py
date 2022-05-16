##############################################################################################
## Course   : Linked Data and Python: Introduction                                          ##
## Section  : Querying/Navigation                                                           ##
## Authors  : Christian Fleiner, Andreas Harth                                              ##
## See more : https://github.com/wintechis/SMART-vhb-Linked-Data-and-Python-Introduction    ##
##                                                                                          ##
## Learing Goals:                                                                           ##
## - Apply graph methods to extract triples                                                 ##
## - Retrieve list objects transitively and recursively                                     ##
##############################################################################################

##################################################
## Import classes from library
from tracemalloc import start
from rdflib import FOAF, RDF, RDFS
from rdflib import Graph, URIRef, Literal, BNode

#################################################
## Add triples to graph (see https://data.nobelprize.org/resource/laureate/1 for more information)[Wilhelm Conrad Röntgen]
g = Graph().parse('https://data.nobelprize.org/store/6/metadata/3743?recursive=laureate&format=text/turtle')

#################################################
# Iterating over all triples
# print('============ Iterating over triples ============')
# for i, triple in enumerate(g, start=1):
#     print(i, *triple)

#################################################
# Iterating over all triple terms
# print('============ Iterating over triple terms ============')
# for i, (s, p, o) in enumerate(g, start=1):
#     print(i, s, p, o)

#################################################
## Iterating over specific terms
# print('============ Iterating over specific terms ============')
# for i, s in enumerate(g.subjects(), start=1):
#     print(i, s)

#################################################
## Iterating over selective terms
# print('============ Iterating over selective terms ============')
# for i, s in enumerate(g.subjects(predicate=RDFS.label, object=None), start=1):
#     print(i, s)

#################################################
## Iterating over selective term combinations
# print('============ Iterating over selective term combinations ============')
# for i, (s, o) in enumerate(g.subject_objects(predicate=RDFS.label), start=1):
#     print(i, s, o)

#################################################
## Retrieving term with value
# alice = URIRef('http://example.org/alice')
# a_name = Literal('Alice')
# g.add((alice, RDFS.label, a_name ))
# print('============ Retrieving term with value ============')
# print(g.value(predicate=RDFS.label, object=a_name))



#################################################
## Retrieve Lists
# data = """
# PREFIX foaf: <http://xmlns.com/foaf/0.1/>
# PREFIX ex: <http://example.org/>

# ex:alice foaf:knows  (ex:bob ex:charlie ex:daisy) .
# #ex:alice foaf:member  (ex:gym ex:club) .
# """
# g = Graph().parse(data=data)

## Transistive Closure (see <https://rdflib.readthedocs.io/en/stable/apidocs/rdflib.html?highlight=transitive#rdflib.transitiveClosure> for more information)
# def topList(node,g):
#    for s in g.subjects(RDF.rest, node):
#       yield s
# l = []
# for bn in [bn for bn in g.transitiveClosure(topList, RDF.nil)][::-1]:
#      l.append(g.value(subject=bn, predicate=RDF.first))
# print([x.n3() for x in l])


## Get objects from single list
# def get_list_items(g:Graph, bn: BNode, l=list()) -> list:
#     next_bn = g.value(subject=bn, predicate=RDF.rest)
#     l.append(g.value(subject=bn, predicate=RDF.first))
#     if next_bn != RDF.nil: 
#         get_list_items(g, next_bn)
#     return l

# alice = URIRef('http://example.org/alice')
# bn = g.value(subject=alice, predicate=FOAF.knows)

# l = get_list_items(g,bn)
# print([x.n3() for x in l])


