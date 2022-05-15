from rdflib import Literal, XSD, Graph

##########################################################
## Datetime / 2022-05-01T18:25:43+1

def create_datetime() -> Literal:
    return Literal('2022-05-01T18:25:43+1', datatype=XSD.dateTime)

##########################################################
## Namespaces are preloaded
def reset_namespaces() -> Graph:
    g = Graph()
    g.namespace_manager.store._Memory__namespace = {}
    g.namespace_manager.store._Memory__prefix = {}
    return g

if __name__ == '__main__':
    print(create_datetime())
    #print([ns for ns in reset_namespaces().namespaces()])
    #python -m unittest -v  tests.E2