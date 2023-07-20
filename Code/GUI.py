from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(650, 355)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("main_ico.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 650, 355))
        self.label.setStyleSheet("background-color: rgb(25,25,30)")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 651, 27))
        self.label_2.setStyleSheet("background-color: rgb(35,35,43)")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(3, 0, 70, 27))
        self.label_3.setStyleSheet("font: 63 16pt \"Mayberry Pro\";\n""")
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(625, 0, 27, 27))
        self.pushButton.setStyleSheet("QPushButton{\n"
"color: white;\n"
"background-color: rgb(35,35,43);\n"
"font: 63 12pt \"Mayberry Pro\";\n"
"border: none;\n"
"}\n"
"QPushButton:hover {\n"
"color: #e84118;\n"
"}\n"
"QPushButton:pressed {\n"
"color:#c23616;\n"
"}\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(600, 0, 27, 27))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"color: white;\n"
"background-color: rgb(35,35,43);\n"
"font: 63 16pt \"Mayberry Pro\";\n"
"border: none;\n"
"}\n"
"QPushButton:hover {\n"
"color: rgb(200,200,200);\n"
"}\n"
"QPushButton:pressed {\n"
"color: rgb(150,150,150);\n"
"}\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(3, 30, 210, 62))
        self.label_4.setStyleSheet("background-color: rgb(30,30,35);\n"
"border: 1px solid rgb(35,35,40)")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(3, 32, 209, 20))
        self.label_5.setStyleSheet("font: 63 14pt \"Mayberry Pro\";\n"
"")
        self.label_5.setObjectName("label_5")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(6, 60, 100, 28))
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"color: white;\n"
"background-color: rgb(40,40,45);\n"
"font: 63 11pt \"Mayberry Pro\";\n"
"font-weight: bold;\n"
"border: none;\n"
"}\n"
"QPushButton:hover {\n"
"border: 1px solid rgb(70,70,75);\n"
"background-color: rgb(43,43,48);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(45,45,50);\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(110, 60, 100, 28))
        self.pushButton_4.setStyleSheet("QPushButton{\n"
"color: white;\n"
"background-color: rgb(40,40,45);\n"
"font: 63 11pt \"Mayberry Pro\";\n"
"font-weight: bold;\n"
"border: none;\n"
"}\n"
"QPushButton:hover {\n"
"border: 1px solid rgb(70,70,75);\n"
"background-color: rgb(43,43,48);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(45,45,50);\n"
"}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(3, 95, 210, 62))
        self.label_6.setStyleSheet("background-color: rgb(30,30,35);\n"
"border: 1px solid rgb(35,35,40)")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(3, 160, 210, 62))
        self.label_7.setStyleSheet("background-color: rgb(30,30,35);\n"
"border: 1px solid rgb(35,35,40)")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(3, 225, 210, 62))
        self.label_8.setStyleSheet("background-color: rgb(30,30,35);\n"
"border: 1px solid rgb(35,35,40)")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(3, 290, 210, 62))
        self.label_9.setStyleSheet("background-color: rgb(30,30,35);\n"
"border: 1px solid rgb(35,35,40)")
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(0, 97, 209, 20))
        self.label_10.setStyleSheet("font: 63 14pt \"Mayberry Pro\";\n"
"")
        self.label_10.setObjectName("label_10")
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(6, 126, 100, 28))
        self.pushButton_5.setStyleSheet("QPushButton{\n"
"color: white;\n"
"background-color: rgb(40,40,45);\n"
"font: 63 11pt \"Mayberry Pro\";\n"
"font-weight: bold;\n"
"border: none;\n"
"}\n"
"QPushButton:hover {\n"
"border: 1px solid rgb(70,70,75);\n"
"background-color: rgb(43,43,48);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(45,45,50);\n"
"}")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(Form)
        self.pushButton_6.setGeometry(QtCore.QRect(110, 126, 100, 28))
        self.pushButton_6.setStyleSheet("QPushButton{\n"
"color: white;\n"
"background-color: rgb(40,40,45);\n"
"font: 63 11pt \"Mayberry Pro\";\n"
"font-weight: bold;\n"
"border: none;\n"
"}\n"
"QPushButton:hover {\n"
"border: 1px solid rgb(70,70,75);\n"
"background-color: rgb(43,43,48);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(45,45,50);\n"
"}")
        self.pushButton_6.setObjectName("pushButton_6")
        self.label_11 = QtWidgets.QLabel(Form)
        self.label_11.setGeometry(QtCore.QRect(0, 161, 209, 20))
        self.label_11.setStyleSheet("font: 63 14pt \"Mayberry Pro\";\n"
"")
        self.label_11.setObjectName("label_11")
        self.pushButton_7 = QtWidgets.QPushButton(Form)
        self.pushButton_7.setGeometry(QtCore.QRect(6, 190, 100, 28))
        self.pushButton_7.setStyleSheet("QPushButton{\n"
"color: white;\n"
"background-color: rgb(40,40,45);\n"
"font: 63 11pt \"Mayberry Pro\";\n"
"font-weight: bold;\n"
"border: none;\n"
"}\n"
"QPushButton:hover {\n"
"border: 1px solid rgb(70,70,75);\n"
"background-color: rgb(43,43,48);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(45,45,50);\n"
"}")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(Form)
        self.pushButton_8.setGeometry(QtCore.QRect(110, 190, 100, 28))
        self.pushButton_8.setStyleSheet("QPushButton{\n"
"color: white;\n"
"background-color: rgb(40,40,45);\n"
"font: 63 11pt \"Mayberry Pro\";\n"
"font-weight: bold;\n"
"border: none;\n"
"}\n"
"QPushButton:hover {\n"
"border: 1px solid rgb(70,70,75);\n"
"background-color: rgb(43,43,48);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(45,45,50);\n"
"}")
        self.pushButton_8.setObjectName("pushButton_8")
        self.label_12 = QtWidgets.QLabel(Form)
        self.label_12.setGeometry(QtCore.QRect(3, 224, 209, 30))
        self.label_12.setStyleSheet("font: 63 14pt \"Mayberry Pro\";\n"
"")
        self.label_12.setObjectName("label_12")
        self.pushButton_9 = QtWidgets.QPushButton(Form)
        self.pushButton_9.setGeometry(QtCore.QRect(6, 255, 100, 28))
        self.pushButton_9.setStyleSheet("QPushButton{\n"
"color: white;\n"
"background-color: rgb(40,40,45);\n"
"font: 63 11pt \"Mayberry Pro\";\n"
"font-weight: bold;\n"
"border: none;\n"
"}\n"
"QPushButton:hover {\n"
"border: 1px solid rgb(70,70,75);\n"
"background-color: rgb(43,43,48);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(45,45,50);\n"
"}")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(Form)
        self.pushButton_10.setGeometry(QtCore.QRect(110, 255, 100, 28))
        self.pushButton_10.setStyleSheet("QPushButton{\n"
"color: white;\n"
"background-color: rgb(40,40,45);\n"
"font: 63 11pt \"Mayberry Pro\";\n"
"font-weight: bold;\n"
"border: none;\n"
"}\n"
"QPushButton:hover {\n"
"border: 1px solid rgb(70,70,75);\n"
"background-color: rgb(43,43,48);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(45,45,50);\n"
"}")
        self.pushButton_10.setObjectName("pushButton_10")
        self.label_13 = QtWidgets.QLabel(Form)
        self.label_13.setGeometry(QtCore.QRect(3, 290, 209, 30))
        self.label_13.setStyleSheet("font: 63 14pt \"Mayberry Pro\";\n"
"")
        self.label_13.setObjectName("label_13")
        self.pushButton_11 = QtWidgets.QPushButton(Form)
        self.pushButton_11.setGeometry(QtCore.QRect(6, 320, 204, 28))
        self.pushButton_11.setStyleSheet("QPushButton{\n"
"color: white;\n"
"background-color: rgb(40,40,45);\n"
"font: 63 11pt \"Mayberry Pro\";\n"
"font-weight: bold;\n"
"border: none;\n"
"}\n"
"QPushButton:hover {\n"
"border: 1px solid rgb(70,70,75);\n"
"background-color: rgb(43,43,48);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(45,45,50);\n"
"}")
        self.pushButton_11.setObjectName("pushButton_11")
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(220, 31, 425, 191))
        self.textBrowser.setStyleSheet("background-color: rgb(45,45,50);\n"
"border: 1px solid rgb(100,100,100);\n"
"\n"
"color: white;\n"
"font: 11pt \"Arial\";\n"
"")
        self.textBrowser.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser.setObjectName("textBrowser")
        self.label_14 = QtWidgets.QLabel(Form)
        self.label_14.setGeometry(QtCore.QRect(435, 290, 210, 62))
        self.label_14.setStyleSheet("background-color: rgb(30,30,35);\n"
"border: 1px solid rgb(35,35,40)")
        self.label_14.setText("")
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(Form)
        self.label_15.setGeometry(QtCore.QRect(220, 290, 210, 62))
        self.label_15.setStyleSheet("background-color: rgb(30,30,35);\n"
"border: 1px solid rgb(35,35,40)")
        self.label_15.setText("")
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(Form)
        self.label_16.setGeometry(QtCore.QRect(436, 290, 209, 30))
        self.label_16.setStyleSheet("font: 63 14pt \"Mayberry Pro\";\n"
"")
        self.label_16.setObjectName("label_16")
        self.pushButton_12 = QtWidgets.QPushButton(Form)
        self.pushButton_12.setGeometry(QtCore.QRect(438, 320, 100, 28))
        self.pushButton_12.setStyleSheet("QPushButton{\n"
"color: white;\n"
"background-color: rgb(40,40,45);\n"
"font: 63 11pt \"Mayberry Pro\";\n"
"font-weight: bold;\n"
"border: none;\n"
"}\n"
"QPushButton:hover {\n"
"border: 1px solid rgb(70,70,75);\n"
"background-color: rgb(43,43,48);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(45,45,50);\n"
"}")
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(Form)
        self.pushButton_13.setGeometry(QtCore.QRect(543, 320, 100, 28))
        self.pushButton_13.setStyleSheet("QPushButton{\n"
"color: white;\n"
"background-color: rgb(40,40,45);\n"
"font: 63 11pt \"Mayberry Pro\";\n"
"font-weight: bold;\n"
"border: none;\n"
"}\n"
"QPushButton:hover {\n"
"border: 1px solid rgb(70,70,75);\n"
"background-color: rgb(43,43,48);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(45,45,50);\n"
"}")
        self.pushButton_13.setObjectName("pushButton_13")
        self.label_17 = QtWidgets.QLabel(Form)
        self.label_17.setGeometry(QtCore.QRect(220, 290, 209, 30))
        self.label_17.setStyleSheet("font: 63 14pt \"Mayberry Pro\";\n"
"")
        self.label_17.setObjectName("label_17")
        self.pushButton_14 = QtWidgets.QPushButton(Form)
        self.pushButton_14.setGeometry(QtCore.QRect(223, 320, 204, 28))
        self.pushButton_14.setStyleSheet("QPushButton{\n"
"color: white;\n"
"background-color: rgb(40,40,45);\n"
"font: 63 11pt \"Mayberry Pro\";\n"
"font-weight: bold;\n"
"border: none;\n"
"}\n"
"QPushButton:hover {\n"
"border: 1px solid rgb(70,70,75);\n"
"background-color: rgb(43,43,48);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(45,45,50);\n"
"}")
        self.pushButton_14.setObjectName("pushButton_14")
        self.label_18 = QtWidgets.QLabel(Form)
        self.label_18.setGeometry(QtCore.QRect(220, 225, 425, 61))
        self.label_18.setStyleSheet("background-color: rgb(30,30,35);\n"
"border: 1px solid rgb(35,35,40)")
        self.label_18.setText("")
        self.label_18.setObjectName("label_18")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(225, 230, 301, 30))
        self.lineEdit.setStyleSheet("background-color: rgb(45,45,50);\n"
"border: 1px solid rgb(100,100,100);\n"
"\n"
"color: white;\n"
"font: 11pt \"Arial\";\n"
"font-weight: bold;\n"
"\n"
"padding-left: 3px;\n"
"padding-right: 3px;\n"
"")
        self.lineEdit.setMaxLength(100)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_15 = QtWidgets.QPushButton(Form)
        self.pushButton_15.setGeometry(QtCore.QRect(530, 230, 111, 30))
        self.pushButton_15.setStyleSheet("QPushButton{\n"
"color: white;\n"
"background-color: rgb(40,40,45);\n"
"font: 63 11pt \"Mayberry Pro\";\n"
"font-weight: bold;\n"
"border: none;\n"
"}\n"
"QPushButton:hover {\n"
"border: 1px solid rgb(70,70,75);\n"
"background-color: rgb(43,43,48);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(45,45,50);\n"
"}")
        self.pushButton_15.setObjectName("pushButton_15")
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.pushButton_2.raise_()
        self.label_4.raise_()
        self.pushButton.raise_()
        self.pushButton_3.raise_()
        self.pushButton_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.label_10.raise_()
        self.pushButton_5.raise_()
        self.pushButton_6.raise_()
        self.label_11.raise_()
        self.pushButton_7.raise_()
        self.pushButton_8.raise_()
        self.label_12.raise_()
        self.pushButton_9.raise_()
        self.pushButton_10.raise_()
        self.label_13.raise_()
        self.pushButton_11.raise_()
        self.textBrowser.raise_()
        self.label_14.raise_()
        self.label_15.raise_()
        self.label_16.raise_()
        self.pushButton_12.raise_()
        self.pushButton_13.raise_()
        self.label_17.raise_()
        self.pushButton_14.raise_()
        self.label_18.raise_()
        self.lineEdit.raise_()
        self.pushButton_15.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        global _translate
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Stealth"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p><span style=\" font-weight:400; color:#ffffff;\">Stealth</span></p></body></html>"))
        self.pushButton.setText(_translate("Form", "X"))
        self.pushButton_2.setText(_translate("Form", "-"))
        self.label_5.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" color:#1884f8;\">Download</span></p></body></html>"))
        self.pushButton_3.setText(_translate("Form", "Открыть"))
        self.pushButton_4.setText(_translate("Form", "Очистить"))
        self.label_10.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" color:#1884f8;\">Recent</span></p></body></html>"))
        self.pushButton_5.setText(_translate("Form", "Открыть"))
        self.pushButton_6.setText(_translate("Form", "Очистить"))
        self.label_11.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" color:#1884f8;\">Prefetch</span></p></body></html>"))
        self.pushButton_7.setText(_translate("Form", "Открыть"))
        self.pushButton_8.setText(_translate("Form", "Очистить"))
        self.label_12.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" color:#1884f8;\">Temp</span></p></body></html>"))
        self.pushButton_9.setText(_translate("Form", "Открыть"))
        self.pushButton_10.setText(_translate("Form", "Очистить"))
        self.label_13.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" color:#1884f8;\">AppData</span></p></body></html>"))
        self.pushButton_11.setText(_translate("Form", "Открыть"))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_16.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" color:#1675e1;\">Kill Process</span></p></body></html>"))
        self.pushButton_12.setText(_translate("Form", "Включить"))
        self.pushButton_13.setText(_translate("Form", "Выключить"))
        self.label_17.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" color:#1675e1;\">Event Log</span></p></body></html>"))
        self.pushButton_14.setText(_translate("Form", "Очистить"))
        self.pushButton_15.setText(_translate("Form", "Удалить"))

class Widget(QtWidgets.QWidget, Ui_Form):
    def __init__(self, parent=None):
        super(Widget, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            x_main, y_main = self.geometry().x(), self.geometry().y()
            cursor_x, cursor_y = QtGui.QCursor.pos().x(), QtGui.QCursor.pos().y()

            if x_main <= cursor_x <= x_main + self.geometry().width():
                if y_main <= cursor_y <= y_main + self.geometry().height():
                    self.old_pos = event.pos()
                else:
                    self.old_pos = None
        elif event.button() == QtCore.Qt.RightButton:
            self.old_pos = None

    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.old_pos = None

    def mouseMoveEvent(self, event):
        if not self.old_pos:
            return

        try:
                delta = event.pos() - self.old_pos
                self.move(self.pos() + delta)
        except:
                pass