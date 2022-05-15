from typing import Iterator, Literal
from rdflib import Graph, URIRef

citations = '''
PREFIX ex: <http://example.org/>

ex:a ex:cites ex:b , ex:c .
ex:b ex:cites ex:c .
ex:d ex:cites ex:a, ex:f .
ex:e ex:cites ex:d, ex:c .


'''

#return the 3. to 5. triple of the graph
def get_slices() -> list[dict]:
    #Nobel Peace Prize 2020
    g = Graph().parse('https://data.nobelprize.org/store/6/metadata/3886?recursive=nobelprize&format=text/turtle', format='turtle')
    return sorted(list(g))[2:4]

#return all documents that were cited (make use of the transitive_objects method of a graph) 
def get_all_citations() -> Iterator[URIRef]:
    g = Graph().parse(data=citations, format='turtle')
    return g.transitive_objects(subject=URIRef('http://example.org/d'), predicate=URIRef('http://example.org/cites'))




if __name__ == '__main__':
    print(list(map(lambda triple: [term.n3() for term in triple], get_slices())))
    #print([x.n3() for x in get_all_citations()])