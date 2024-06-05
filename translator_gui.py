# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'translator.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets



class Ui_MainWindow(QtWidgets.QMainWindow):
    '''QtPy GUI. Main window, button and etc.'''
    def __init__(self) -> None:
        super(Ui_MainWindow, self).__init__()
        self.setupUi()


    
    
    def setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(800, 600)
        
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        
        self.originalText = QtWidgets.QTextEdit(self)
        self.originalText.setGeometry(QtCore.QRect(50, 50, 700, 200))
        self.originalText.setStyleSheet("")
        self.originalText.setObjectName("originalText")
        
        self.translatedText = QtWidgets.QLabel(self.centralwidget)
        self.translatedText.setGeometry(QtCore.QRect(50, 350, 700, 200))
        self.translatedText.setStyleSheet("border: 1px solid black;")
        self.translatedText.setText("Перевод")
        self.translatedText.setAlignment(QtCore.Qt.AlignTop|QtCore.Qt.AlignLeft)
        self.translatedText.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.translatedText.setObjectName("translatedText")
        
        self.translateButton = QtWidgets.QPushButton(self.centralwidget)
        self.translateButton.setGeometry(QtCore.QRect(50, 305, 120, 35))
        self.translateButton.setObjectName("translateButton")
        
        self.changeLang = QtWidgets.QComboBox(self.centralwidget)
        self.changeLang.setGeometry(QtCore.QRect(50, 260, 120, 35))
        self.changeLang.setObjectName("changeLang")
        self.changeLang.addItem("")
        self.changeLang.addItem("")
        
        
        self.setCentralWidget(self.centralwidget)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "High mind translator"))
        self.originalText.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.translateButton.setText(_translate("MainWindow", "Перевести"))
        self.changeLang.setItemText(0, _translate("MainWindow", "Русский - Шотыну"))
        self.changeLang.setItemText(1, _translate("MainWindow", "Шотыну - Русский"))
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_MainWindow()
    ui.show()
    sys.exit(app.exec_())
