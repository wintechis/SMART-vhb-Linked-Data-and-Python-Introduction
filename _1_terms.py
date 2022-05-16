##############################################################################################
## Course   : Linked Data and Python: Introduction                                          ##
## Section  : Terms                                                                         ##
## Authors  : Christian Fleiner, Andreas Harth                                              ##
## See more : https://github.com/wintechis/SMART-vhb-Linked-Data-and-Python-Introduction    ##
##                                                                                          ##
## Learning Goals:                                                                          ##
## - Understand basic terms of the RDFLib                                                   ##
## - Create a graph with triples                                                            ##
##############################################################################################

##################################################
## Import library
import rdflib

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

##################################################
## Define terms

# ## Define subjects
# alice   = rdflib.URIRef('http://example.org/Alice')
# bob     = rdflib.URIRef('http://example.org/Bob')

# ## Define predicates
# first_name  = rdflib.URIRef('http://xmlns.com/foaf/0.1/firstName')
# age         = rdflib.URIRef('http://xmlns.com/foaf/0.1/age')
# knows       = rdflib.URIRef('http://xmlns.com/foaf/0.1/knows')

# ## Define objects
# a_name  = rdflib.Literal('Alice')
# b_name  = rdflib.Literal('Bob', lang='en')
# _21     = rdflib.Literal(21)
# # Define blank nodes
# b0 = rdflib.BNode()


#################################################
## Add triples to graph

# g = rdflib.Graph()

# # ex:Alice    foaf:firstName   "Alice"^^xsd:string .
# g.add((alice, first_name, a_name))
# # ex:Alice    foaf:age         "21"^^xsd:integer .
# g.add((alice, age, _21))
# # ex:Alice    foaf:knows        ex:Bob    .
# g.add((alice, knows, bob))
# # ex:Alice    foaf:knows        _:b0    .
# g.add((alice, knows, b0))
# # ex:Bob      foaf:firstName   "Bob"@en .
# g.add((bob, first_name, b_name))


################################################
# Print serialized graph to terminal
# print('============ Graph as String ============')
# print(g.serialize(format='turtle'))




