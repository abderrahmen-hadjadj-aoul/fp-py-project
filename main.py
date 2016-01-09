################################################################################
# 08/01/2016
#
# Abderrahmen Hadjadj-Aoul
# Gabriel Greslin
#
# SD314: Miniproject - FP in Python
#
################################################################################

from functools import reduce

################################################################################
# 1.
# write a function loop such that loop(p, f, x) returns
# x when p(x) is True and
# loop(p, f, x) returns loop(p, f, f(x)) otherwise.
loop = lambda p, f, x: x if p(x) else loop(p, f, f(x))

# Tests
print("# loop(p, f, x) - TESTS")
print("#######################\n")

# Test 1
print("# loop(p, f, x) - Test 1")
p = lambda x: not x < 5
def f(x):
    print("x:"+str(x))
    return x+1
y = loop(p, f, 1)
print("*y:"+str(y))
print("")

################################################################################
# 2.
# write a function exists such that exists(p, l) returns
# True when there is an element of list l such that p(l) is true.
exists = lambda p, l: p(l[0]) or exists(p, l[1:]) if len(l) > 0 else False

# Tests
print("# exists(p, l) - TESTS")
print("######################\n")

# Test 1
print("# exists(p, l) - Test 1")
l = [1,2,3,4,5]
p = lambda x: x == 2
r = exists(p, l)
print("l")
print(l)
print("result:"+str(r))
print("expected:True")
if r:
    print("test:passed")
else:
    print("test:ERROR")
print("")

# Test 2
print("# exists(p, l) - Test 2")
l = [1,3,4,5]
p = lambda x: x == 2
r = exists(p, l)
print("l")
print(l)
print("r:"+str(r))
if not r:
    print("test:passed")
else:
    print("test:ERROR")
print("")

# Test 3
print("# exists(p, l) - Test 3")
l = [1,3,4,5]
p = lambda x: x > 5
r = exists(p, l)
print("l")
print(l)
print("r:"+str(r))
if not r:
    print("test:passed")
else:
    print("test:ERROR")
print("")

################################################################################
# 3.
# write a function find such that find(p, l) returns
# x if x is the first element of l such that p(x) is True.
# When no such element exists, simply return None.
find  = lambda p, l: ( l[0] if p(l[0]) else find(p, l[1:]) ) if len(l) > 0 else None

# Tests
print("# find(p, l) - TESTS")
print("#####################\n")

# Test 1
print("# find(p, l) - Test 1")
l = [1,2,3,4,5]
p = lambda x: x == 3
r = find(p, l)
print("l")
print(l)
print("result:"+str(r))
print("expected:3")
if r == 3:
    print("test:passed")
else:
    print("test:ERROR")
print("")

# Test 2
print("# find(p, l) - Test 1")
l = [1,2,3,4,5, 7, 8, 9]
p = lambda x: x > 5
r = find(p, l)
print("l")
print(l)
print("result:"+str(r))
print("expected:7")
if r == 7:
    print("test:passed")
else:
    print("test:ERROR")
print("")

# Test 2
print("# find(p, l) - Test 1")
l = [1,2,3,4,5, 7, 8, 9]
p = lambda x: x == 6
r = find(p, l)
print("l")
print(l)
print("result:"+str(r))
print("expected:None")
if r == None:
    print("test:passed")
else:
    print("test:ERROR")
print("")

################################################################################
# 4.
# we now consider that the possible states of the game we are interested in are represented by a set E. We have a
# relation R such that xRy if and only if the state y is reachable in one step from x in the game. As a relation is a
# subset of E x E, we will consider that R will be implemented in Python by a function rel that takes an element
# and returns a list of elements of the same type such that for all y in rel(x) xRy holds.
# We will consider here a simple relation on integers: xNy holds if and only if the difference between x and y is at
# most 2. This relation will be used to illustrate the concepts in the following. You can also use this relation for
# testing purposes for instance.
#
# Implement N by a near function. For instance near(2) should return the list [0, 1, 2, 3, 4].

near = lambda x: [x-2, x-1, x, x+1, x+2]
# Probalement pas la reponse attendue :/ !

# Test
print("\n# near(x) - TESTS")
print("#################\n")

# Test 1
print("# near(x) - Test 1")

l = near(2)
print(l)

################################################################################
# 5.
# a relation R allows to compute the states reachable from a state in one step. We want now to be able to compute
# the states reachable from a list of states in one step.
# Write a function flat_map such that flat_map(rel, l) where l is a list of possible states returns the list of all
# possible states reachable in one step from the states of l. For instance, flat_map(near, [2, 3, 4]) should return
# [0, 1, 2, 3, 4, 1, 2, 3, 4, 5, 2, 3, 4, 5, 6].

flat_map = lambda rel, l: reduce(lambda x, y: x+rel(y), l, [])

# Test
print("\n# flat_map(x) - TESTS")
print("#####################\n")

# Test 1
print("# flat_map(x) - Test 1")
fm = flat_map(near, [2])
print(fm)
print("")

# Test 2
print("# flat_map(x) - Test 2")
fm = flat_map(near, [2, 3, 4])
print(fm)
print("")

################################################################################
# 6.
# write a function iter(rel, n) that iterates the relation rel n times. What should this function return?

iter = lambda rel, n: lambda z: loop(lambda x: x[0] > n, lambda x: [x[0]+1, flat_map(rel, x[1])], [1, [z]])[1]
# Retourne une *fonction* qui calculs les etats accessibles en n tours

# Tests

print("\n# iter(rel, n) - TESTS")
print("#######################\n")

print("# iter(rel, n) - Test 1")
i = iter(near, 1)
r = i(2)
print(r)
print("")

print("# iter(rel, n) - Test 2")
i = iter(near, 2)
r = i(2)
print(r)
print("")

print("# iter(rel, n) - Test 3")
i = iter(near, 3)
r = i(2)
print(r)
print("")

################################################################################
# 7. the next step in solving the game is to compute the transitive closure of R: you will obtain all the possible states
# from a given state. Of course, you will not compute the transitive closure of R as it may be infinite: we want here
# to iterate R starting from a given state and stop when we have a reachable state that verifies a given property (for
# instance to be the winning state. . . ).
