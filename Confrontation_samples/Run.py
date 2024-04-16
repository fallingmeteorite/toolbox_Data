#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
from invoke import run

parser = argparse.ArgumentParser()
parser.add_argument("--inupt_dir", type=str, default="../Input/")
parser.add_argument("--output_dir", type=str, default="../Output/")
parser.add_argument("--epochs", type=int, default=800)
parser.add_argument("--Learning_rate", type=int, default=0.0001)
parser.add_argument("--target", type=int, default=512)
args = parser.parse_args()
inupt_dir = args.inupt_dir
output_dir = args.output_dir
epochs = args.epochs
Learning_rate = args.Learning_rate
target = args.target

run(inupt_dir, output_dir, epochs, Learning_rate, target)
