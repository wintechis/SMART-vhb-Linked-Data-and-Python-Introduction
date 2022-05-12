from rdflib import Graph, RDFS
from rdflib.namespace import Namespace
from rdflib.query import Result, ResultRow
from rdflib.plugins.sparql import prepareQuery

#################################################
## Add triples to graph (see https://data.nobelprize.org/resource/laureate/1 for more information)[Wilhelm Conrad Röntgen]
g = Graph().parse('https://data.nobelprize.org/store/6/metadata/3743?recursive=laureate&format=text/turtle')


#################################################
## Querying local graph
qres = g.query('''
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

    SELECT ?s ?o
    WHERE {
        ?s  rdfs:label  ?o .
    }
    ''')

#################################################
## Querying local graph with prepareQuery
# q = prepareQuery('''
#     SELECT ?s ?o 
#     WHERE {
#         ?s  rdfs:label  ?o .
#     }''',
#     initNs = { "rdfs": RDFS }
# )

# qres = g.query(q)


#################################################
## Querying remote SPARQL endpoints (unstable)
#g = Graph()
#qres = g.query(
#    """
#    SELECT ?s
#    WHERE {
#      SERVICE <http://dbpedia.org/sparql> {
#        ?s a ?o .
#      }
#    }
#    LIMIT 3
#    """
#)

assert isinstance(qres, Result)
for row in qres:
    #iterating will yield lists of ResultRow objects
    assert isinstance(row, ResultRow)
    print(f'<{"> rdfs:label ".join(row.asdict().values())} .')

#################################################
# SPARQL ASK
# qres = g.query('''
#     PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

#     ASK
#     WHERE {
#         ?s  rdfs:label  ?o .
#     }
#     ''')

# print(qres.askAnswer)


#################################################
## SPARQL CONSTRUCT
# qres = g.query('''
#     PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
#     PREFIX ex: <http://example.org/>

#     CONSTRUCT {?s ex:label ?o.}
#     WHERE {
#         ?s  rdfs:label  ?o .
#     }
#     ''')

#for triple in qres:
#    print(triple)


##########################
## Print readable triples
# for triple in qres:
#     print(*map(lambda x: x.n3(), triple))



##########################
## Add CONSTRUCTED triples 
## to new graph and print
# g2 = Graph()
# for triple in qres:
#     g2.add(triple)

# for s,p,o in g2:
#     print(s,p,o)


#################################################
## SPARQL DESCRIBE (not implemented)
# try:
#     qres = g.query('''
#         PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

#         DESCRIBE ?s
#         WHERE {
#             ?s  rdfs:label  ?o .
#         }
#         ''')
# except Exception as e:
#     print(e)


#################################################
## Distinguish Result objects
# for row in qres:
#     if qres.type == 'ASK': pass
#     elif qres.type == 'CONSTRUCT': pass
#     elif qres.type == 'DESCRIBE': pass
#     elif qres.type == 'SELECT': pass