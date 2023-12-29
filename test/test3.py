#!/usr/bin/python3
# _*_ coding: utf-8 _*_
#
# Copyright (C) 2023 - 2023 Gosu, Inc. All Rights Reserved 
#
# @Time    : 2023/12/28 15:22
# @Author  : GosuXX
# @File    : test3.py

""" 训练模型 """
import cv2
import numpy as np

# 创建LBPH人脸识别器
recognizer = cv2.face.LBPHFaceRecognizer_create()

# 训练识别器
recognizer.train(images, np.array(labels))

# 保存模型
recognizer.save('my_model.xml')
