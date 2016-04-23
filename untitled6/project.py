# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from Crypto.Hash import SHA,SHA256,SHA512,MD5
import codecs,string

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(610, 453)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralWidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 601, 391))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_3.setGeometry(QtCore.QRect(139, 30, 351, 25))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label = QtWidgets.QLabel(self.tab)

        self.label.setGeometry(QtCore.QRect(30, 32, 67, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(40, 80, 67, 17))
        self.label_2.setObjectName("label_2")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_4.setGeometry(QtCore.QRect(140, 80, 351, 25))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.textEdit_3 = QtWidgets.QTextEdit(self.tab)
        self.textEdit_3.setGeometry(QtCore.QRect(140, 140, 351, 141))
        self.textEdit_3.setObjectName("textEdit_3")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(40, 190, 67, 17))
        self.label_3.setObjectName("label_3")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab)
        self.pushButton_3.setGeometry(QtCore.QRect(400, 310, 185, 27))
        self.pushButton_3.setObjectName("pushButton_3")
        self.radioButton_7 = QtWidgets.QRadioButton(self.tab)
        self.radioButton_7.setGeometry(QtCore.QRect(120, 310, 114, 22))
        self.radioButton_7.setObjectName("radioButton_7")
        self.radioButton_8 = QtWidgets.QRadioButton(self.tab)
        self.radioButton_8.setGeometry(QtCore.QRect(280, 310, 114, 22))
        self.radioButton_8.setObjectName("radioButton_8")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.group0=QtWidgets.QGroupBox(self.tab_2)

        self.group=QtWidgets.QGroupBox(self.tab_2)
        self.radioButton_6 = QtWidgets.QRadioButton(self.group)
        self.radioButton_6.setGeometry(QtCore.QRect(390, 250, 181, 22))
        self.radioButton_6.setObjectName("radioButton_6")
        self.radioButton = QtWidgets.QRadioButton(self.tab_2)
        self.radioButton.setGeometry(QtCore.QRect(30, 20, 114, 22))
        self.radioButton.setObjectName("radioButton")
        self.textEdit = QtWidgets.QTextEdit(self.tab_2)
        self.textEdit.setGeometry(QtCore.QRect(10, 200, 371, 111))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(self.tab_2)
        self.pushButton.setGeometry(QtCore.QRect(470, 320, 97, 27))
        self.pushButton.setObjectName("pushButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.tab_2)
        self.radioButton_2.setGeometry(QtCore.QRect(140, 20, 114, 22))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_4 = QtWidgets.QRadioButton(self.tab_2)
        self.radioButton_4.setGeometry(QtCore.QRect(360, 20, 114, 22))

        self.radioButton_4.setObjectName("radioButton_4")
        self.radioButton_5 = QtWidgets.QRadioButton(self.group)
        self.radioButton_5.setGeometry(QtCore.QRect(390, 120, 171, 22))
        self.radioButton_5.setObjectName("radioButton_5")
        self.radioButton_3 = QtWidgets.QRadioButton(self.tab_2)
        self.radioButton_3.setGeometry(QtCore.QRect(230, 20, 114, 22))
        self.radioButton_3.setObjectName("radioButton_3")
        self.lineEdit = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit.setGeometry(QtCore.QRect(10, 120, 371, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 610, 27))
        self.menuBar.setObjectName("menuBar")
        self.menuFiles = QtWidgets.QMenu(self.menuBar)
        self.menuFiles.setObjectName("menuFiles")
        self.menuAbout = QtWidgets.QMenu(self.menuBar)
        self.menuAbout.setObjectName("menuAbout")
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
        self.pushButton_3.clicked.connect(self.PARTY2)
        self.radioButton_7.clicked.connect(self.switch)
        self.radioButton_8.clicked.connect(self.switch1)
        self.message=QtWidgets.QMessageBox()
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def switch(self):
        self.textEdit_3.setDisabled(True)
        self.lineEdit_3.setDisabled(False)
    def switch1(self):
        self.lineEdit_3.setDisabled(True)
        self.textEdit_3.setDisabled(False)
    def loadFile(self):
        self.textEdit.setDisabled(True)
        self.lineEdit.setDisabled(False)
    def loadText(self):
        self.lineEdit.setDisabled(True)
        self.textEdit.setDisabled(False)

    def PARTY2(self):

        key=self.lineEdit_4.text().upper()


        dic={}    #create dictionary to use for encryption and decryption
        alpha = list(string.ascii_uppercase)    #create a list of normal alphabets
        for j in alpha:                         #initialize the dictionary with keys
            dic[j]=[]
        for k in dic.keys():                    #making the suitable shifts  in the alphabet sequence
            shift=alpha.index(k)
            for i in range(shift,26):
                dic[k].append(alpha[i])
            for i in range(shift):
                    dic[k].append(alpha[i])
        if self.radioButton_7.isChecked():   # checking if the encrypt radio button is checked button

            a=list(self.lineEdit_3.text().upper())  # converting all letters to upper case letters
            m=""          # this string will be used to mathc the clear text in length
            for i in range(len (a)):
                m+=key[i%len(key)]
            m=list(m)
            self.textEdit_3.setReadOnly(False)
            CIPHER=""        #this string will store the cipher
            for i in range(len(m)):
                CIPHER+=(dic[m[i]][alpha.index(a[i])])  #using the dictornary to create the cipher
            self.textEdit_3.setText(CIPHER)
        if self.radioButton_8.isChecked():                  #this is the decryption radio button
            cipher=self.textEdit_3.toPlainText().upper()
            m=""
            for i in range(len (cipher)):
                m+=key[i%len(key)]
            m=list(m)
            key=self.lineEdit_4.text()

            CLEAR=""
            for i in range(len(m)):
                li=dic[m[i]]

                w=li.index(cipher[i])
                CLEAR+=alpha[w]
            self.lineEdit_3.setText(CLEAR)





    def retranslateUi(self, MainWindow):                                     # pyuic cenerated code

        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "clear text"))
        self.label_2.setText(_translate("MainWindow", "key"))
        self.label_3.setText(_translate("MainWindow", "cipher"))
        self.pushButton_3.setText(_translate("MainWindow", "generate cipher /clear text"))
        self.radioButton_7.setText(_translate("MainWindow", "encrypt"))
        self.radioButton_8.setText(_translate("MainWindow", "decrypt"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "vignere cipher"))
        self.radioButton_6.setText(_translate("MainWindow", "calculate hash for text"))
        self.radioButton.setText(_translate("MainWindow", "MD5"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.radioButton_2.setText(_translate("MainWindow", "SHA-1"))
        self.radioButton_4.setText(_translate("MainWindow", "SHA512"))
        self.radioButton_5.setText(_translate("MainWindow", "calculate hash for file"))
        self.radioButton_3.setText(_translate("MainWindow", "SHA256"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Hashing algorithms"))
        self.menuFiles.setTitle(_translate("MainWindow", "files"))
        self.menuAbout.setTitle(_translate("MainWindow", "about"))
        self.actionOpen.setText(_translate("MainWindow", "open"))
        self.actionSave.setText(_translate("MainWindow", "save"))
        self.message.setGeometry(500,500,800,400)

    def PARTY (self):                        #modern hashing algortihms tab
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

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

