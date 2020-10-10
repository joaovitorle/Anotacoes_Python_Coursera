num = [3,5,8]
accum = []
for w in num:
    x = w**2
    accum.append(x)
print (accum)

s = input('Enter some text:')
ac = ''
for c in s: 
    ac = ac + c + '-' + c + '-'
print (ac)