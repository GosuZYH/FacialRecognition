#!/usr/bin/python3
# _*_ coding: utf-8 _*_
#
# Copyright (C) 2023 - 2023 Gosu, Inc. All Rights Reserved 
#
# @Time    : 2023/12/29 10:30
# @Author  : GosuXX
# @File    : record_face.py
import os

import cv2

from utils.env import clear_path
from utils.file_helper import read_yml


def record_face():
    """ Record several images for label-face to dataset. """
    clear_path(temp_path := os.path.abspath("dataset"))
    model_file = f'{os.path.dirname(cv2.__file__)}\\data\\haarcascade_frontalface_default.xml'
    face_detector = cv2.CascadeClassifier(model_file)
    face_label = input('Input your name and look at the camera:')
    all_labels = read_yml("labels.yml")
    count = 0

    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    while cap.isOpened() and (count <= 100):  # 当摄像头开着的时候且保存的照片少于阈值
        ret, frame = cap.read()  # ret为Bool判断读取成功/失败  frame为帧截图
        if not ret:
            # 摄像头断开就出去
            break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # 图片covert灰度处理
        face = face_detector.detectMultiScale(gray, 1.3, 5)  # 用选择face_detector把脸信息搞出来
        cv2.putText(frame, f"Hi,{face_label},Please hold your face on camera", (25, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), thickness=2)
        for (x, y, w, h) in face:
            # 给脸的坐标画框并把图导出来
            cv2.putText(frame, face_label, (x, y - 6), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 255, 0), thickness=1)
            cv2.rectangle(frame, (x, y), (x + w, y + w), (0, 255, 0), thickness=2)
            cv2.imwrite(f"{temp_path}/{str(face_label)}.{str(count)}.jpg", gray[y:y + h, x:x + w])
            count += 1
        cv2.imshow('Capture', frame)
        k = cv2.waitKey(1)  # k=27则为ESC 1则为1ms停顿

    _, frame = cap.read()
    cv2.putText(frame, "Fine!", (30, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), thickness=2)
    cv2.imshow('Capture', frame)
    cv2.waitKey(0)  # k=27则为ESC 1则为1ms停顿
    cap.release()
    cv2.destroyAllWindows()
