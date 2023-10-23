#Lists : Ordered, Mutable, allows duplicatre elements

mylist = ["banana" , "cherry" , "apple"]
print(mylist)

mylist2 = [5, True, "apple" , "apple"]
print(mylist2)

item = mylist2[0]
print(item)
item = mylist2[-1]
print(item)

for i in mylist:
    print(i)
    

count = mylist.count("apple")
print(count)

if "banana" in mylist:# to check the element is in your list
    print("Y")
else:
    print("N")

print(len(mylist))

mylist.append("orange")
print(mylist)

mylist.insert(2, "watermelon")
print(mylist)

item1 = mylist.pop()
print(item1)


item1 = mylist.remove("cherry")
item1 = mylist.reverse()
item1 = mylist.sort()

num_list = [10 , -2 , 9 , 84 , -400]
num_list.sort()
print(num_list)

print(mylist)


mylist = [1,2,3,4,5,6,7]

a = mylist[1:6]#(startindex : stopindex-1 : stepindex)
a = mylist[::-1]
print(a)


list_org = ['banana', 'apple' , 'flower']

list_copy = list_org

list_copy.append("orange")

print(list_copy)
print(list_org)


#LIST COMPREHENSION

a= [1,2,3,4,5,6]
# syntax = [expression + for loop which states the list name]
print(a)
b= [i*i for i in a] 
print(b)






















