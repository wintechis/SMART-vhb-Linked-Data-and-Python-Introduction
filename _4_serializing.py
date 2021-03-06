##############################################################################################
## Course   : Linked Data and Python: Introduction                                          ##
## Section  : Serializing                                                                   ##
## Authors  : Christian Fleiner, Andreas Harth                                              ##
## See more : https://github.com/wintechis/SMART-vhb-Linked-Data-and-Python-Introduction    ##
##                                                                                          ##
## Learning Goals:                                                                          ##
## - Serialize to string or to file                                                         ##
## - Serialize in multiple formats                                                          ##
##############################################################################################

##################################################
## Import graph from library
from rdflib import Graph


#################################################
## Parse local file
g = Graph().parse(source='example.ttl')


################################################
# Print serialized graph to terminal
# print('============ Graph as String ============')
# print(g.serialize(format='turtle'))

# ###############################################
# # Write to file
# g.serialize(destination='serialized.ttl', format='turtle')

# ###############################################
# Serialize to string and write to file
# data = g.serialize(format='turtle')
# with open('serialized.ttl', 'w') as f:
#    f.write(data)


#############################################################
# See formats.py/.txt for available Serializers and Parsers #
#############################################################