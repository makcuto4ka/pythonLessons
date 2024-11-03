tree=[None,None,None]
tree[1]=input('Введите значение кореня: ')
def new_child(tree,navi):
    copy_tree=[tree]
    last_copy=copy_tree[0]
    for i in navi:
        print(copy_tree,1.1,last_copy)
        if i=='L':
            copy_tree.append(last_copy[0])
            last_copy=last_copy[0]
        else:
            copy_tree.append(last_copy[2])
            last_copy=last_copy[2]
        print(copy_tree,1.2,last_copy)
    copy_tree[-1]=[None,input('Введите значение листочка: '),None]
    print(copy_tree,2)
    for i in navi[::-1]:
        if i=='L':
            if type(copy_tree[-2])==list:
                copy_tree[-2][0]=copy_tree[-1]
            else:
                copy_tree[0][0]=copy_tree[-1]
        else:
            if type(copy_tree[-2])==list:
                copy_tree[-2][2]=copy_tree[-1]
            else:
                copy_tree[2]=copy_tree[-1]
        copy_tree=copy_tree[:-1]
        print(copy_tree,3)
    return copy_tree[0]
navi=input('Введите маршрут к нужному листочку:')   
while navi!='':
    tree=new_child(tree,navi)
    print(tree,777)
    navi=input('Введите маршрут к нужному листочку:') 
        
        
        