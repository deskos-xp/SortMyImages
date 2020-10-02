import pathlib
from pathlib import Path
import os
class uic_forms:
    def __init__(self):
        self.root=pathlib.Path().absolute()/pathlib.Path('UIC')
        self.files={}
        self.scan() 
    
    def scan(self):
        for root,dirname,fnames in os.walk(self.root):
            for fname in fnames:
                self.files[fname]=Path(root)/Path(fname)


        print(self.root,self.files)
