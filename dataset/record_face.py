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

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
face_detector = cv2.CascadeClassifier(f'{os.path.dirname(cv2.__file__)}\\data\\haarcascade_frontalface_default.xml')
face_id = input('User data input,Look at the camera and wait ...')
count = 0

while cap.isOpened():
    ret, frame = cap.read()
    if ret is True:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    else:
        break
    faces = face_detector.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + w), (255, 0, 0))
        count += 1
        cv2.imwrite(str(face_id) + '.' + str(count) + '.jpg', gray[y:y + h, x:x + w])
        cv2.imshow('image', frame)
    k = cv2.waitKey(1)
    if k == 27:
        break
    elif count >= 200:
        break

cap.release()
cv2.destroyAllWindows()
