# set
# are unique in nature.
# unordered collection of items.
# mutable in nature.

s1 = {1,1,2,3,4,5,6,6,6}
s2 = set()
#print(s1)
# add
# s1.add(12) # add single record
# print(s1)

#s1.update([13,14,15,16,17]) # add multiple record
#print(s1)

# remove
s1 = {1,2,3,4,5,6,7}
# print(s1)
# s1.remove(4)
# s1.discard(12)
# s1.clear()
# print(s1)

# read
s1 = {1,2,3,4,5,6,7}
for value in s1:
    # print(value)
    pass

# convert set => list then use index    
# print(list(s1)[0])

# copy
newSet = s1.copy()
# print(newSet)

# freeze
s2 = frozenset([1,2,3,4,5,6])

# print(s1)
# Operations
s1 = {1,2,3}
s2 = {1,2,4}
# Union.
print(s1.union(s2)) #{1, 2, 3, 4}
# Intersections.
print(s1.intersection(s2)) #{1, 2}
# Differences.
print(s2-s1) # {4}
# Symmetric difference.
print(s1 ^ s2) #{3, 4}