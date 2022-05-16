##############################################################################################
## Course   : Linked Data and Python: Introduction                                          ##
## Section  : Namespaces - Excercise                                                        ##
## Authors  : Christian Fleiner, Andreas Harth                                              ##
## See more : https://github.com/wintechis/SMART-vhb-Linked-Data-and-Python-Introduction    ##
##                                                                                          ##
## Exercises:                                                                               ##
## - 2.1 Create Literal of a specific type                                                  ##
## - 2.2 Unbind preloaded namespaces (See namespaceManager class)                           ##
##############################################################################################

from rdflib import Literal, XSD, Graph

##################################################################
##  2.1 Return date_time as Literal of type dateTime            ##
##################################################################

def create_datetime() -> Literal:
    date_time = '2022-05-01T18:25:43+1'
    # ↓↓↓ START TO CODE BELOW ↓↓↓
    return 


##################################################################
##  2.2 Unbind preloaded namespaces and return graph            ##
##################################################################
def reset_namespaces() -> Graph:
    g = Graph()
    # ↓↓↓ START TO CODE BELOW ↓↓↓


    return g

if __name__ == '__main__':
    print(create_datetime())
    #print([ns for ns in reset_namespaces().namespaces()])
    #python -m unittest -v  tests.E2