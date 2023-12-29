#!/usr/bin/python3
# _*_ coding: utf-8 _*_
#
# Copyright (C) 2023 - 2023 Gosu, Inc. All Rights Reserved 
#
# @Time    : 2023/12/28 15:19
# @Author  : GosuXX
# @File    : test2.py

# coding=gbk
"""
图片人脸识别
作者：川川
@时间  : 2021/9/5 17:22
"""
import cv2
import numpy as np

prototxt_path = r"./deploy.prototxt.txt"
model_path = r"./res10_300x300_ssd_iter_140000_fp16.caffemodel"

model = cv2.dnn.readNetFromCaffe(prototxt_path, model_path)
image = cv2.imread("img/img1.jpg")
h, w = image.shape[:2]
blob = cv2.dnn.blobFromImage(image, 1.0, (300, 300), (104.0, 177.0, 123.0))
model.setInput(blob)
output = np.squeeze(model.forward())
font_scale = 1.0
for i in range(0, output.shape[0]):
    confidence = output[i, 2]
    if confidence > 0.5:
        box = output[i, 3:7] * np.array([w, h, w, h])
        start_x, start_y, end_x, end_y = box.astype(np.int)
        cv2.rectangle(image, (start_x, start_y), (end_x, end_y), color=(255, 0, 0), thickness=2)
        cv2.putText(image, f"{confidence * 100:.2f}%", (start_x, start_y - 5), cv2.FONT_HERSHEY_SIMPLEX, font_scale,
                    (255, 0, 0), 2)
cv2.imshow("image", image)
cv2.waitKey(0)
cv2.imwrite("beauty_detected.jpg", image)
