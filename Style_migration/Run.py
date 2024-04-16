#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
from invoke import run

parser = argparse.ArgumentParser()
parser.add_argument("--inupt_dir", type=str, default="../Input/")
parser.add_argument("--output_dir", type=str, default="../Output/")
parser.add_argument("--Style_imgsize", type=str, default="01.png")
parser.add_argument("--imgsize", type=int, default=512)
args = parser.parse_args()
inupt_dir = args.inupt_dir
output_dir = args.output_dir
Style_imgsize = args.Style_imgsize
imgsize = args.imgsize

run(inupt_dir, output_dir, Style_imgsize, imgsize)
