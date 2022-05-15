from rdflib import Graph



def serialize_example_in_xml() -> str:
    return Graph().parse('example.ttl', format='turtle').serialize(format='application/rdf+xml')


def save_example_as_xml_file() -> None:
    Graph().parse('example.ttl', format='turtle').serialize(destination='solutions/example.rdf', format='application/rdf+xml')


if __name__ == '__main__':
    print(serialize_example_in_xml())

    #save_example_as_xml_file()
    #print(Graph().parse('solutions/example.rdf', format='xml').serialize(format='turtle'))