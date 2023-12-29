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


def generate_images_and_labels(dir):
    labels = []
    images = []
    label = 0

    # 遍历目录中的每个子目录
    for subdir in os.listdir(dir):
        subdir_path = os.path.join(dir, subdir)

        if os.path.isdir(subdir_path):
            # 遍历子目录中的每个图像文件
            for filename in os.listdir(subdir_path):
                filepath = os.path.join(subdir_path, filename)

                # 读取图像文件
                img = cv2.imread(filepath)  # cv2.IMREAD_GRAYSCALE

                if img is not None:
                    # 将图像添加到图像列表中
                    images.append(img)
                    # 将标签添加到标签列表中
                    labels.append(label)

            # 对于每个子目录，我们使用一个新的标签
            label += 1

    return images, np.array(labels)


images, labels = generate_images_and_labels('dataset')
print("ok")
