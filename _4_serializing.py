##########################################################
##                                                      ##
##                                                      ##
##                                                      ##
##########################################################



#import required classes from rdflib package
from rdflib import Graph



#################################################
## Add triples to graph

## parse local file
g = Graph().parse(source='D:/python_projects/ldpy_intro/example.ttl')


#################################################
## Serialize graph

## Serialize to terminal
print(g.serialize(format='turtle'))

## Serialize to directly to file
#g.serialize(destination='D:/python_projects/ldpy_intro/serialized.ttl', format='turtle')

## Serialize to string and write to file
#data = g.serialize(format='turtle')
#with open('D:/python_projects/ldpy_intro/serialized.ttl', 'w') as f:
#    f.write(data)
