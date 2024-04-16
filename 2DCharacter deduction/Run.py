#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
from invoke import run

parser = argparse.ArgumentParser()
parser.add_argument('--input_dir', type=str, default='../Input', help='input data dir')
parser.add_argument('--output_dir', type=str, default='../Output', help='output dir')
parser.add_argument('--img_size', type=int, default=1024, help='hyperparameter, input image size of the net')
parser.add_argument('--device', type=str, default='cpu', help='cpu or cuda:0')
opt = parser.parse_args()
data = opt.input_dir
out = opt.output_dir
img_size = opt.img_size
device = opt.device

run(data, out, img_size, device)
