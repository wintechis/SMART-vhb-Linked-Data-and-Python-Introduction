from typing import Iterator

import rdflib
from rdflib.plugins.sparql import algebra, evaluate
from rdflib.plugins.sparql.sparql import QueryContext
from rdflib.plugins.sparql.parserutils import CompValue
from rdflib import FOAF, RDFS, Graph

#################################################
## Create dummy classes for improved type hinting
class SolutionMapping (dict):
    pass

class ResultSet (Iterator[SolutionMapping]):
    pass


#################################################
## Load data

##  Excerpt from the Nobel Prize winners in Physics 2021/2020
data = """
PREFIX dbo: <http://dbpedia.org/ontology/> 
PREFIX foaf: <http://xmlns.com/foaf/0.1/> 
PREFIX nobel: <http://data.nobelprize.org/terms/> 
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> 

PREFIX laureate: <http://data.nobelprize.org/resource/laureate/>
PREFIX university: <http://data.nobelprize.org/resource/university/>
PREFIX year: <http://data.nobelprize.org/resource/nobelprize/Physics/>

laureate:1000 rdfs:label "Klaus Hasselmann" ;
    nobel:nobelPrize year:2021 ;
    dbo:affiliation university:Max_Planck_Institute_for_Meteorology ;
    foaf:gender "male" .

laureate:1001 rdfs:label "Giorgio Parisi" ;
    nobel:nobelPrize year:2021 ;
    dbo:affiliation university:Sapienza_University_of_Rome ;
    foaf:gender "male" .

laureate:988 rdfs:label "Roger Penrose" .
    
laureate:989 rdfs:label "Reinhard Genzel" .
   
laureate:990 rdfs:label "Andrea Ghez" ;
    foaf:gender "female" .

laureate:999 rdfs:label "Syukuro Manabe" ;
    nobel:nobelPrize year:2021 ;
    dbo:affiliation university:Princeton_University .
"""
g = Graph().parse(data=data, format='ttl')


#################################################
## Create BGP expression
tp1 = [rdflib.term.Variable('x'), rdflib.URIRef(RDFS.label), rdflib.term.Variable('l')]
tp2 = [rdflib.term.Variable('x'), rdflib.URIRef(FOAF.gender), rdflib.term.Variable('g')]

bgp = CompValue("BGP")
#bgp = algebra.BGP(triples=[tp1, tp2])
bgp.algebra = algebra.BGP(triples=[tp1, tp2])


#################################################
## Return valid triples
# result_set = evaluate.evalQuery(g, bgp, initBindings={})
# print('============ RESULT SET ============')
# for i, solution_mapping in enumerate(result_set, start=1):
#   print(f'{i}: {solution_mapping}')

#################################################
## Convert RDFLib terms to native datatypes

def n3(𝝁: SolutionMapping) -> SolutionMapping:
    ''' applies n3 method for all RDFLib terms in Solution Mapping '''
    return {k.n3(): v.n3() for k, v in 𝝁.items()}

# 𝛀 = evaluate.evalQuery(g, bgp, initBindings={})
# print('============ RESULT SET ============')
# for i, 𝝁 in enumerate(𝛀, start=1):
#   print(f'{i}: {n3(𝝁)}')


#################################################
## Check solution mapping compatibility
def is_compatible(a: SolutionMapping, b: SolutionMapping) -> bool:
    ''' returns True, if shared variables (keys) have no conflicting values'''
    for x in a.keys() & b.keys():
        if a[x] != b[x]:
            return False
    return True

𝝁_1 = {'?x': '<http://data.nobelprize.org/resource/laureate/1000>', '?l': '"Klaus Hasselmann"', '?g': '"male"'}
𝝁_2 = {'?x': '<http://data.nobelprize.org/resource/laureate/1000>', '?n': '"<http://data.nobelprize.org/terms/nobelPrize>"'}

# print(is_compatible(𝝁_1, 𝝁_2))

#################################################
## Check compatibility of multiple solution mappings

# def are_all_compatible(*args: SolutionMapping) -> bool:
#     for a in args[:-1]:
#         for b in args[1:]:
#             if not is_compatible(a,b):
#                 return False
#     return True

𝝁_3 = {'?x': '<http://data.nobelprize.org/resource/laureate/988>', '?l': '"Roger Penrose"'}
𝝁_4 = {'?y': '<http://data.nobelprize.org/resource/laureate/988>', '?k': '"Roger Penrose"'}

# print(are_all_compatible(𝝁_1, 𝝁_2, 𝝁_3, 𝝁_4))

#################################################
## Merging compatible solution mapppings
# 𝝁_34 = 𝝁_3 | 𝝁_4
# print(𝝁_34)


#################################################
## JOIN Operation
tp1 = [rdflib.term.Variable('entity'), rdflib.URIRef(RDFS.label), rdflib.term.Variable('label')]
tp2 = [rdflib.term.Variable('entity'), rdflib.URIRef(FOAF.gender), rdflib.term.Variable('gender')]
tp3 = [rdflib.term.Variable('entity'), rdflib.URIRef('http://data.nobelprize.org/terms/nobelPrize'), rdflib.term.Variable('nobelprize')]

bgp1 = algebra.BGP(triples=[tp1, tp2])
bgp1.algebra = algebra.BGP(triples=[tp1, tp2])
𝛀_l = evaluate.evalQuery(g, bgp1, initBindings={})

bgp2 = algebra.BGP(triples=[tp3])
bgp2.algebra = algebra.BGP(triples=[tp3])
𝛀_r = evaluate.evalQuery(g, bgp2, initBindings={})

# ctx = QueryContext(g, initBindings={})
# join_ = algebra.Join(bgp1, bgp2)
# print('============ JOIN: RESULT SET ============')
# for i, x in  enumerate(evaluate.evalJoin(ctx, join_)):
#     print(i, n3(x))


#################################################
## UNION Operation
# ctx = QueryContext(g, initBindings={})
# union_ = algebra.Union(bgp1, bgp2)
# print('============ UNION: RESULT SET ============')
# for i, x in  enumerate(evaluate.evalUnion(ctx, union_)):
#     print(i, n3(x))




