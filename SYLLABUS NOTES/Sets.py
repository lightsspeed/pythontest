#Sets : unordered, mutable , no duplicates

myset = {1,2,3,45,1,2}
print(myset)

myset = set([1,2,3])
print(myset)

myset = set("Hello")# unordered
print(myset)

myset1 = {} #Dict type
print(type(myset))
print(type(myset1))

#empty set can be like
myset_empty = set()#empty
print(type(myset_empty))

#add/remove elements in sets
myset_empty.add(1)
myset_empty.add(2)
myset_empty.add(3)

myset_empty.remove(3)
myset_empty.discard(2)
print(myset_empty.pop())
print(myset_empty.clear())

for x in myset:
    print(x)

integer_set = {1, 2, 3, 4, 5}
string_set = {'apple', 'banana', 'cherry', 'date'}
mixed_set = {1, 'apple', 2.5, (3, 4)}

odds = {1,3,5,7,9}
evens = {0,2,4,6,8}
primes = {2,3,5,7}

#union of sets
u = integer_set.union(string_set)
print(u)

#intersection of sets
i = odds.intersection(evens)# output will be empty set. cuz there is no similar values
print(i)
# output will be empty set. cuz there is no similar values between the sets

i1 = odds.intersection(primes)
print(i1)

i2 = evens.intersection(primes)
print(i2)


setA = {1,2,3,5,6,8,64,9,81}
setB = {1,2,3,4,6,3,2,8,9,20}

#finding the diff betn two sets
diff = setA.difference(setB)#prints unique elemnts from sets defined earlier i.e setA
diff1 = setA.symmetric_difference(setB)#prints unique elements from both sets
print("diffrence", diff)
print("diffrence", diff1)

setA.update(setB)
print(setA)



















