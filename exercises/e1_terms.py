##########################################################
##  Exercise 1 - Terms                                  ##
##  Version: 1.0                                        ##
##  Task Description: Creat                             ##
##########################################################

from typing import Literal
import rdflib

##########################################################
## 
data1 = '''<http://example.org/Alice> <http://example.org/weight> 63.5 '''

def create_triple() -> tuple:
    alice = rdflib.URIRef('http://example.org/Alice')
    p_weight = rdflib.URIRef('http://example.org/weight')
    o_weight = rdflib.Literal(63.5)

    return (alice, p_weight, o_weight)

##########################################################
##

data1 = '''
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX ex: <http://example.org/>

ex:Alice    foaf:knows (:Bob :Charlie :Daisy) .  
'''

def add_data_to_graph() -> rdflib.Graph:
    # create graph instance
    g = rdflib.Graph()

    #create terms
    alice = rdflib.URIRef('http://example.org/Alice')
    bob = rdflib.URIRef('http://example.org/Bob')
    charlie = rdflib.URIRef('http://example.org/Charlie')
    daisy = rdflib.URIRef('http://example.org/Daisy')
    knows = rdflib.URIRef('http://xmlns.com/foaf/0.1/knows')
    
    first = rdflib.URIRef('http://www.w3.org/1999/02/22-rdf-syntax-ns#first')
    rest = rdflib.URIRef('http://www.w3.org/1999/02/22-rdf-syntax-ns#rest')
    nil = rdflib.URIRef('http://www.w3.org/1999/02/22-rdf-syntax-ns#nil')

    #add triples to graph
    g.add((alice, knows, rdflib.BNode(1)))
    g.add((rdflib.BNode(1), first, bob))
    g.add((rdflib.BNode(1), rest, rdflib.BNode(2)))
    g.add((rdflib.BNode(2), first, charlie))
    g.add((rdflib.BNode(2), rest, rdflib.BNode(3)))
    g.add((rdflib.BNode(3), first, daisy))
    g.add((rdflib.BNode(3), rest, nil))
 
    return g


if __name__ == '__main__':
    print(create_triple())
    #print(add_data_to_graph().serialize(format='turtle'))
    #python -m unittest -v  tests.E1
    
    
