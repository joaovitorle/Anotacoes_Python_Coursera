#1
lista_fruta = ['banana','maça', 'pera', 'uva']
print (lista_fruta)


lista_fruta [0] = 'Chocolate'
lista_fruta [-1] = 'Coco'
print (lista_fruta)

#2
alist = ['a', 'b', 'c', 'd', 'f']

alist[1:4] = ['x', 'y']

print (alist)

#3 I need to make a new variable to change a string,using concanated,just a list could be changed !
greeting = 'Hello World!'
new_greeting = 'J' + greeting[1:]
print (new_greeting)
print (greeting)