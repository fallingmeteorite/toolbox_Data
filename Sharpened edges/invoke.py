#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Sharpened_edges import start
import sys
import os
from tqdm import tqdm
import time

sys.path.append('../../key.py')
from key import key

key()


def run(input_dir, output_dir):
    number_one = -1
    number_two = -1
    files = os.listdir(input_dir)
    num_png = len(files)
    for i in tqdm(range(num_png), desc=r"处理进度", ncols=150):
        number_one += 1
        number_two += 1
        file_one = (files[number_one])
        time.sleep(1.0)
        try:
            if file_one.endswith(r".png"):
                start(input_dir + file_one, output_dir + file_one)
            else:
                pass
        except:
            print("文件损坏,无法完成处理")
            print("损坏文件名称:" + str(file_one))
