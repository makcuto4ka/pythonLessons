import json
from matplotlib import pyplot as plt


def help():
    print('Команды:')
    print('  new - создание нового листочка')
    print('  del - удаление листочка или ветки')
    print('  save - сохранение дерева в файл')
    print('  open - открытие дерева из файла')
    print('Для завершения программы нажмите Enter')

def save_tree(tree):
    name_file=input('Введите название файла: ')
    with open(f'{name_file}.txt', 'w') as fw:
        return json.dump(tree, fw)

def open_tree():
    name_file=input('Введите название файла: ')
    with open(f'{name_file}.txt', 'r') as fr:
        return  json.load(fr)
    
def new_child(tree,navi):
    copy_tree=[tree]
    last_copy=copy_tree[0]
    try:
        if navi=='':
            copy_tree[0][1]=input('Введите значение кореня: ')
            return copy_tree[0]
        for i in navi:
            if i=='L':
                copy_tree.append(last_copy[0])
                last_copy=last_copy[0]
            else:
                copy_tree.append(last_copy[2])
                last_copy=last_copy[2]
        copy_tree[-1]=[None,input('Введите значение листочка: '),None]
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
    except TypeError:
        print('Ошибка! Неверный путь к листочку.')
    return copy_tree[0]

def delete_child(tree,navi):
    copy_tree=[tree]
    last_copy=copy_tree[0]
    try:
        for i in navi:
            if i=='L':
                copy_tree.append(last_copy[0])
                last_copy=last_copy[0]
            else:
                copy_tree.append(last_copy[2])
                last_copy=last_copy[2]
        copy_tree[-1]=[None,None,None]
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
    except TypeError:
        print('Ошибка! Неверный путь к листочку.')
    return copy_tree[0]

def max_depth(tree):
    if type(tree) == list:
        return 1 + max(max_depth(i) for i in tree) 
    else:
        return 0
    
def show_tree(tree):
    k=max_depth(tree)    
    fig = plt.figure()
    ax = fig.add_subplot()
    fig.suptitle('Дерево', fontsize=14, fontweight='bold')
    ax.axis([0, k*3, 0, k*10])
    ax.annotate('annotate', xy=(5, 10), xytext=(4, 10),arrowprops=dict(facecolor='black', shrink=0.05))
    plt.show()
tree=[None,None,None]


action=input('Введите действие (для помощи введите - help): ') 
while action!='':
    if action=='new':
        navi=input('Введите путь к нужному листочку (для изменения корня нажмите Enter): ').upper() 
        tree=new_child(tree,navi)
    elif action=='del':
        navi=input('Введите путь к нужному листочку: ') .upper() 
        tree=delete_child(tree,navi)
    elif action=='save': 
        save_tree(tree)
    elif action=='open':
        open_tree()
    elif action=='help':
        help()
    else:
        print('Ошибка! Команды не существует.')
    print(tree)
    action=input('Введите действие (для помощи введите - help): ') 
    
        
        
        