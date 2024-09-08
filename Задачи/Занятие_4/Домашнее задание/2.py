s = 'аоаоиммдтм(поннннпрппоннннннннннннмлтмлтмлтмтмлххз)тм'
for i in range(len(s)):
    if s[i]=='(':
        a=i
    elif s[i]==')':
        b=i
print(s[a+1:b])
