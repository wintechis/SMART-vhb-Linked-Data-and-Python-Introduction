##########################
## Algebra.py
##########################

from _8_algebra import ResultSet, is_compatible, n3


g = rdflib.ConjunctiveGraph().parse('https://data.nobelprize.org/store/6/metadata/3981?recursive=nobelprize&format=text/turtle')
#Retrieve data: The Nobel Prize in Physics 2020
g.parse('https://data.nobelprize.org/store/6/metadata/3183?recursive=nobelprize&format=text/turtle')
#Retrieve data: The Nobel Prize in Physics 2019
g.parse('https://data.nobelprize.org/store/6/metadata/2547?recursive=nobelprize&format=text/turtle')

##########################
## Exercise 8.1
##########################
def join(𝛀_l: ResultSet, 𝛀_r: ResultSet) -> ResultSet:
    # TODO return the ResultSet after a JOIN operation between 𝛀_l and 𝛀_r.
    # A ResultList is a Python list with solution mappings (Python dictionaries) as items.
    # After a JOIN operation only solution mappings remain that fulfill the conditions of both ResultSets.
    # You may use the is_compatible function.
    𝛀_l, 𝛀_r = list(𝛀_l), list(𝛀_r) # convert iterators to lists
    𝛀 = []
    # ↓↓↓ START TO CODE BELOW ↓↓↓

    return iter(𝛀)


##########################
## Exercise 8.2
##########################
def union(𝛀_l: ResultSet, 𝛀_r: ResultSet) -> ResultSet:
     # TODO return the ResultSet after a UNION operation between 𝛀_l and 𝛀_r.
     # ↓↓↓ START TO CODE BELOW ↓↓↓
     pass