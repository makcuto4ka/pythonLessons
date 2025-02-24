# УСТАНОВКА cv2: pip install opencv-python

from random import randint
import cv2

k = int(input('Количество повторений: '))
t=int(input('Время на ответ: '))
m=[randint(1, 16) for x in range(k)]
for i in m:
    img = cv2.imread(f'image/{i}V.jpg')
    img = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
    cv2.imshow("Window", img)
    cv2.setWindowProperty("Window", cv2.WND_PROP_TOPMOST, 1)
    cv2.waitKey(t*1000)
    cv2.destroyAllWindows()
    

    img = cv2.imread(f'image/{i}.jpg')
    img = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
    cv2.imshow("Window", img)
    cv2.setWindowProperty("Window", cv2.WND_PROP_TOPMOST, 1)
    cv2.waitKey(t*1000)
    cv2.destroyAllWindows()