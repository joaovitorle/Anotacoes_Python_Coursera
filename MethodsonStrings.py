#1 Upper and Lower

ss = 'Hello, World'
print(ss.upper())

tt = ss.lower()
print(tt)
print(ss)

#2 Count, Strip, Replace

ss = '    Hello,World    '

els = ss.count('l')
print(els)

print('***'+ss.strip()+'***') #Strip tira os espaços desnecessários do começo e do final

news = ss.replace ('o', '***')
print(news)


