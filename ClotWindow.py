from PyQt5.QtWidgets import QMainWindow,QLabel,QProgressBar,QVBoxLayout,QWidget,QHBoxLayout,QMessageBox
from PyQt5.QtCore import Qt,pyqtSignal
from PyQt5.QtGui import QIcon
import base64
import os
from seg_ico import imglogo

class Process(QMainWindow):
    _clotProcessSignal = pyqtSignal(str)
    def __init__(self,isClosed):
        super().__init__()
        self.closed=isClosed
        self.initUI()
    

    def initUI(self):
        self.setFixedSize(500,120)
        #self.setGeometry(200, 300, 800, 600)
        tmp = open('in.ico', 'wb')
        tmp.write(base64.b64decode(imglogo))
        tmp.close()
        self.setWindowIcon(QIcon("in.ico"))
        os.remove('in.ico')
        if self.closed==False:
            self.setWindowFlags(Qt.WindowMinimizeButtonHint|Qt.WindowStaysOnTopHint)
        else:
            self.setWindowFlags(Qt.WindowStaysOnTopHint)
        #self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.setWindowTitle("Clot Detection")
        self.setGeometry(600, 500, 500, 100)
        self.show()
        #self.exec()
        self.mainLayout = QVBoxLayout()
        self.mainlayout_widget = QWidget()
        self.upLayout=QHBoxLayout()
        self.downLayout=QHBoxLayout()
        self.mainLayout.addLayout(self.upLayout)
        self.mainLayout.addLayout(self.downLayout)
        self.mainlayout_widget.setLayout(self.mainLayout)
        self.setCentralWidget(self.mainlayout_widget)


        self.processLabel_01 = QLabel()
        self.processLabel_01.setText("Processing:")
        self.processLabel_01.move(10, 40)
        self.processBar = QProgressBar()
        self.processBar.setGeometry(110, 35,200,30)
        self.processBar.setStyleSheet(("QProgressBar{border:1px solid #FFFFFF;"
                                        "height:30;"
                                        "background:gray;"
                                        "text-align:center;}"))
        self.processBar.setValue(0)
        self.fillLabel=QLabel()
        self.label=QLabel()
        #self.label.setGeometry(0,80,10,5)
        self.label02=QLabel()
        self.label.setGeometry(0,80,10,5)
        self.processLabel_02 = QLabel()
        self.processLabel_02.setText("                  Initializing...")
        self.processLabel_02.resize(300, 20)
        self.processLabel_02.move(55, 80)
        # self.processLabel_03=QLabel(self.processWindow)
        # self.processLabel_03.setText("MAKABAKA")
        # self.processLabel_03.move(120,85)
        # self.processLabel_04 = QLabel()
        # self.processLabel_04.setText("")
        # self.processLabel_04.resize(150, 20)
        # self.processLabel_04.move(330, 40)
        # self.processLabel_01 = QLabel()
        # self.processLabel_01.setText("Processing:")
        # self.processLabel_01.setGeometry(10, 40,90,5)
        # self.processBar = QProgressBar()
        # self.processBar.setGeometry(110, 35,200,30)
        # self.processBar.setStyleSheet(("QProgressBar{border:1px solid #FFFFFF;"
        #                                 "height:30;"
        #                                 "background:gray;"
        #                                 "text-align:center;}"))
        # self.processBar.setValue(0)
        # self.label=QLabel()
        # #self.label.setGeometry(0,80,10,5)
        # self.label02=QLabel()
        # self.label.setGeometry(0,80,10,5)
        # self.processLabel_02 = QLabel()
        # self.processLabel_02.setText("")
        # self.processLabel_02.resize(300, 20)
        # self.processLabel_02.setGeometry(70, 80,150,5)
        # # self.processLabel_03=QLabel(self.processWindow)
        # # self.processLabel_03.setText("MAKABAKA")
        # # self.processLabel_03.move(120,85)
        self.processLabel_04 = QLabel()
        self.processLabel_04.setText("")
        self.processLabel_04.resize(150, 20)
        # #横着第一排
        # self.processLabel_04.setGeometry(330, 40,100,5)

        self.upLayout.addWidget(self.processLabel_01)
        self.upLayout.addWidget(self.processBar)
        self.upLayout.addWidget(self.processLabel_04)
        self.downLayout.addWidget(self.label)
        self.downLayout.addWidget(self.processLabel_02)
        self.downLayout.addWidget(self.label02)
        self.downLayout.addWidget(self.fillLabel)
        

    def closeEvent(self,event):
        if self.isHidden()==False:
            result=QMessageBox.question(self,"'Warning!'","Are you sure to close the window, that means you discard clot detection!",QMessageBox.Yes|QMessageBox.No,QMessageBox.No)
            if result==QMessageBox.Yes:
                self._clotProcessSignal.emit("Closed")
                event.accept()
            else:
                event.ignore()
        else:
            self.close()