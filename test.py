# from matplotlib import pyplot as plt
# fig = plt.figure()
# ax = fig.add_subplot()
# fig.suptitle('Дерево', fontsize=14, fontweight='bold')
# ax.axis([0, 10, 0, 10])
# ax.annotate('annotate', xy=(5, 10), xytext=(4, 10),arrowprops=dict(facecolor='black', shrink=0.05))
# plt.show()
a=[[[[None, '3', [None, '3', None]], '3', None], '1', [None, '4', None]], '0', [[None, '5', None], '2', [None, '6', None]]]
# def count_list(l):
#     count = 0
#     for e in l:
#         if isinstance(e, list):
#             count = count + 1 + count_list(e)
#     return count
# print(count_list(a))

 
# def max_depth(tree):
#     if type(tree) == list:
#         return 1 + max(max_depth(i) for i in tree) 
#     else:
#         return 0
 
# print (max_depth(a))
# from matplotlib import pyplot as plt
# tree=[[[[None, '3', [None, '3', None]], '3', None], '1', [None, '4', None]], '0', [[None, '5', None], '2', [None, '6', None]]]
# def max_depth(tree):
#     if type(tree) == list:
#         return 1 + max(max_depth(i) for i in tree) 
#     else:
#         return 0
    

# k=max_depth(tree)    
# fig = plt.figure()
# ax = fig.add_subplot()
# fig.suptitle('Дерево', fontsize=14, fontweight='bold')
# ax.axis([0, k*10, 0, k*3])
# ax.text(k*3//2-2, k*10-1, tree[1])
# #ax.annotate('', xy=(1, 1), xytext=(4, 10),arrowprops=dict(facecolor='black', shrink=0.05))
# plt.show()
from PIL import Image, ImageDraw, ImageFont
tree=[[[[None, '3', [None, '3', None]], '3', None], '1', [None, '4', None]], 'fhvnvnv', [[None, '5', None], '2', [None, '6', None]]]
def max_depth(tree):
    if type(tree) == list:
        return 1 + max(max_depth(i) for i in tree) 
    else:
        return 0
    

k=max_depth(tree)
h=k*100
w=k*100
img = Image.new('RGB', [h, w], color='white')
draw = ImageDraw.Draw(img)
size=20
font = ImageFont.load_default(size)

draw.text((h//2-len(tree[1])*size/4, 0), tree[1], 'black',font=font) 
img1 = ImageDraw.Draw(img)  
img1.line([(h//2, 20),(w//4,100)], fill ='black', width = 5)
img.show()