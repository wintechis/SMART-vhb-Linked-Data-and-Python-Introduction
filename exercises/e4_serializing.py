##############################################################################################
## Course   : Linked Data and Python: Introduction                                          ##
## Section  : Serializing - Excercise                                                       ##
## Authors  : Christian Fleiner, Andreas Harth                                              ##
## See more : https://github.com/wintechis/SMART-vhb-Linked-Data-and-Python-Introduction    ##
##                                                                                          ##
## Exercises:                                                                               ##
## - 4.1 Serialize to string                                                                ##
## - 4.2 Serialize to file                                                                  ##
##############################################################################################

from rdflib import Graph

###########################################################################
##  4.1 Return a XML/RDF formatted string with the data of 'example.ttl' ##
###########################################################################

def serialize_example_in_xml() -> str:
    g = Graph()
    # ↓↓↓ START TO CODE BELOW ↓↓↓
    return 

#####################################################################################
##  4.2 Parse 'example.ttl' and serialize it in XML/RDF to 'exercises/example.rdf' ##
#####################################################################################
def save_example_as_xml_file() -> None:
    destination = 'exercises/example.rdf'
    g = Graph()
    # ↓↓↓ START TO CODE BELOW ↓↓↓


if __name__ == '__main__':
    print(serialize_example_in_xml())

    # save_example_as_xml_file()
    # print(Graph().parse('exercises/example.rdf', format='xml').serialize(format='turtle'))