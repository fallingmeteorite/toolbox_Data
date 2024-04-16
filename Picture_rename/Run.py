#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
from invoke import run

parser = argparse.ArgumentParser()
parser.add_argument("--inupt_dir", type=str, default="../Input/")
parser.add_argument("--output_dir", type=str, default="../Output/")
parser.add_argument("--globalname", type=str, default="0")
args = parser.parse_args()
inupt_dir = args.inupt_dir
output_dir = args.output_dir
globalname = args.globalname

run(inupt_dir, output_dir, globalname)
