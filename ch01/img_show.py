# coding: utf-8
import matplotlib.pyplot as plt
from matplotlib.image import imread

import os
cwd = os.getcwd()

img = imread('./dataset/cactus.png') # 이미지 읽어오기
plt.imshow(img)

plt.show()
