#!/usr/bin/python3
# _*_ coding: utf-8 _*_
#
# Copyright (C) 2023 - 2023 Gosu, Inc. All Rights Reserved 
#
# @Time    : 2023/12/28 15:25
# @Author  : GosuXX
# @File    : label_generator.py

import os
import cv2
import numpy as np
from PIL import Image

from utils.env import clear_path


def gen_faces_xml():
    """ Generate the yml file for face-data. """
    clear_path(res_path := os.path.abspath("res"))
    recognizer = cv2.face.LBPHFaceRecognizer.create()
    model_file = f'{os.path.dirname(cv2.__file__)}\\data\\haarcascade_frontalface_default.xml'
    detector = cv2.CascadeClassifier(model_file)
    image_paths = [os.path.join("dataset", f) for f in os.listdir("dataset")]
    face_samples = []
    label_ids = []

    for image_path in image_paths:
        img = Image.open(image_path).convert('L')
        img_np = np.array(img, 'uint8')
        if os.path.split(image_path)[-1].split(".")[-1] != 'jpg':
            continue

        label_id = hash(os.path.split(image_path)[-1].split(".")[0])
        faces = detector.detectMultiScale(img_np)

        for (x, y, w, h) in faces:
            face_samples.append(img_np[y:y + h, x:x + w])
            label_ids.append(label_id)

    recognizer.train(face_samples, np.array(label_ids))
    recognizer.save(res_path + "/trainer.yml")
    print(f"{res_path}/trainer.yml generated!")
    return face_samples, label_ids
