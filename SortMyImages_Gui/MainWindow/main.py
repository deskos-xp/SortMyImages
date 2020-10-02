from PyQt5 import uic
from PyQt5.QtCore import QThreadPool,QObject,QRunnable,QThread,pyqtSignal,pyqtSlot
from PyQt5.QtWidgets import QApplication,QMainWindow,QDialog,QHeaderView,QShortcut
import os,ast,sys,json,ast
from PyQt5.QtGui import QIcon,QImage,QKeySequence,QPixmap
import logging
logging.basicConfig(level=logging.INFO)
from pathlib import Path
from UIC.forms import uic_forms
from Generator.Generator import gen as img_src
from PIL import Image
from workers.UploaderWorker import UploadWorker
import argparse
class Main(QMainWindow):
    src="../images_src"
 
    def __init__(self):
        super(QMainWindow,self).__init__() 

        parser=argparse.ArgumentParser()
        parser.add_argument('-s','--img-src',help="where images come from")
        options=parser.parse_args()
        if options.img_src:
            self.src=options.img_src

        self.forms=uic_forms()         
        uic.loadUi(self.forms.files['main.ui'],self)
        self.buttons()
        self.imgs_src=img_src(self.src)
        cur=self.imgs_src.__next__()
        self.img.setPixmap(QPixmap(cur))
        self.path.setText(cur)
        self.resolution.setText('{}'.format(Image.open(cur).size))
        print(dir(self.imgs_src))

    def next_img(self):
        im=self.imgs_src.__next__()
        self.img.setPixmap(QPixmap(im))
        self.path.setText(im)
        self.resolution.setText('{}'.format(Image.open(im).size))

    '''
    def handle_testing(self):
        logging.info(self.sender())
        w=UploadWorker('http://localhost:8000/sorterdb/upload_testing/',self.path.text())
        w.signals.finished.connect(lambda :logging.info('uploaded testing'))
        w.signals.hasErrors.connect(logging.error)
        w.signals.hasResponse.connect(logging.info)

        QThreadPool.globalInstance().start(w)
        self.next_img()
    '''
    def handle_training(self):
        try:
            logging.info(self.sender())
            w=UploadWorker('http://localhost:8000/sorterdb/upload_training/',self.path.text())
            w.signals.finished.connect(lambda :logging.info('uploaded training'))
            w.signals.hasErrors.connect(logging.error)
            w.signals.hasResponse.connect(logging.info)

            QThreadPool.globalInstance().start(w)
            self.next_img()
        except Exception as e:
            logging.error(e)

    def handle_unuseable(self):
        try:
            logging.info(self.sender())
            w=UploadWorker('http://localhost:8000/sorterdb/upload_unuseable/',self.path.text())
            w.signals.finished.connect(lambda :logging.info('uploaded unuseable'))
            w.signals.hasErrors.connect(logging.error)
            w.signals.hasResponse.connect(logging.info)

            QThreadPool.globalInstance().start(w)

            self.next_img()
        except Exception as e:
            logging.error(e)
        
    def buttons(self):
        #self.testing_sc=QShortcut(QKeySequence('q'),self)
        #self.testing_sc.activated.connect(self.handle_testing)

        self.training_sc=QShortcut(QKeySequence('a'),self)
        self.training_sc.activated.connect(self.handle_training)
        
        self.unuseable_sc=QShortcut(QKeySequence('d'),self)
        self.unuseable_sc.activated.connect(self.handle_unuseable)    

        #self.testing.clicked.connect(self.handle_testing)
        self.training.clicked.connect(self.handle_training)
        self.unuseable.clicked.connect(self.handle_unuseable)
        
def main():
    app=QApplication(sys.argv)
    win=Main()
    win.show()
    app.exec_()
