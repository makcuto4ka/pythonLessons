# tree= [[[10],3,[1]],7,[5]]
# t=tree
# s=0
# in_order_traversal = []
# while s!=1:
#     if type(t[0])==list and t[0]!=None:
#         t0=t
#         t=t[0]
#     elif type(t[0])!=list and t[0]!=None:
#         if len(t0[2])==3:
#             lc=t0[2][1]
#         else:
#             lc=t0[2][0]
#             s+=1
#         in_order_traversal +=[t[0],t0[1],lc,tree[1],tree[2][0]]
# print(in_order_traversal)


def f(n,p):
    if n>0:
        p*=n
        n-=1
        return f(n,p)
    else:
        return p
n=int(input())
print(f(n,1))