#working on frozenset 

x=("a","b","c","d","e","f")

fset=frozenset(x)

print(fset)

l=frozenset([1,2,3,4])

m=frozenset(["a","e","i","o","u"]) 

y=frozenset(["a","b",1,2,"c","f",4])

z=frozenset([2,"a","c",3,4,1,6,"d","e"])

print(y.union(z))

print(y.difference(z))

print(y.symmetric_difference(z))

print(y.isdisjoint(z))

print(l.issubset(z))

print(y.issuperset(l))

print(z.issuperset(l))

print(z.isdisjoint(l))

print(m.issuperset(fset))

print(y.intersection(z))
