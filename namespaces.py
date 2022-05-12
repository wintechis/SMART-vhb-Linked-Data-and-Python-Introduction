##########################################################
##                                                      ##
##                                                      ##
##                                                      ##
##########################################################



#import required classes from rdflib package
from rdflib import URIRef,Literal, BNode, Graph, FOAF, XSD
from rdflib.namespace import Namespace

#string with RDF triples in Turtle
data = '''
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> 

PREFIX ex: <http://example.org/>
#OR @prefix ex: <http://example.org/> .

ex:Alice    foaf:firstName   "Alice"^^xsd:string  ;
    foaf:age        "21"^^xsd:integer   ; 
    foaf:knows      ex:Bob    , _:b0 .

ex:Bob      foaf:firstName  "Bob"^^xsd:string   .
'''
##################################################
## Define namespace
EX = Namespace('http://example.org/')


##################################################
## Define subjects
alice   = URIRef('Alice', EX)
bob     = URIRef('Bob', EX)

## Define predicates -> obsolete

## Define objects
a_name  = Literal('Alice', datatype=XSD.string)
b_name  = Literal('Bob', datatype=XSD.string)
_21     = Literal(21, datatype=XSD.integer)

## Define blank nodes
b0 = BNode('b0')

#################################################
## Add triples to graph

g = Graph()

# ex:Alice    foaf:firstName   "Alice"^^xsd:string .
g.add((alice, FOAF.firstName, a_name))
# ex:Alice    foaf:age         "21"^^xsd:integer .
g.add((alice, FOAF.age, _21))
# ex:Alice    foaf:knows        ex:Bob    .
g.add((alice, FOAF.knows, bob))
# ex:Alice    foaf:knows        _:b0    .
g.add((alice, FOAF.knows, b0))
# ex:Bob      foaf:firstName   "Bob"^^xsd:string .
g.add((bob,   FOAF.firstName, b_name))

## Triple Removal
#g.remove((bob,   FOAF.firstName, b_name))

#################################################
## Bind namespace to graph
g.bind('ex', EX)

#################################################
## Print all triples to terminal
#print(g.serialize(format='turtle'))



#################################################
## Unbind namespace from graph
def unbind(g:Graph, ns: Namespace):
    uri = URIRef(str(ns))
    p = g.namespace_manager.store._Memory__prefix.get(uri)
    if p:
        g.namespace_manager.store._Memory__namespace.pop(p, None)
        g.namespace_manager.store._Memory__prefix.pop(uri, None)

unbind(g, EX)

print(g.serialize(format='turtle'))