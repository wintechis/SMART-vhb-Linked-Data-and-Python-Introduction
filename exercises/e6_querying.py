##############################################################################################
## Course   : Linked Data and Python: Introduction                                          ##
## Section  : Querying/Navigation - Excercise                                               ##
## Authors  : Christian Fleiner, Andreas Harth                                              ##
## See more : https://github.com/wintechis/SMART-vhb-Linked-Data-and-Python-Introduction    ##
##                                                                                          ##
## Exercises:                                                                               ##
## - 6.1 Retrieve triple range from triple list                                             ##
## - 6.2 Use transitive methods                                                             ##
##############################################################################################

from typing import Iterator
from rdflib import Graph, URIRef

###################################################
##  6.1 Return the 2. and 3. triple of the graph ##
###################################################

def get_slices() -> list[dict]:
    #Nobel Peace Prize 2020
    g = Graph().parse('https://data.nobelprize.org/store/6/metadata/3886?recursive=nobelprize&format=text/turtle', format='turtle')
    l = sorted(list(g))
    # ↓↓↓ START TO CODE BELOW ↓↓↓
    return

###################################################################################################################################
##  6.2 Return all documents that were cited by d directly or indirectly (make use of the transitive_objects method of a graph)  ##
###################################################################################################################################
citations = '''
PREFIX ex: <http://example.org/>

ex:a ex:cites ex:b , ex:c .
ex:b ex:cites ex:c .
ex:d ex:cites ex:a, ex:f .
ex:e ex:cites ex:d, ex:c .


'''
def get_all_citations() -> Iterator[URIRef]:
    g = Graph().parse(data=citations, format='turtle')
    # Use g.transitive_objects()
     # ↓↓↓ START TO CODE BELOW ↓↓↓
    return 

if __name__ == '__main__':
    print(list(map(lambda triple: [term.n3() for term in triple], get_slices())))
    #print([x.n3() for x in get_all_citations()])