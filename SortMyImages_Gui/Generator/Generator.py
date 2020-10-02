import os,sys
from pathlib import Path

def gen(path):
    for root,dirname,fnames in os.walk(path,topdown=True):
        for fname in fnames:
            yield os.path.join(root,fname)
            
