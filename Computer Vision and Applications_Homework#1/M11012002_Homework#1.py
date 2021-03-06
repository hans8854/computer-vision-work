# -*- coding: utf-8 -*-
"""Untitled

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1smg8e3aJKnZeSsHoVQls61v3i0CMCm5e
"""

from numpy.lib.function_base import append
import numpy as np
from google.colab.patches import cv2_imshow
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import cv2 # 導入OpenCV函式庫
from google.colab import files


#1)read the given image
img1 = cv2.imread('1.jpg')
img2 = cv2.imread('2.jpg')
img3 = cv2.imread('3.jpg')
#2) Read trajectory.xyz
x,y,z = np.loadtxt('trajectory.xyz').T
num = len(x)
x_reshape = x.reshape(num,1)
y_reshape = y.reshape(num,1)
z_reshape = z.reshape(num,1)
world4 = np.ones((num,1) ,dtype=float) 
xyz = np.hstack((x_reshape,y_reshape,z_reshape,world4))
# print(xyz)
# print(num)
# 建立 3D 圖形
# fig = plt.figure()
# ax = fig.gca(projection='3d')
# for i in range(num):
#     ax.scatter(xyz[i,0], xyz[i,1], xyz[i,2],s=20, c='red',marker='.')



# -----------------------1.txt-------------------------------------------------
camera1K = np.array([[1302.772461, 0.000000, 780.000000],
            [0.000000, 1302.772461, 473.000000],
            [0.000000, 0.000000, 1.000000]])

camera1RT = np.array([[0.593688,0.802865,-0.054238,-17.286613],
            [0.583624, -0.476011, -0.657875 ,8.647337],
            [-0.554003, 0.358918, -0.751171 ,37.070713]])

# -----------------------2.txt-------------------------------------------------
camera2K = np.array([[1302.772461, 0.000000, 780.000000],
            [0.000000, 1302.772461, 473.000000],
            [0.000000, 0.000000, 1.000000]])
camera2RT =np.array([[0.989605, -0.136529, 0.045175, 0.677726],
            [-0.000234, -0.315661, -0.948874, 6.772503],
            [0.143808, 0.938999, -0.312410, 23.802778]])

# -----------------------3.txt-------------------------------------------------
camera3K = np.array([[2893.163818, 0.000000, 780.000000],
            [0.000000, 2893.163574, 473.000000],
            [0.000000, 0.000000, 1.000000]])
camera3RT =np.array([[0.989605, -0.136529, 0.045175, 0.677726],
            [-0.000234, -0.315661, -0.948874, 6.772503],
            [0.143808, 0.938999, -0.312410, 23.802778]])


# Do matrix multiplication (ex. x=K[R|T]X)
def matrix_multiplication(pictureK,pictureRT,point):
  camera = np.dot(pictureK,pictureRT)
  camera = np.dot(camera,point)
  img_pixl = camera/camera[2]
  return img_pixl[:2]

#--------------------change 3D points to 2D pixl 1.jpg-----------------
camera1 = []
for i in range(num):
  camera1.append(matrix_multiplication(camera1K,camera1RT,xyz[i]))
camera1 = np.array(camera1)
camera1 = np.trunc(camera1)
camera1 = camera1.astype(np.int16)

#4)Draw projected 2D points on images1.
for i in range(num):
  cv2.circle(img1,(camera1[i,0],camera1[i,1]), 3, (0, 0, 255), -1)
cv2_imshow(img1)
# 5) Save those images in Step-4.
cv2.imwrite('image1.jpg', img1)
files.download("image1.jpg")

#--------------------change 3D points to 2D pixl 2.jpg-----------------
camera2 = []
for i in range(num):
  camera2.append(matrix_multiplication(camera2K,camera2RT,xyz[i]))
camera2 = np.array(camera2)
camera2 = np.trunc(camera2)
camera2 = camera2.astype(np.int16)

#4)Draw projected 2D points on images2.
for i in range(num):
  cv2.circle(img2,(camera2[i,0],camera2[i,1]), 3, (0, 0, 255), -1)
cv2_imshow(img2)
# 5) Save those images in Step-4.
cv2.imwrite('image2.jpg', img2)
files.download("image2.jpg")

#--------------------change 3D points to 2D pixl 3.jpg-----------------
camera3 = []
for i in range(num):
  camera3.append(matrix_multiplication(camera3K,camera3RT,xyz[i]))
camera3 = np.array(camera3)
camera3 = np.trunc(camera3)
camera3 = camera3.astype(np.int16)

#4)Draw projected 2D points on images3.
for i in range(num):
  cv2.circle(img3,(camera3[i,0],camera3[i,1]), 3, (0, 0, 255), -1)
cv2_imshow(img3)
# 5) Save those images in Step-4.
cv2.imwrite('image3.jpg', img3)
files.download("image3.jpg")