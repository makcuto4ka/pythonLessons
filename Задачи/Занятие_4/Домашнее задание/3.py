s = 'Абстракция муха авария слон книжка умный аллея'
s=s.split()
a=''
for i in s:
    if i[0].lower()=='а'and i[-1]=='я':
        a+= i + ' '
print(a)