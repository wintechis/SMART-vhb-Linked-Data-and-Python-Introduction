
from rdflib.parser import Parser
from rdflib.serializer import Serializer
from rdflib import plugin


parsers = ['=== Parsers ===']
serializers = ['=== Serializers ===']

for k in plugin._plugins.keys():
    # k[0]: keyword, k[1]: class
    # iterate over all registerd plugins and save  
    # kezwords of parsers and serializers
    if k[1] == Parser : parsers.append(k[0])
    elif k[1] == Serializer: serializers.append(k[0])


# write available formats to file 'formats.txt'
with open('formats.txt', 'w') as f:
    for p in parsers: f.write(p + '\n')
    f.write('\n\n')
    for s in serializers: f.write(s + '\n')
