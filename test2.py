tree=[[[[None, '3', [None, '3', None]], '3', None], '1', [None, '4', None]], 'fhvnvnv', [[None, '5', None], '2', [None, '6', None]]]
def sort_tree(tree):
    new_tree=[]
    last_tree=tree
    while type(last_tree)==list:
        new_tree.append(list(filter(lambda x: type(x)!=list, last_tree)))
        last_tree=list(filter(lambda x: type(x)==list, last_tree))
        print(last_tree)
        arr=[]
        for i in last_tree:
            arr.append(i)
        last_tree=arr
        print(new_tree)
        t=input()
    return new_tree
print(sort_tree(tree))