addition_str = "2+5+10+20"
addition_str_splited= addition_str.split("+")
sum_val = 0
for c in addition_str_splited: 
    sum_val = sum_val + int(c)

print(sum_val) 

