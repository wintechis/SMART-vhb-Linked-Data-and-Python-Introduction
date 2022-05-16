##############################################################################################
## Course   : Linked Data and Python: Introduction                                          ##
## Section  : Terms - Exercise                                                              ##
## Authors  : Christian Fleiner, Andreas Harth                                              ##
## See more : https://github.com/wintechis/SMART-vhb-Linked-Data-and-Python-Introduction    ##
##                                                                                          ##
## Exercises:                                                                               ##
## - 1.1 Create Terms                                                                       ##
## - 1.2 Create Terms and add to Graph                                                      ##
##############################################################################################



import rdflib

###################################################################
##  1.1 Create the triple described in data1_1 with rdflib.terms ##
###################################################################
data1_1 = '''<http://example.org/Alice> <http://example.org/weight> 63.5 '''

def create_triple() -> tuple:
    # ↓↓↓ START TO CODE BELOW ↓↓↓



    return (alice, p_weight, o_weight)

##########################################################################
##  1.2 Create the triples described in data1_2 and add them to graph g ##
##########################################################################
data1_2 = '''
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX ex: <http://example.org/>

ex:Alice    foaf:knows (:Bob :Charlie :Daisy) .  
'''

def add_data_to_graph() -> rdflib.Graph:
    # create graph instance
    g = rdflib.Graph()

    #create terms
    # ↓↓↓ START TO CODE BELOW ↓↓↓









    #add triples to graph
    # ↓↓↓ START TO CODE BELOW ↓↓↓
   








 
    return g


if __name__ == '__main__':
    print(create_triple())
    #print(add_data_to_graph().serialize(format='turtle'))
    #python -m unittest -v  tests.E1
    
    
