#set

a = {1,2,3,4,3,3,4,5,5,5,6};

print(a);
print(len(a));

a.add(1);
print(a);

a.discard(6); #remove an element
print(a);

b = a.copy(); #copy ref.
print(b);

a.clear(); #empty set
print(a);

#Operation on set:

# 1. union:

set1 = {1,5,7,8};
set2={2,1,5,9,10};

print(set1|set2);
print(set1.union(set2));

#intersection:

print(set1&set2)
print(set1.intersection(set2));

#differecen

print(set1-set2)
print(set2-set1)

#symmtric diff = union - intersection

