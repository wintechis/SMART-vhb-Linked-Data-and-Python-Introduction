##########################################################
##                                                      ##
##                                                      ##
##                                                      ##
##########################################################



#import the rdflib package
import rdflib

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
## Define subjects
alice   = rdflib.URIRef('http://example.org/Alice')
bob     = rdflib.URIRef('http://example.org/Bob')

## Define predicates
first_name  = rdflib.URIRef('http://xmlns.com/foaf/0.1/firstName')
age         = rdflib.URIRef('http://xmlns.com/foaf/0.1/age')
knows       = rdflib.URIRef('http://xmlns.com/foaf/0.1/knows')

## Define objects
a_name  = rdflib.Literal('Alice')
b_name  = rdflib.Literal('Bob', lang='en')
_21     = rdflib.Literal(21)

## Define blank nodes
b0 = rdflib.BNode()


#################################################
## Add triples to graph

g = rdflib.Graph()

# ex:Alice    foaf:firstName   "Alice"^^xsd:string .
g.add((alice, first_name, a_name))
# ex:Alice    foaf:age         "21"^^xsd:integer .
g.add((alice, age, _21))
# ex:Alice    foaf:knows        ex:Bob    .
g.add((alice, knows, bob))
# ex:Alice    foaf:knows        _:b0    .
g.add((alice, knows, b0))
# ex:Bob      foaf:firstName   "Bob"@en .
g.add((bob, first_name, b_name))


#################################################
## Print all triples to terminal
print(g.serialize(format='turtle'))




