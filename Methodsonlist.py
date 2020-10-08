mylist = []
mylist.append(5) #append means add a new item to the end 
mylist.append(27)
mylist.append(3)
mylist.append(12)
print(mylist)

mylist.insert(1, 12) #insert, inserts the item wherever you tell it to, in this case we're going to tell it to insert at position number one, the number 12
print(mylist)
print(mylist.count(12))

print(mylist.index(3)) #index is a method, we will insert a value (3), and index will tell us the position where that value can be found
print(mylist.count(5))

mylist.reverse() #reverse is going to mirror the order of the items
print(mylist)

mylist.sort() #is a method is going to take the items in the list and just reorder them from smallest to biggest 
print(mylist)

mylist.remove(5) #Specifies a value that need to be removed from the list
print(mylist)

lastitem = mylist.pop() #Will get the last item 
print(lastitem)
print(mylist)