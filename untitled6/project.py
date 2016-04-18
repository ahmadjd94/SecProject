# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from Crypto.Hash import SHA,SHA256,SHA512,MD5
import codecs

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(610, 453)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.radioButton = QtWidgets.QRadioButton(self.centralWidget)
        self.radioButton.setGeometry(QtCore.QRect(40, 30, 114, 22))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralWidget)
        self.radioButton_2.setGeometry(QtCore.QRect(150, 30, 114, 22))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.centralWidget)
        self.radioButton_3.setGeometry(QtCore.QRect(240, 30, 114, 22))
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(self.centralWidget)
        self.radioButton_4.setGeometry(QtCore.QRect(370, 30, 114, 22))
        self.radioButton_4.setObjectName("radioButton_4")
        self.pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(480, 330, 97, 27))
        self.pushButton.setObjectName("pushButton")
        self.radioButton_5 = QtWidgets.QRadioButton(self.centralWidget)
        self.radioButton_5.setGeometry(QtCore.QRect(400, 130, 171, 22))
        self.radioButton_5.setObjectName("radioButton_5")
        self.buttonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.radioButton_5)
        self.radioButton_6 = QtWidgets.QRadioButton(self.centralWidget)
        self.radioButton_6.setGeometry(QtCore.QRect(400, 260, 181, 22))
        self.radioButton_6.setObjectName("radioButton_6")
        self.buttonGroup.addButton(self.radioButton_6)
        self.textEdit = QtWidgets.QTextEdit(self.centralWidget)
        self.textEdit.setGeometry(QtCore.QRect(20, 210, 371, 111))
        self.textEdit.setObjectName("textEdit")
        self.lineEdit = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 130, 371, 25))
        self.lineEdit.setObjectName("lineEdit")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 610, 27))
        self.menuBar.setObjectName("menuBar")
        self.menuFiles = QtWidgets.QMenu(self.menuBar)
        self.menuFiles.setObjectName("menuFiles")
        self.menuAbout = QtWidgets.QMenu(self.menuBar)
        self.menuAbout.setObjectName("menuAbout")
        self.message=QtWidgets.QMessageBox()

        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)

        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.menuFiles.addAction(self.actionOpen)
        self.menuFiles.addAction(self.actionSave)
        self.menuBar.addAction(self.menuFiles.menuAction())
        self.menuBar.addAction(self.menuAbout.menuAction())
        self.radioButton_5.clicked.connect(self.loadFile)
        self.radioButton_6.clicked.connect(self.loadText)
        self.pushButton.clicked.connect(self.PARTY)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def loadFile(self):
        self.textEdit.setDisabled(True)
        self.lineEdit.setDisabled(False)
    def loadText(self):
        self.lineEdit.setDisabled(True)
        self.textEdit.setDisabled(False)
    def PARTY (self):
        text=""
        working=False
        if self.radioButton_5.isChecked():
            f=open(self.lineEdit.text(),'r')
            for i in f:
                text+=i
            working=True
        elif self.radioButton_6.isChecked():
            text=self.textEdit.toPlainText()
            working=True
        else:
            self.message.setText("please select something to load")
            self.message.show()
        if working:
            if self.radioButton.isChecked():
                hsh=MD5.new()
                hsh.update(codecs.encode(text,'ascii'))
                self.message.setText("generated hash is :")
                self.message.setDetailedText(hsh.hexdigest())
                self.message.show()

            if self.radioButton_2.isChecked():
                hsh=SHA.new()
                hsh.update(codecs.encode(text,'ascii'))
                self.message.setText("generated hash is :")
                self.message.setDetailedText(hsh.hexdigest())
                self.message.show()


            if self.radioButton_3.isChecked():
                hsh=SHA256.new()
                hsh.update(codecs.encode(text,'ascii'))
                self.message.setText("generated hash is :")
                self.message.setDetailedText(hsh.hexdigest())
                self.message.show()


            if self.radioButton_4.isChecked():
                hsh=SHA512.new()
                hsh.update(codecs.encode(text,'ascii'))
                self.message.setText("generated hash is :")
                self.message.setDetailedText(hsh.hexdigest())
                self.message.show()







    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.radioButton.setText(_translate("MainWindow", "MD5"))
        self.radioButton_2.setText(_translate("MainWindow", "SHA-1"))
        self.radioButton_3.setText(_translate("MainWindow", "SHA256"))
        self.radioButton_4.setText(_translate("MainWindow", "SHA512"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.radioButton_5.setText(_translate("MainWindow", "calculate hash for file"))
        self.radioButton_6.setText(_translate("MainWindow", "calculate hash for text"))
        self.menuFiles.setTitle(_translate("MainWindow", "files"))
        self.menuAbout.setTitle(_translate("MainWindow", "about"))
        self.actionOpen.setText(_translate("MainWindow", "open"))
        self.actionSave.setText(_translate("MainWindow", "save"))
        self.message.setGeometry(500,500,800,400)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

