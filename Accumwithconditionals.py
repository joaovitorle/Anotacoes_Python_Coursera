frase = 'Meu nome é João Vitor'

accum= 0 

for c in frase: 
    if c != ' ':
        accum = accum +1 
print (accum)


s = "what if we went to the zoo"
x = 0
for i in s:
    if i in ['a', 'e', 'i', 'o', 'u']:
        x += 1
print(x)

nums = [9, 3, 8, 11, 5, 29, 2]
best_num = 0
for n in nums:
    if n > best_num:
        best_num = n
print(best_num)

nums = [9, 3, 8, 11, 5, 29, 2]
best_num = nums[0]
for n in nums:
    if n > best_num:
        best_num = n
print(best_num)

sentence = "python is a high level general purpose programming language that can be applied to many different classes of problems."
num_a_or_e = 0
for n in sentence.split(): 
    if ("a" in n) or ("e" in n):
        num_a_or_e+=1
print(num_a_or_e)



