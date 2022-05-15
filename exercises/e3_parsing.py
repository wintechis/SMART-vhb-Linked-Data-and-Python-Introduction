from rdflib import Graph

data3 = """
    PREFIX ex: <http://example.org/>

    ex:alice ex:lies ex:ice_cream .

    ex:ice_cream ex:is  ex:cold ;
        ex:flavour  'vanilla' .
    """

##########################################################
## Create a turtle file with the content given in data3
def parse_from_file():
    g = Graph()
    try:
        g.parse('exercises/ice_cream.ttl')
    except FileNotFoundError as e:
        print(f'{e}\nCreate a file "ice_cream.ttl" in folder "exercises" or change the filepath!')
    return g

##########################################################
##  Parse a Web resource in the format 'application/rdf+xml' (xml) instead of 'turtle'
def parse_from_web():
    g = Graph()
    g.parse('https://data.nobelprize.org/store/6/metadata/1930?recursive=nobelprize&format=application/rdf+xml', format='xml')
    return g





if __name__ == '__main__':
    #print(parse_from_file().serialize(format='turtle'))
    print(parse_from_web().serialize(format='turtle'))