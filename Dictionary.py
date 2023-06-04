dictionaryTest = {'name' : "Mahir", "roll" : 1316, "year" : "2nd"}
print(dictionaryTest)
#excess the roll
print(dictionaryTest['roll'])
print(dictionaryTest['year'])

# to update any key
dictionaryTest['name'] = "Faisal"
dictionaryTest['year'] = '3rd'
print("Print the values only:")
for x in dictionaryTest:
    print(dictionaryTest[x]) # this will print only the vslues

# now print the values with their keys
print("Print the values with their keys :")
for x,y in dictionaryTest.items():
    print(x , y)

# to create a copy of whole dictionary
x = dictionaryTest.copy()
print("Copying the dictionary to x :")
print(x)

# to delete any items from dictionary

del dictionaryTest['year']
print("After deleting the item year, the dictionary is :")
for x,y in dictionaryTest.items():
    print(x,y)

# to clear whole dictionary

dictionaryTest.clear()
print("After clearing whole dictionary :")
print(dictionaryTest)





