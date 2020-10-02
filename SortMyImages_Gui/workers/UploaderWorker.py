from PyQt5.QtCore import QObject,QRunnable,pyqtSignal,pyqtSlot
import os,json,ast,requests

class UploadWorkerSignals(QObject):
    killMe:bool=False
    finished:pyqtSignal=pyqtSignal()
    hasResponse:pyqtSignal=pyqtSignal(requests.Response)
    session:requests.Session=requests.Session()
    hasErrors:pyqtSignal=pyqtSignal(Exception)

    @pyqtSlot()
    def kill(self):
        self.killMe=True
        self.session.close()


class UploadWorker(QRunnable):
    signals=UploadWorkerSignals()
    img_path=None
    def __init__(self,endpoint,img_path):
        super(UploadWorker,self).__init__()
        self.img=img_path
        self.endpoint=endpoint

    def run(self):
        try:
            files={'file':open(self.img,'rb')}
            response=self.signals.session.post(self.endpoint,files=files)
            if response:
                self.signals.hasResponse.emit(response)
        except Exception as e:
            self.signals.hasErrors.emit(e)
        
        self.signals.finished.emit()
        
