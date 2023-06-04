list = [34,12,8,5,"Hello World",34]
for x in list:
    print(x)
print(list[4]) #this will print 'Hello World'
# adding new value in the list
print("After adding 89 in the list: ")
list.append(89)
print(list)
# inserting new value at index 3
list.insert(3,67)
print("After inserting 67 at index 3, the list is :")
print(list)

# nested list
list2 = [32, -36, 5 ,9, [-12,20,90]]
print(list2[1])
print(list2[4]) # this will print [-12,20,90]
print(list2[4][1]) # it will print the second value of [-12,20,90], is 20
# lets concataned two list
list = list + list2
# after concatenting two list
print("After concatanating two list :")
print(list)
# using remove function
list.remove("Hello World")
print("After removing Hello World, list is :")
print(list)
# Pop function
list.pop()
# remove from a specific index
list.remove(list[2])
print(list)
# lets sort the list
list.sort()
print("After sorting the list :")
print(list)
#knowing index of the value
print(list.index(89))
# counting the number of a balue in a list
list.count(34)
print("Counted 34 :" )
print(list.count(34))


