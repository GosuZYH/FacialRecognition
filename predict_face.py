#!/usr/bin/python3
# _*_ coding: utf-8 _*_
#
# Copyright (C) 2023 - 2023 Gosu, Inc. All Rights Reserved 
#
# @Time    : 2023/12/29 15:08
# @Author  : GosuXX
# @File    : predict_face.py
import os

import cv2

from utils.file_helper import read_yml

FONT = cv2.FONT_HERSHEY_SIMPLEX


def predict_face(target=None):
    recognizer = cv2.face.LBPHFaceRecognizer.create()
    recognizer.read('res/trainer.yml')
    model_file = f'{os.path.dirname(cv2.__file__)}\\data\\haarcascade_frontalface_default.xml'
    face_cascade = cv2.CascadeClassifier(model_file)
    all_labels = data if (data := read_yml("labels.yml")) is not None else {}

    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    cap.set(6, cv2.VideoWriter.fourcc('M', 'J', 'P', 'G'))
    minW = 0.1 * cap.get(3)
    minH = 0.1 * cap.get(4)

    while True:
        ret, img = cap.read()
        if not ret:
            break
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.2,
            minNeighbors=5,
            minSize=(int(minW), int(minH))
        )
        for (x, y, w, h) in faces:
            face_id, confidence = recognizer.predict(gray[y:y + h, x:x + w])
            if (40 < confidence < 50) and ((res := all_labels.get(face_id, None)) is not None):
                label = all_labels[face_id]
                confidence = "{0}%".format(round(100 - confidence))
                if res == target:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
                cv2.putText(img, f"{label}-{str(confidence)}", (x + 5, y - 5), FONT, 1, (0, 0, 255), 2)
            else:
                label = "unknown"
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
                cv2.putText(img, f"{label}", (x + 5, y - 5), FONT, 1, (0, 0, 255), 2)
            cv2.imshow('camera', img)
        k = cv2.waitKey(1)

    cap.release()
    cv2.destroyAllWindows()
