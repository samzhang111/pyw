from __future__ import print_function
import pkgutil
import sys
import os
import argparse
import pyw

def list_packages():
    args = pyw.init_args()

    opath = os.getenv('PATH').split(':')
    sys.path.extend(opath)

    for (path_wrapper, pkg, is_library) in pkgutil.iter_modules():
        try:
            print(os.path.join(path_wrapper.path, pkg))
        except AttributeError:
            continue

if __name__ == '__main__':
    list_packages()
