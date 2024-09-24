m=''
for i in range(1,11):
    for j in range(1,11):
      m+=str(j*i)+' '*(3-len(str(j*i)))
    print(m)
    m=''




def f(n):
  for i in range(2,int(n**0.5)+1):
    if n%i==0:
      return 0
      break
  return 1
st = int(input("От "))
fn = int(input("До "))
for i in range(st,fn+1):
  if f(i)==1:
    print(i)
