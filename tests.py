import unittest
from exercises import e1_terms, e2_namespaces
from solutions import s1_terms, s2_namespaces


###########################################
## 1 - Terms
##########################################

class E1(unittest.TestCase):

    # def setUp(self) -> None:
    #     return super().setUp()

    def test_create_triple(self):
        self.assertEqual(e1_terms.create_triple(), s1_terms.create_triple())

    def test_add_data_to_graph(self):
        self.assertEqual(e1_terms.add_data_to_graph().serialize(format='ntriples'), s1_terms.add_data_to_graph().serialize(format='ntriples'))

  
    # def tearDown(self) -> None:
    #     return super().tearDown()

###########################################
## 2 - Namespaces
##########################################

class E2(unittest.TestCase):

    # def setUp(self) -> None:
    #     return super().setUp()

    def test_create_datetime(self):
        self.assertEqual(e2_namespaces.create_datetime(), s2_namespaces.create_datetime())

    def test_reset_namespaces(self):
        g1 = e2_namespaces.reset_namespaces()
        g2 = s2_namespaces.reset_namespaces()
        
        self.assertEqual(g1.namespace_manager.store._Memory__namespace,g2.namespace_manager.store._Memory__namespace)
        self.assertEqual(g2.namespace_manager.store._Memory__prefix,g2.namespace_manager.store._Memory__prefix, msg='Make sure to clear the prefix dictionary for consistency, too!')

    # def tearDown(self) -> None:
    #     return super().tearDown()



###########################################
## Main Loop
##########################################
if __name__ == '__main__':
    unittest.main()
