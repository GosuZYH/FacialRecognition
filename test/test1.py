#!/usr/bin/python3
# _*_ coding: utf-8 _*_
#
# Copyright (C) 2023 - 2023 Gosu, Inc. All Rights Reserved 
#
# @Time    : 2023/12/28 14:53
# @Author  : GosuXX
# @File    : test1.py

import os

import cv2
import numpy as np

# 摄像头
# cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
# _, img = cap.read()
# img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imwrite("../dataset/img3.jpg", img)

# 加载人脸检测分类器
face_cascade = cv2.CascadeClassifier(f'{os.path.dirname(cv2.__file__)}\\data\\haarcascade_frontalface_default.xml')
'''
haarcascade_eye.xml：用于检测眼睛。
haarcascade_eye_tree_eyeglasses.xml：用于检测佩戴眼镜的眼睛。
haarcascade_frontalcatface.xml：用于检测正面的猫脸。
haarcascade_frontalcatface_extended.xml：用于检测正面的猫脸，这是一个扩展集。
haarcascade_frontalface_alt.xml：用于检测正面人脸的替代算法。
haarcascade_frontalface_alt2.xml：另一个用于检测正面人脸的替代算法。
haarcascade_frontalface_alt_tree.xml：基于树的方法，用于检测正面人脸。
haarcascade_frontalface_default.xml：用于检测正面人脸的默认算法。
haarcascade_fullbody.xml：用于检测全身站立姿势的人体。
haarcascade_lefteye_2splits.xml：使用2个分割特征来检测左眼。
haarcascade_license_plate_rus_16stages.xml：设计用于识别俄罗斯车牌。
'''
if face_cascade.empty():
    print("XML file not loaded")
    raise SystemExit
else:
    print("XML file loaded successfully")

# 创建LBPH人脸识别器
recognizer = cv2.face.LBPHFaceRecognizer_create()

# 读取图片
image = cv2.imread("../dataset/img1.jpg")
# 图像转换为灰度图：
grayImg = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# 检测图像中的所有面孔
faces = face_cascade.detectMultiScale(grayImg)

# 训练识别器
labels = [0]
recognizer.train(faces, np.array(labels))

# 为每个人脸绘制一个蓝色矩形
for x, y, width, height in faces:
    # 这里的color是 蓝 黄 红，与rgb相反，thickness设置宽度
    cv2.rectangle(image, (x, y), (x + width, y + height), color=(255, 0, 0), thickness=2)

# 最后，让我们保存新图像
cv2.imwrite("img1.jpg", image)
cv2.waitKey(0)

# 使用识别器进行人脸识别
# label, confidence = recognizer.predict(face)
