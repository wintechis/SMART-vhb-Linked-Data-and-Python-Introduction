import rdflib
from rdflib.plugins.sparql import algebra, evaluate
from rdflib.plugins.sparql.parserutils import CompValue

##  Evaluation of BGP Expressions
ttl = """
@prefix ex: <http://example.org/baz#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> . 
@prefix : <http://harth.org/astro-graph#> . 
:Sonne  ex:radius "1.392e6"^^xsd:double ; 
        ex:satellit :Merkur, :Venus, :Erde, :Mars ;
        ex:name "Sun" .
:Merkur ex:radius "2439.7"^^xsd:double . 
:Venus ex:radius "6051.9"^^xsd:double . 
:Erde ex:radius "6372.8"^^xsd:double ; 
      ex:satellit :Mond . 
:Mars ex:radius "3402.5"^^xsd:double ; 	  
      ex:satellit :Phobos, :Deimos . 
:Mond ex:name "Mond"@de, "Moon"@en ; 
      ex:radius "1737.1"^^xsd:double . 
:Phobos ex:name "Phobos" . 
:Deimos ex:name "Deimos" . 
"""
class SolutionMapping (dict):
    pass



def n3(𝝁: SolutionMapping):
    return {k.n3(): v.n3() for k, v in 𝝁.items()}
   

tp1 = [rdflib.term.Variable('x'), rdflib.URIRef('http://example.org/baz#radius'), rdflib.term.Variable('r')]
tp2 = [rdflib.term.Variable('x'), rdflib.URIRef('http://example.org/baz#name'), rdflib.term.Variable('n')]
#bgp = algebra.BGP(triples=[tp1, tp2])

bgp = CompValue("BGP")
#bgp = algebra.BGP(triples=[tp1, tp2])
bgp.algebra = algebra.BGP(triples=[tp1, tp2])


g = rdflib.Graph().parse(data=ttl)
results = evaluate.evalQuery(g, bgp, initBindings={})
#for answer in results:
#   print('answer', n3(answer))


###  Solution Mapping Compatibility


def compatible(a: SolutionMapping, b: SolutionMapping) -> bool:
    for x in a.keys() & b.keys():
        if a[x] != a[x]:
            return False
    return True

def all_compatible(*args: SolutionMapping) -> bool:
    for a in args[:-1]:
        for b in args[1:]:
            if not compatible(a,b):
                return False
    return True

𝝁_4 = {'?x': '<http://harth.org/astro-graph#Mond>', '?r': '"1737.1"^^<http://www.w3.org/2001/XMLSchema#double>'}
𝝁_5 = {'?x': '<http://harth.org/astro-graph#Mond>', '?r': '"1737.1"^^<http://www.w3.org/2001/XMLSchema#double>'}
𝝁_6 = {'?x': '<http://harth.org/astro-graph#Mond>', '?r': '"1760.0"^^<http://www.w3.org/2001/XMLSchema#double>'}
𝝁_7 = {'?x': '<http://harth.org/astro-graph#Mond>', '?r': '"1737.1"^^<http://www.w3.org/2001/XMLSchema#double>'}
#print(all_compatible(mu5, mu4, mu7, mu6))


𝝁_3 = {'?x': '"<http://harth.org/astro-graph#Mond>"', '?r': '"1737.1"^^<http://www.w3.org/2001/XMLSchema#double>'}
𝝁_4 = {'?x': '"<http://harth.org/astro-graph#Mond>"', '?n': '"Moon"@en'}

## merging of compatible solution mapppings
𝝁_45 = 𝝁_3 | 𝝁_4

print(μ_45)


𝛀 = [n3(answer) for answer in results]

print(𝛀)

