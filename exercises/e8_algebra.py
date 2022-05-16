##############################################################################################
## Course   : Linked Data and Python: Introduction                                          ##
## Section  : SPARQL Algebra - Excercise                                                    ##
## Authors  : Christian Fleiner, Andreas Harth                                              ##
## See more : https://github.com/wintechis/SMART-vhb-Linked-Data-and-Python-Introduction    ##
##                                                                                          ##
## Exercises:                                                                               ##
## - 8.1 Create JOIN function                                                               ##
## - 8.2 Create UNION function                                                              ##
##############################################################################################

# ↓↓↓ START TO CODE BELOW ↓↓↓
from typing import Iterator
import rdflib
from rdflib import Graph, RDFS, FOAF
from rdflib.plugins.sparql import algebra, evaluate

#################################################
## Create dummy classes for improved type hinting
class SolutionMapping (dict):
    pass

class ResultSet (Iterator[SolutionMapping]):
    pass


##########################################################################
##  8.2 Create a JOIN operation function (do not use evaluate.evalJoin) ##
##########################################################################
def join(𝛀_l: ResultSet, 𝛀_r: ResultSet) -> ResultSet:
    𝛀_l, 𝛀_r = list(𝛀_l), list(𝛀_r)
    𝛀 = []
    #the is_compatible function might be useful
    # ↓↓↓ START TO CODE BELOW ↓↓↓



    return 𝛀


############################################################################
##  8.2 Create a UNION operation function (do not use evaluate.evalUnion) ##
############################################################################
def union(𝛀_l: ResultSet, 𝛀_r: ResultSet) -> ResultSet:
    #↓↓↓ START TO CODE BELOW ↓↓↓
    return


############################################################################
##  BEGIN: DO NOT CHANGE THE CODE                                         ##
############################################################################

#################################################
## Support Functions copied from _8_algebra
def n3(𝝁: SolutionMapping) -> SolutionMapping:
    ''' applies n3 method for all RDFLib terms in Solution Mapping '''
    return {k.n3(): v.n3() for k, v in 𝝁.items()}

def is_compatible(a: SolutionMapping, b: SolutionMapping) -> bool:
    ''' returns True, if shared variables (keys) have no conflicting values'''
    for x in a.keys() & b.keys():
        if a[x] != b[x]:
            return False
    return True

g = Graph().parse('algebra.ttl', format='ttl')


#################################################
## 𝛀_l and 𝛀_r copied from _8_algebra
tp1 = [rdflib.term.Variable('entity'), rdflib.URIRef(RDFS.label), rdflib.term.Variable('label')]
tp2 = [rdflib.term.Variable('entity'), rdflib.URIRef(FOAF.gender), rdflib.term.Variable('gender')]
tp3 = [rdflib.term.Variable('entity'), rdflib.URIRef('http://data.nobelprize.org/terms/nobelPrize'), rdflib.term.Variable('nobelprize')]

bgp1 = algebra.BGP(triples=[tp1, tp2])
bgp1.algebra = algebra.BGP(triples=[tp1, tp2])
𝛀_l = evaluate.evalQuery(g, bgp1, initBindings={})

bgp2 = algebra.BGP(triples=[tp3])
bgp2.algebra = algebra.BGP(triples=[tp3])
𝛀_r = evaluate.evalQuery(g, bgp2, initBindings={})

############################################################################
##  END: DO NOT CHANGE THE CODE                                           ##
############################################################################


if __name__ == '__main__':
    # 𝛀 = join(𝛀_l, 𝛀_r)
    # print('============ JOIN: RESULT SET ============')
    # for i, x in  enumerate(𝛀):
    #     print(i, n3(x))

    𝛀 = union(𝛀_l, 𝛀_r)
    print('============ Union: RESULT SET ============')
    for i, x in  enumerate(𝛀):
        print(i, n3(x))


