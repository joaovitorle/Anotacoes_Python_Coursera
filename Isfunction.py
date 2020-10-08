#1

a= "banana"
b= "banana"
print (a is b) 

#2

a= [81,82,83]
b= [81,82,83]

print(a is b) #checks whether a and b are aliases for exactly the same object 
print(a == b)
print(id(a))
print(id(b))

#3

a = [81,82,83]
b = a[:]

print (a == b)
print (a is b)

b[0] = 5
print(a)
print(b)