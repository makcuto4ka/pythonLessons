# import os
# import re
# from PIL import Image
# s = [ f.path for f in os.scandir('C:/Users/User/Downloads/11') if f.is_dir() ]
# for i in s:
#     for j in [ f.path for f in os.scandir(i) if f.is_file() ]:
#         if re.fullmatch(r'.{0,}\d{3}.jpg', j):
#             img =Image.open(j)
#             img.save( f'C:/Users/User/ВУЗ/Математический анализ/111/{j[-7:]}')

#################################################################################################3


import queue
from spire.doc import *
from spire.doc.common import *

# Создайте объект документа
doc = Document()

# Загрузите файл Word
doc.LoadFromFile("C:/Users/User/ВУЗ/Математический анализ/лек.docx")

# Создайте объект очереди
nodes = queue.Queue()
nodes.put(doc)

# Создайте список
images = []

while nodes.qsize() > 0:
    node = nodes.get()

    # Переберите дочерние объекты в документе
    for i in range(node.ChildObjects.Count):
        child = node.ChildObjects.get_Item(i)

        # Определите, является ли дочерний объект изображением
        if child.DocumentObjectType == DocumentObjectType.Picture:
            picture = child if isinstance(child, DocPicture) else None
            dataBytes = picture.ImageBytes

            # Добавьте данные изображения в список 
            images.append(dataBytes)
         
        elif isinstance(child, ICompositeObject):
            nodes.put(child if isinstance(child, ICompositeObject) else None)

# Переберите изображения в списке
for i, item in enumerate(images):
    fileName = f'{'0'*(3-len(str(i)))+str(i)}.png'.format(i)
    with open("C:/Users/User/ВУЗ/Математический анализ/222/"+fileName, 'wb') as imageFile:
        # Запишите изображение в указанное место
        imageFile.write(item)