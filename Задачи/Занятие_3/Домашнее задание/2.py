m=''
for i in range(1,11):
    for j in range(1,11):
      m+=str(j*i)+' '*(3-len(str(j*i)))
    print(m)
    m=''
