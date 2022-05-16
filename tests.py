##############################################################################################
## Course   : Linked Data and Python: Introduction                                          ##
## Section  : Tests                                                                         ##
## Authors  : Christian Fleiner, Andreas Harth                                              ##
## See more : https://github.com/wintechis/SMART-vhb-Linked-Data-and-Python-Introduction    ##
##                                                                                          ##
## How to Use:                                                                              ##
## - DO NOT CHANGE ANYTHING IN THIS FILE EXCEPT YOU WANT TO MODIFY A TEST ON YOUR OWN       ##
## - Open a console and enter "python -m unittest -v tests" to run all tests                ##
## - Open a console and enter "python -m unittest -v tests.E1" to only run exercise 1 tests ##
##############################################################################################


import unittest
from exercises import e1_terms, e2_namespaces, e3_parsing, e4_serializing, e6_querying, e8_algebra
from solutions import s1_terms, s2_namespaces, s3_parsing, s4_serializing, s6_querying, s8_algebra


###########################################
## 1 - Terms
##########################################

class E1(unittest.TestCase):

    def test_create_triple(self):
        self.assertEqual(e1_terms.create_triple(), s1_terms.create_triple())

    def test_add_data_to_graph(self):
        self.assertEqual(e1_terms.add_data_to_graph().serialize(format='ntriples'), s1_terms.add_data_to_graph().serialize(format='ntriples'))

###########################################
## 2 - Namespaces
##########################################

class E2(unittest.TestCase):

    def test_create_datetime(self):
        self.assertEqual(e2_namespaces.create_datetime(), s2_namespaces.create_datetime())

    def test_reset_namespaces(self):
        g1 = e2_namespaces.reset_namespaces()
        g2 = s2_namespaces.reset_namespaces()
        
        self.assertEqual(g1.namespace_manager.store._Memory__namespace,g2.namespace_manager.store._Memory__namespace)
        self.assertEqual(g2.namespace_manager.store._Memory__prefix,g2.namespace_manager.store._Memory__prefix, msg='Make sure to clear the prefix dictionary for consistency, too!')

###########################################
## 3 - Parsing
##########################################

class E3(unittest.TestCase):

    def test_parse_from_file(self):
        self.assertEqual(e3_parsing.parse_from_file().serialize(format='turtle'), s3_parsing.parse_from_file().serialize(format='turtle'))

    def test_parse_from_web(self):
        self.assertEqual(e3_parsing.parse_from_web().serialize(format='turtle'), s3_parsing.parse_from_web().serialize(format='turtle'))

###########################################
## 4 - Serializing
##########################################

class E4(unittest.TestCase):

    def test_serialize_example_in_xml(self):
        self.assertTrue(e4_serializing.serialize_example_in_xml(), s4_serializing.serialize_example_in_xml())

    def test_save_example_as_xml_file(self):
        e4_serializing.save_example_as_xml_file(), s4_serializing.save_example_as_xml_file()
        with open('exercises/example.rdf', 'r') as f:
            e = f.read()
        with open('solutions/example.rdf', 'r') as f:
            s = f.read()
        self.assertEqual(e, s)

###########################################
## 5 - Graphs
##########################################

class E5(unittest.TestCase):
    def test_empty_test(self):
        pass

###########################################
## 6 - Querying
##########################################

class E6(unittest.TestCase):

    def test_get_slices(self):
        ex = list(map(lambda triple: [term.n3() for term in triple], e6_querying.get_slices()))
        s = list(map(lambda triple: [term.n3() for term in triple], s6_querying.get_slices()))
        for i, e in enumerate(ex):
            self.assertEqual(e,s[i])

    def test_get_all_citations(self):
        e = set(x.n3() for x in e6_querying.get_all_citations())
        s = set(x.n3() for x in s6_querying.get_all_citations())
        
        self.assertEqual(e, s)

###########################################
## 7 - Sparql
##########################################

class E7(unittest.TestCase):
    def test_empty_test(self):
        pass

###########################################
## 8 - Algebra
##########################################
from rdflib.plugins.sparql import algebra, evaluate
import rdflib

class E8(unittest.TestCase):

    def setUp(self) -> None:
        data8 = """
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
        self.g = rdflib.Graph().parse(data=data8, format='ttl')

        tp1 = [rdflib.term.Variable('entity'), rdflib.URIRef(rdflib.RDFS.label), rdflib.term.Variable('label')]
        tp2 = [rdflib.term.Variable('entity'), rdflib.URIRef(rdflib.FOAF.gender), rdflib.term.Variable('gender')]
        tp3 = [rdflib.term.Variable('entity'), rdflib.URIRef('http://data.nobelprize.org/terms/nobelPrize'), rdflib.term.Variable('nobelprize')]

        self.bgp1 = algebra.BGP(triples=[tp1, tp2])
        self.bgp1.algebra = algebra.BGP(triples=[tp1, tp2])
        self.𝛀_l = list(evaluate.evalQuery(self.g, self.bgp1, initBindings={}))

        self.bgp2 = algebra.BGP(triples=[tp3])
        self.bgp2.algebra = algebra.BGP(triples=[tp3])
        self.𝛀_r = list(evaluate.evalQuery(self.g, self.bgp2, initBindings={}))
        return super().setUp()

    def test_join(self):
        ex = list(e8_algebra.join(self.𝛀_l, self.𝛀_r))
        s = list(s8_algebra.join(self.𝛀_l, self.𝛀_r))
        self.assertEqual(len(ex),len(s))
        for 𝝁 in ex:
            s.remove(𝝁)
        self.assertEqual(len(s),0)
        
            
    def test_union(self):
        ex = list(e8_algebra.union(self.𝛀_l, self.𝛀_r))
        s = list(s8_algebra.union(self.𝛀_l, self.𝛀_r))
        self.assertEqual(len(ex),len(s))
        for 𝝁 in ex:
            s.remove(𝝁)
        self.assertEqual(len(s),0)


###########################################
## Main Loop
##########################################
if __name__ == '__main__':
    unittest.main()
