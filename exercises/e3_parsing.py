##############################################################################################
## Course   : Linked Data and Python: Introduction                                          ##
## Section  : Parsing - Excercise                                                           ##
## Authors  : Christian Fleiner, Andreas Harth                                              ##
## See more : https://github.com/wintechis/SMART-vhb-Linked-Data-and-Python-Introduction    ##
##                                                                                          ##
## Exercises:                                                                               ##
## - 3.1 Parse data from file                                                               ##
## - 3.2 Parse data from Web resource                                                       ##
##############################################################################################

from rdflib import Graph

######################################################################
##  3.1 Create a graph with the content of 'exercises/ice_cream.ttl ##
######################################################################

def parse_from_file():
    g = Graph()
    # ↓↓↓ START TO CODE BELOW ↓↓↓


    return g

####################################################################################
##  3.2 Parse the Web resource at 'uri' in the format 'application/rdf+xml' (xml) ##
####################################################################################

def parse_from_web():
    uri = 'https://data.nobelprize.org/store/6/metadata/1930?recursive=nobelprize&format=application/rdf+xml'
    g = Graph()
    # ↓↓↓ START TO CODE BELOW ↓↓↓

    return g





if __name__ == '__main__':
    #print(parse_from_file().serialize(format='turtle'))
    print(parse_from_web().serialize(format='turtle'))