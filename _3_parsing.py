##########################################################
##                                                      ##
##                                                      ##
##                                                      ##
##########################################################



#import required classes from rdflib package
from rdflib import Graph

#string with RDF triples in Turtle
data = '''
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> 

PREFIX ex: <http://example.org/>
#OR @prefix ex: <http://example.org/> .

ex:Alice    foaf:firstName   "Alice"^^xsd:string  ;
    foaf:age        "21"^^xsd:integer   ; 
    foaf:knows      ex:Bob    .

ex:Bob      foaf:firstName  "Bob"^^xsd:string   .
'''

#################################################
## Add triples to graph

## by add function -> see namespaces.py


## parse string
g = Graph().parse(data=data, format='turtle')

## parse local file
#g = Graph().parse(source='example.ttl')


## parse from stream
#with open('example.ttl', 'r') as f:
#    g = Graph().parse(source=f)

## parse Web resource
#g = Graph().parse(location='http://127.0.0.1:5500/example.ttl')

#################################################
## Print all triples to terminal
print(g.serialize(format='turtle'))
