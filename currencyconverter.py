
from PyQt5 import QtCore, QtGui, QtWidgets
import requests
import json
import time

# YOU NEED TO PUT YOUR OWN API KEY FROM  https://v6.exchangerate-api.com AT LINE 18 IF YOU WANT TO RUN THE CODE.
# EĞER KODU ÇALIŞTIRMAK İSTERSENİZ KENDİ APİ ANAHTARINIZI 18. SATIRA KOYMAK ZORUNDASINIZ.




class Ui_MainWindow(object):


    def process(self):

        self.api_url = "YOUR-API-KEY"
        self.base = self.base_combobox.currentText()
        self.to = self.to_combobox.currentText()
        self.amount = int(self.amount_money_lineedit.text())
        self.result = requests.get(self.api_url + self.base)
        self.result = json.loads(self.result.text)


        for i in range(465,900,50):
            time.sleep(0.02)
            MainWindow.resize(895, i)
        self.sonuc_labeli.setText("\t{0} {1} ={2} {3}".format(self.amount, self.base, self.amount * self.result['conversion_rates'][self.to],self.to))
        self.sonuc_labeli.setStyleSheet("background-color:white;\n"
                                        "border-radius:20px;\n"
                                        "border:5px solid blue;")








    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(895, 465)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color:#B22222;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 40, 671, 61))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)

        self.label.setFont(font)
        self.label.setStyleSheet("background-color:white;\n"
"border-radius:15px;")
        self.label.setObjectName("label")


        self.base_combobox = QtWidgets.QComboBox(self.centralwidget)
        self.base_combobox.setGeometry(QtCore.QRect(110, 180, 241, 61))
        self.base_combobox.setStyleSheet("background-color:white;")
        self.base_combobox.setObjectName("base_combobox")
        self.base_combobox.addItem("")
        self.base_combobox.setItemText(0, "")
        self.base_combobox.addItem("")
        self.base_combobox.addItem("")
        self.base_combobox.addItem("")
        self.base_combobox.addItem("")


        self.to_combobox = QtWidgets.QComboBox(self.centralwidget)
        self.to_combobox.setGeometry(QtCore.QRect(560, 180, 241, 61))
        self.to_combobox.setStyleSheet("background-color:white;")
        self.to_combobox.setObjectName("to_combobox")
        self.to_combobox.addItem("")
        self.to_combobox.setItemText(0, "")
        self.to_combobox.addItem("")
        self.to_combobox.addItem("")
        self.to_combobox.addItem("")
        self.to_combobox.addItem("")



        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(410, 180, 91, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color:white;\n"
"border-radius:20px;")
        self.label_2.setObjectName("label_2")



        self.amount_money_lineedit = QtWidgets.QLineEdit(self.centralwidget)
        self.amount_money_lineedit.setGeometry(QtCore.QRect(360, 270, 331, 51))
        self.amount_money_lineedit.setStyleSheet("background-color:white;\n"
"border-radius:20px;\n"
"border-bottom: 2px solid blue;")
        self.amount_money_lineedit.setObjectName("amount_money_lineedit")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(210, 270, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)



        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color:white;\n"
"border-radius:20px;")
        self.label_3.setObjectName("label_3")



        self.convert_btn = QtWidgets.QPushButton(self.centralwidget)
        self.convert_btn.setGeometry(QtCore.QRect(310, 350, 251, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.convert_btn.setFont(font)
        self.convert_btn.setStyleSheet("QPushButton#convert_btn{\n"
"background-color:white;\n"
"border-radius:20px;\n"
"border:5px solid gray;\n"
"}\n"
"QPushButton#convert_btn:hover{\n"
"    background-color:gray;\n"
"}\n"
"")
        self.convert_btn.setObjectName("convert_btn")
        self.convert_btn.clicked.connect(self.process)



        self.sonuc_labeli = QtWidgets.QLabel(self.centralwidget)
        self.sonuc_labeli.setGeometry(QtCore.QRect(100, 480, 691, 281))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.sonuc_labeli.setFont(font)
        self.sonuc_labeli.setText("")

        self.sonuc_labeli.setObjectName("sonuc_labeli")




        self.label.raise_()
        self.base_combobox.raise_()
        self.to_combobox.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.amount_money_lineedit.raise_()
        self.convert_btn.raise_()
        self.sonuc_labeli.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Currency Converter"))
        self.label.setText(_translate("MainWindow", "                   CONVERT EXCHANGE RATES"))
        self.base_combobox.setItemText(1, _translate("MainWindow", "TRY"))
        self.base_combobox.setItemText(2, _translate("MainWindow", "USD"))
        self.base_combobox.setItemText(3, _translate("MainWindow", "EUR"))
        self.base_combobox.setItemText(4, _translate("MainWindow", "GBP"))
        self.to_combobox.setItemText(1, _translate("MainWindow", "TRY"))
        self.to_combobox.setItemText(2, _translate("MainWindow", "USD"))
        self.to_combobox.setItemText(3, _translate("MainWindow", "EUR"))
        self.to_combobox.setItemText(4, _translate("MainWindow", "GBP"))
        self.label_2.setText(_translate("MainWindow", "    TO"))
        self.amount_money_lineedit.setPlaceholderText(_translate("MainWindow", "please enter the amount of money you want to convert"))
        self.label_3.setText(_translate("MainWindow", "       AMOUNT:"))
        self.convert_btn.setText(_translate("MainWindow", "CONVERT"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
