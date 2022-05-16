##############################################################################################
## Course   : Linked Data and Python: Introduction                                          ##
## Section  : Parsing                                                                       ##
## Authors  : Christian Fleiner, Andreas Harth                                              ##
## See more : https://github.com/wintechis/SMART-vhb-Linked-Data-and-Python-Introduction    ##
##                                                                                          ##
## Learning Goals:                                                                          ##
## - Parse data from string, file, stream and the Web                                       ##
## - Run dummy server with Live server extension                                            ##
##############################################################################################


##################################################
## Import graph from library
from rdflib import Graph

##################################################
## Define RDF data
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

#################################################
## Add triples to graph

## By add function -> see namespaces.py

## Parse string
# g = Graph().parse(data=data, format='turtle')

## Parse local file
# g = Graph().parse(source='example.ttl')


## Parse from stream
# with open('example.ttl', 'r') as f:
#    g = Graph().parse(source=f)

## Parse Web resource / with Live Server Extension from Ritwick Dey
# g = Graph().parse(location='http://127.0.0.1:5500/example.ttl')

################################################
# Print serialized graph to terminal
# print('============ Graph as String ============')
# print(g.serialize(format='turtle'))
