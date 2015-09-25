#!/usr/bin/env python
from __future__ import print_function
import argparse
import pkgutil
import os
import sys
import subprocess

def init_args():
    parser = argparse.ArgumentParser(description="Where is my Python module installed?")
    parser.add_argument("module", nargs="?", help="Module to locate.")
    return parser.parse_args()

def run_find(paths, args):
    for p in paths:
        path, pkg = os.path.split(p)
        if not args.module or pkg == args.module:
            print(p)

def main():
    argsdict = init_args()
    argslist = sys.argv[1:]
    pkgs2 = subprocess.check_output(["python2", "listpkg.py"] + argslist).split('\n')
    pkgs3 = subprocess.check_output(["python3", "listpkg.py"] + argslist).split('\n')
    pkgs = set(pkgs2).union(set(pkgs3))
    run_find(pkgs, argsdict)

if __name__ == '__main__':
    main()
