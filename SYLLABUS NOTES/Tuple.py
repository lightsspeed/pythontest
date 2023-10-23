#Tuples : ordered, immutable, allows duplicates elements
#-- brackets are not important but use comma after the elemnt
import timeit
tuple = ("akhi" , 32 , "Navimumbai")


print(tuple)

#item = tuple[0]
#print(item)

#tuple[0] = 'choure'
# This is not possible in Tuple , cuz it is immutable.

#for i in tuple:
   # print(i)

tuple1 = ("1","1","2","3","4","5","6","7")#allows duplicate elemnts

print(len(tuple1))

print(tuple1.count('1'))
print(tuple1.index("2"))

tuple1_list = list(tuple1)
print(tuple1_list)

#indexing of slicing is same as Lists

name , age , city = tuple#values of tuple must match the unpacked elemnts

print(name)
print(age)
print(city)

print(timeit.timeit(stmt="[0,1,2,3,4,5]", number = 1000000))#Lists
print(timeit.timeit(stmt="(0,1,2,3,4,5)", number = 1000000))#Tuple
#Tuples are faster to execute than Lists---> check output.