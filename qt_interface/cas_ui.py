# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt_interface/untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(759, 586)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.tab)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.choose_file_button = QtWidgets.QPushButton(self.tab)
        self.choose_file_button.setObjectName("choose_file_button")
        self.horizontalLayout.addWidget(self.choose_file_button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.open_file_button = QtWidgets.QPushButton(self.tab)
        self.open_file_button.setObjectName("open_file_button")
        self.horizontalLayout_3.addWidget(self.open_file_button)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.tab)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.horizontalLayout_4.addWidget(self.plainTextEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.line = QtWidgets.QFrame(self.tab)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.verticalLayout_12.addLayout(self.verticalLayout_2)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.checkBox_7 = QtWidgets.QCheckBox(self.tab)
        self.checkBox_7.setObjectName("checkBox_7")
        self.verticalLayout_3.addWidget(self.checkBox_7)
        self.checkBox_8 = QtWidgets.QCheckBox(self.tab)
        self.checkBox_8.setObjectName("checkBox_8")
        self.verticalLayout_3.addWidget(self.checkBox_8)
        self.checkBox_6 = QtWidgets.QCheckBox(self.tab)
        self.checkBox_6.setObjectName("checkBox_6")
        self.verticalLayout_3.addWidget(self.checkBox_6)
        self.checkBox_5 = QtWidgets.QCheckBox(self.tab)
        self.checkBox_5.setObjectName("checkBox_5")
        self.verticalLayout_3.addWidget(self.checkBox_5)
        self.checkBox_9 = QtWidgets.QCheckBox(self.tab)
        self.checkBox_9.setObjectName("checkBox_9")
        self.verticalLayout_3.addWidget(self.checkBox_9)
        self.horizontalLayout_6.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_4.addWidget(self.label_5)
        self.checkBox_12 = QtWidgets.QCheckBox(self.tab)
        self.checkBox_12.setObjectName("checkBox_12")
        self.verticalLayout_4.addWidget(self.checkBox_12)
        self.checkBox_13 = QtWidgets.QCheckBox(self.tab)
        self.checkBox_13.setObjectName("checkBox_13")
        self.verticalLayout_4.addWidget(self.checkBox_13)
        self.checkBox_11 = QtWidgets.QCheckBox(self.tab)
        self.checkBox_11.setObjectName("checkBox_11")
        self.verticalLayout_4.addWidget(self.checkBox_11)
        self.checkBox_10 = QtWidgets.QCheckBox(self.tab)
        self.checkBox_10.setObjectName("checkBox_10")
        self.verticalLayout_4.addWidget(self.checkBox_10)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem1)
        self.horizontalLayout_6.addLayout(self.verticalLayout_4)
        self.verticalLayout_9.addLayout(self.horizontalLayout_6)
        self.line_3 = QtWidgets.QFrame(self.tab)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_9.addWidget(self.line_3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_6.addWidget(self.label_3)
        self.checkBox_4 = QtWidgets.QCheckBox(self.tab)
        self.checkBox_4.setObjectName("checkBox_4")
        self.verticalLayout_6.addWidget(self.checkBox_4)
        self.checkBox = QtWidgets.QCheckBox(self.tab)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout_6.addWidget(self.checkBox)
        self.checkBox_2 = QtWidgets.QCheckBox(self.tab)
        self.checkBox_2.setObjectName("checkBox_2")
        self.verticalLayout_6.addWidget(self.checkBox_2)
        self.checkBox_3 = QtWidgets.QCheckBox(self.tab)
        self.checkBox_3.setObjectName("checkBox_3")
        self.verticalLayout_6.addWidget(self.checkBox_3)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem2)
        self.horizontalLayout_5.addLayout(self.verticalLayout_6)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_5.addWidget(self.label_6)
        self.checkBox_18 = QtWidgets.QCheckBox(self.tab)
        self.checkBox_18.setObjectName("checkBox_18")
        self.verticalLayout_5.addWidget(self.checkBox_18)
        self.checkBox_15 = QtWidgets.QCheckBox(self.tab)
        self.checkBox_15.setObjectName("checkBox_15")
        self.verticalLayout_5.addWidget(self.checkBox_15)
        self.checkBox_14 = QtWidgets.QCheckBox(self.tab)
        self.checkBox_14.setObjectName("checkBox_14")
        self.verticalLayout_5.addWidget(self.checkBox_14)
        self.checkBox_17 = QtWidgets.QCheckBox(self.tab)
        self.checkBox_17.setObjectName("checkBox_17")
        self.verticalLayout_5.addWidget(self.checkBox_17)
        self.checkBox_16 = QtWidgets.QCheckBox(self.tab)
        self.checkBox_16.setObjectName("checkBox_16")
        self.verticalLayout_5.addWidget(self.checkBox_16)
        self.checkBox_19 = QtWidgets.QCheckBox(self.tab)
        self.checkBox_19.setObjectName("checkBox_19")
        self.verticalLayout_5.addWidget(self.checkBox_19)
        self.checkBox_20 = QtWidgets.QCheckBox(self.tab)
        self.checkBox_20.setObjectName("checkBox_20")
        self.verticalLayout_5.addWidget(self.checkBox_20)
        self.horizontalLayout_5.addLayout(self.verticalLayout_5)
        self.verticalLayout_9.addLayout(self.horizontalLayout_5)
        self.verticalLayout_11.addLayout(self.verticalLayout_9)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_8.addWidget(self.label_2)
        self.speed_slider = QtWidgets.QSlider(self.tab)
        self.speed_slider.setOrientation(QtCore.Qt.Horizontal)
        self.speed_slider.setObjectName("speed_slider")
        self.verticalLayout_8.addWidget(self.speed_slider)
        self.verticalLayout_10.addLayout(self.verticalLayout_8)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setObjectName("label")
        self.verticalLayout_7.addWidget(self.label)
        self.year_slider = QRangeSlider(self.tab)
        self.year_slider.setOrientation(QtCore.Qt.Horizontal)
        self.year_slider.setObjectName("year_slider")
        self.verticalLayout_7.addWidget(self.year_slider)
        self.verticalLayout_10.addLayout(self.verticalLayout_7)
        self.verticalLayout_11.addLayout(self.verticalLayout_10)
        self.horizontalLayout_7.addLayout(self.verticalLayout_11)
        self.line_2 = QtWidgets.QFrame(self.tab)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_7.addWidget(self.line_2)
        self.widget = QWebEngineView(self.tab)
        self.widget.setObjectName("widget")
        self.horizontalLayout_7.addWidget(self.widget)
        self.horizontalLayout_7.setStretch(2, 9)
        self.verticalLayout_12.addLayout(self.horizontalLayout_7)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.horizontalLayout_2.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.choose_file_button.setText(_translate("MainWindow", "Choose file"))
        self.open_file_button.setText(_translate("MainWindow", "Open file"))
        self.plainTextEdit.setPlainText(_translate("MainWindow", "The detail of the data will be shown here"))
        self.label_4.setText(_translate("MainWindow", "Light"))
        self.checkBox_7.setText(_translate("MainWindow", "Bright sun"))
        self.checkBox_8.setText(_translate("MainWindow", "Dark"))
        self.checkBox_6.setText(_translate("MainWindow", "Overcast"))
        self.checkBox_5.setText(_translate("MainWindow", "Twilight"))
        self.checkBox_9.setText(_translate("MainWindow", "Unknown"))
        self.label_5.setText(_translate("MainWindow", "Road light"))
        self.checkBox_12.setText(_translate("MainWindow", "Null"))
        self.checkBox_13.setText(_translate("MainWindow", "On"))
        self.checkBox_11.setText(_translate("MainWindow", "Off"))
        self.checkBox_10.setText(_translate("MainWindow", "Unknown"))
        self.label_3.setText(_translate("MainWindow", "Crash severity"))
        self.checkBox_4.setText(_translate("MainWindow", "Fatal Crash"))
        self.checkBox.setText(_translate("MainWindow", "Serious Crash"))
        self.checkBox_2.setText(_translate("MainWindow", "Non-Injury Crash"))
        self.checkBox_3.setText(_translate("MainWindow", "Minor Crash"))
        self.label_6.setText(_translate("MainWindow", "Weather"))
        self.checkBox_18.setText(_translate("MainWindow", "Fine"))
        self.checkBox_15.setText(_translate("MainWindow", "Heavy rain"))
        self.checkBox_14.setText(_translate("MainWindow", "Light rain"))
        self.checkBox_17.setText(_translate("MainWindow", "Snow"))
        self.checkBox_16.setText(_translate("MainWindow", "Mist or Fog"))
        self.checkBox_19.setText(_translate("MainWindow", "Hail or Sleet"))
        self.checkBox_20.setText(_translate("MainWindow", "Unknown"))
        self.label_2.setText(_translate("MainWindow", "Speed limit"))
        self.label.setText(_translate("MainWindow", "Crash year"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
from qtrangeslider import QRangeSlider
from PyQt5.QtWebEngineWidgets import QWebEngineView


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())