#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
from invoke import run

parser = argparse.ArgumentParser()
parser.add_argument("--inupt_dir", type=str, default="../Input/")
parser.add_argument("--output_dir", type=str, default="../Output/")
parser.add_argument("--size", type=str, default=2)
args = parser.parse_args()
inupt_dir = args.inupt_dir
output_dir = args.output_dir
size = args.size

run(inupt_dir, output_dir, size)
