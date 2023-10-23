#Dictionaries: Key-value pairs, unordered, Mutable.
mydict = {"name" : "akhi" , "age" : 32}
print(mydict)
 
dict2 = dict(name = "akhi" , age = 32 , city = "navimumbai" )
print(dict2)

value = mydict["age"]
print(value)

mydict["email"] = "akhi.c@ui.com"#to add key:value in dictionary
print(mydict)

del mydict["name"]
print(mydict)

mydict.pop("age")
print(mydict)

mydict.popitem()
print(mydict)



if "name" in dict2:
    print(dict2["name"])

try:
    print(dict2["lastname"])
except:
    print("error")

for key in dict2.keys():#or only --> for key in dict2:
    print(key)

for value in dict2.values():#or only --> for value in dict2:
    print(value)

#do that in combined manner.

for key, value in dict2.items():#include dict2.items
    print(key, value)

dict2_copy = dict2
print(dict2_copy)

dict2_copy["email"] = "akhi@xyz.com"

print(dict2_copy)
print(dict2)# here the original dict gets changed with the new assigned dict

dict3 = dict2.copy()# here the original dict doesnt get affected. important to note.
print(dict3)

#merge the dicts. Update method.
import random

# Create a dictionary with random keys and values
dictionary1 = {f'key{i}': random.randint(1, 100) for i in range(5)}

# Create another dictionary with different random keys and values
dictionary2 = {f'item{i}': random.choice(['apple', 'banana', 'cherry', 'date']) for i in range(3)}

# Display the dictionaries
print("Dictionary 1:")
print(dictionary1)

print("Dictionary 2:")
print(dictionary2)

dictionary1.update(dictionary2)
print("\n", dictionary1)

#adding tuples in dicts but not possible with Lists-- cuz lists are immutable.
tuple1 =  (1,2)
dictss = {tuple1: 5}

print(dictss)



















