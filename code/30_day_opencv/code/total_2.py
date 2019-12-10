# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  SanJin
@Version        :  
------------------------------------
@File           :  total_2.py
@Description    :  
@CreateTime     :  2019/12/5 15:55
------------------------------------
@ModifyTime     :  
"""
import cv2 as cv
import numpy as np


def create_image():
    # # 建立一个400高400宽3维的元素全部为0的数组
    # img = np.zeros([400, 400, 3], np.uint8)
    # # RGB分别是(0=B,1=G,2=R)
    # # 默认为全部，如果加数字 就可以认为是哪行哪列
    # # img[:, :, 0] = np.ones([400, 400]) * 255
    # img[:, :, 2] = np.ones([400, 400]) * 255
    # cv.imshow("new image", img)
    img = np.ones([400, 400, 1], np.uint8)
    # 设置三维数组内每个元素都是1，在乘以颜色值，才会有颜色，
    # img[:, :, 0] = np.ones([400, 400]) * 127
    # 等同于  img = img * 0
    img = img * 127
    cv.imshow("new image", img)



print("------------------Hello Python------------------------")
src = cv.imread("E:/Disk/H/github/Opencv3.x/code/30_day_opencv/images/lining.png")  # imread，是cv2库中读取图片的函数（）中填写所读去图片的位置，最好写绝对位置
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)  # 设置生成的窗口的名字和自动窗口调整大小
cv.imshow("input image", src)  # imshow,用于显示读取到的图片，并命名读出来的窗口名字
# 增加程序运行开始时间
t1 = cv.getTickCount()
# 运行程序
create_image()
# 记录程序运行结束时间
t2 = cv.getTickCount()
# 计算时间差,单位是ms
time = (t2-t1)/cv.getTickFrequency()
print("time is : %s ms" %((time)*1000))
gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)  # 生成灰度图
cv.imwrite("D:/TOFU/github_new/Python/Numpy/images/lining_1.png", gray)
# video_demo()  # 调用video 函数 使之显示
cv.waitKey(0)

cv.destroyAllWindows()
