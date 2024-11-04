import json
from PIL import Image, ImageDraw, ImageFont


def help():
    print('Команды:')
    print('  new - создание нового листочка')
    print('  del - удаление листочка или ветки')
    print('  save - сохранение дерева в файл')
    print('  open - открытие дерева из файла')
    print('  show - нарисовать дерево')
    print('  depth - узнать максимальную глубину дерева')
    print('Для завершения программы нажмите Enter')

def save_tree(tree):
    try:
        name_file=input('Введите название файла: ')
        with open(f'{name_file}.txt', 'w') as fw:
            return json.dump(tree, fw)
    except FileNotFoundError:
        print('Ошибка! Вы ввели недопустимый символ для имени файла.')
def open_tree():
    name_file=input('Введите название файла: ')
    try:
        with open(f'{name_file}.txt', 'r') as fr:
            return  json.load(fr)
    except FileNotFoundError:
        print('Ошибка! Файл не найден.')
    
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

def sort_tree(tree):
    new_tree=[]
    last_tree=tree
    k=0
    index=[0]
    while len(list(filter(lambda x: type(x)!=list and x!=None, last_tree)))>0:
        new_tree.append([None]*2**k)
        list_str=list(filter(lambda x: type(x)==str, last_tree))
        k3=0
        for i in index:
            new_tree[k][i]=(list_str[k3])
            k3+=1
        index=[]
        k2=0
        for i in last_tree:
            if type(i)==list:
                index.append(k2)
            elif type(i)==str:
                k2-=1
            k2+=1
        last_tree=list(filter(lambda x: type(x)==list, last_tree))
        arr=[]
        for i in last_tree:
            arr+=i
        last_tree=arr
        k+=1
    return new_tree

def show_tree(tree):  
    s_tree=sort_tree(tree)
    k=len(s_tree)
    h=k*50
    w=k*150
    img = Image.new('RGB', [w, h], color='white')
    draw = ImageDraw.Draw(img)
    size=20
    font = ImageFont.load_default(size)
    ki=0
    for i in range(len(s_tree)):
        kj=0
        kj2=0
        for j in range(len(s_tree[i])):
            if s_tree[i][j] != None:
                draw.text((w*(kj+1)//(len(s_tree[i])+1)-len(s_tree[i][j])*size//4, ki*50), s_tree[i][j], 'black',font=font) 
            if i+1!=len(s_tree):
                if s_tree[i][j] != None and s_tree[i+1][j] != None:
                    img1 = ImageDraw.Draw(img)  
                    img1.line([(w*(kj+1)//(len(s_tree[i])+1), ki*50+20),(w*(kj2+1)//(2**(ki+1)+1),ki*50+50)], fill ='black', width = 4)
                if s_tree[i][j] != None and s_tree[i+1][j+1] != None:
                    img1 = ImageDraw.Draw(img)  
                    img1.line([(w*(kj+1)//(len(s_tree[i])+1), ki*50+20),(w*(kj2+2)//(2**(ki+1)+1),ki*50+50)], fill ='black', width = 4)
            kj+=1
            kj2+=2
        ki+=1
    img.show()
    action=input('Для сохранения картинки дерева введите save: ').lower()
    if action=='save':
        name_file=input('Введите название файла: ')
        img.save(f'{name_file}.png') 
    

tree=[None,None,None]


action=input('Введите действие (для помощи введите - help): ').lower()
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
        tree=open_tree()
    elif action=='help':
        help()
    elif action=='show':
        show_tree(tree)
    elif action=='depth':
        print(max_depth(tree))
    else:
        print('Ошибка! Команды не существует.')
    print(tree)
    action=input('Введите действие (для помощи введите - help): ').lower()