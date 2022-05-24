##############################################################################################
## Course   : Linked Data and Python: Introduction                                          ##
## Section  : SPARQL Queries / Requests                                                     ##
## Authors  : Christian Fleiner, Andreas Harth                                              ##
## See more : https://github.com/wintechis/SMART-vhb-Linked-Data-and-Python-Introduction    ##
##                                                                                          ##
## Learning Goals:                                                                          ##
## - Execute SPARQL queries on graphs                                                       ##
## - Prepare SPARQL queries with the prepareQuery function                                  ##
##############################################################################################

##################################################
## Import classes from library
from rdflib import Graph, RDFS
from rdflib.query import Result, ResultRow
from rdflib.plugins.sparql import prepareQuery

#################################################
## Load graph (see https://data.nobelprize.org/resource/laureate/1 for more information)[Wilhelm Conrad Röntgen]
g = Graph().parse('https://data.nobelprize.org/store/6/metadata/3743?recursive=laureate&format=text/turtle')

#################################################
## Querying local graph
# qres = g.query('''
#     PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

#     SELECT ?s ?o
#     WHERE {
#         ?s  rdfs:label  ?o .
#     }
#     ''')

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
## Querying remote SPARQL endpoints (unstable) (example from: https://rdflib.readthedocs.io/en/stable/intro_to_sparql.html)
# g = Graph()
# qres = g.query(
#    """
#    SELECT ?s
#    WHERE {
#      SERVICE <http://dbpedia.org/sparql> {
#        ?s a ?o .
#      }
#    }
#    LIMIT 3
#    """
# )

# assert isinstance(qres, Result)
# print('============ SPARQL SELECT Result ============')
# for i, row in enumerate(qres, start=1):
#     #iterating will yield lists of ResultRow objects
#     assert isinstance(row, ResultRow)
#     print(i, [x.n3() for x in row])

#################################################
# SPARQL ASK
# qres = g.query('''
#     PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

#     ASK
#     WHERE {
#         ?s  rdfs:label  ?o .
#     }
#     ''')
# print('============ SPARQL ASK Result ============')
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
# print('============ SPARQL CONSTRUCT Result ============')
# for i, triple in enumerate(qres, start=1):
#    print(i, [x.n3() for x in triple])



#################################################
## Add CONSTRUCTED triples 
## to new graph and print
# g2 = Graph()
# for triple in qres:
#     g2.add(triple)

# for i, triple in enumerate(g2, start=1):
#     print(i, [x.n3() for x in triple])


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

#################################################
## UPDATE Graph
g = Graph()
g.update('''
PREFIX ex: <http://example.org/>
INSERT DATA {
    ex:alice   ex:knows     ex:bob .
}

''')
print(g.serialize(format='ttl'))