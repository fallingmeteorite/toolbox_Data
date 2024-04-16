#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
from invoke import run

parser = argparse.ArgumentParser()
parser.add_argument("--inupt_dir", type=str, default="../Input/")
parser.add_argument("--output_dir", type=str, default="../Output/")
parser.add_argument("--long", type=int, default=1332)
parser.add_argument("--hight", type=int, default=290)
args = parser.parse_args()
inupt_dir = args.inupt_dir
output_dir = args.output_dir
long = args.long
hight = args.hight

run(inupt_dir, output_dir, long, hight)
