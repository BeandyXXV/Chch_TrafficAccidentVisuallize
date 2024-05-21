# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt_interface/cas_ui_design.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5 import QtWebEngineWidgets
from qtrangeslider import QRangeSlider

from ui_function import UiFunction


class Ui_MainWindow(object):

    def __init__(self):
        self.ui_function = UiFunction(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.map_show_tab = QtWidgets.QWidget()
        self.map_show_tab.setObjectName("map_show_tab")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.map_show_tab)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout()
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.file_dir_text = QtWidgets.QLineEdit(self.map_show_tab)
        self.file_dir_text.setObjectName("file_dir_text")
        self.horizontalLayout.addWidget(self.file_dir_text)
        self.choose_file_button = QtWidgets.QPushButton(self.map_show_tab)
        self.choose_file_button.setObjectName("choose_file_button")
        self.choose_file_button.clicked.connect(self.ui_function.browse_file)
        self.horizontalLayout.addWidget(self.choose_file_button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.open_file_button = QtWidgets.QPushButton(self.map_show_tab)
        self.open_file_button.setObjectName("open_file_button")
        self.open_file_button.clicked.connect(self.ui_function.open_file)
        self.verticalLayout.addWidget(self.open_file_button)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.data_detail_showbox = QtWidgets.QPlainTextEdit(self.map_show_tab)
        self.data_detail_showbox.setObjectName("data_detail_showbox")
        self.horizontalLayout_4.addWidget(self.data_detail_showbox)
        self.verticalLayout_13.addLayout(self.horizontalLayout_4)
        self.line = QtWidgets.QFrame(self.map_show_tab)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_13.addWidget(self.line)
        self.verticalLayout_14.addLayout(self.verticalLayout_13)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.light_select_label = QtWidgets.QLabel(self.map_show_tab)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.light_select_label.setFont(font)
        self.light_select_label.setObjectName("light_select_label")
        self.verticalLayout_3.addWidget(self.light_select_label)
        self.bright_sun_box = QtWidgets.QCheckBox(self.map_show_tab)
        self.bright_sun_box.setObjectName("bright_sun_box")
        self.verticalLayout_3.addWidget(self.bright_sun_box)
        self.dark_box = QtWidgets.QCheckBox(self.map_show_tab)
        self.dark_box.setObjectName("dark_box")
        self.verticalLayout_3.addWidget(self.dark_box)
        self.overcast_box = QtWidgets.QCheckBox(self.map_show_tab)
        self.overcast_box.setObjectName("overcast_box")
        self.verticalLayout_3.addWidget(self.overcast_box)
        self.twilight_box = QtWidgets.QCheckBox(self.map_show_tab)
        self.twilight_box.setObjectName("twilight_box")
        self.verticalLayout_3.addWidget(self.twilight_box)
        self.light_unknown_box = QtWidgets.QCheckBox(self.map_show_tab)
        self.light_unknown_box.setObjectName("light_unknown_box")
        self.verticalLayout_3.addWidget(self.light_unknown_box)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.horizontalLayout_6.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.road_light_select_label = QtWidgets.QLabel(self.map_show_tab)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.road_light_select_label.setFont(font)
        self.road_light_select_label.setObjectName("road_light_select_label")
        self.verticalLayout_4.addWidget(self.road_light_select_label)
        self.null_box = QtWidgets.QCheckBox(self.map_show_tab)
        self.null_box.setObjectName("null_box")
        self.verticalLayout_4.addWidget(self.null_box)
        self.on_box = QtWidgets.QCheckBox(self.map_show_tab)
        self.on_box.setObjectName("on_box")
        self.verticalLayout_4.addWidget(self.on_box)
        self.off_box = QtWidgets.QCheckBox(self.map_show_tab)
        self.off_box.setObjectName("off_box")
        self.verticalLayout_4.addWidget(self.off_box)
        self.road_light_unknown_box = QtWidgets.QCheckBox(self.map_show_tab)
        self.road_light_unknown_box.setObjectName("road_light_unknown_box")
        self.verticalLayout_4.addWidget(self.road_light_unknown_box)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem1)
        self.horizontalLayout_6.addLayout(self.verticalLayout_4)
        self.verticalLayout_9.addLayout(self.horizontalLayout_6)
        self.line_3 = QtWidgets.QFrame(self.map_show_tab)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_9.addWidget(self.line_3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.crash_severity_select_label = QtWidgets.QLabel(self.map_show_tab)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.crash_severity_select_label.setFont(font)
        self.crash_severity_select_label.setObjectName("crash_severity_select_label")
        self.verticalLayout_6.addWidget(self.crash_severity_select_label)
        self.fatal_crash_box = QtWidgets.QCheckBox(self.map_show_tab)
        self.fatal_crash_box.setObjectName("fatal_crash_box")
        self.verticalLayout_6.addWidget(self.fatal_crash_box)
        self.serious_crash_box = QtWidgets.QCheckBox(self.map_show_tab)
        self.serious_crash_box.setObjectName("serious_crash_box")
        self.verticalLayout_6.addWidget(self.serious_crash_box)
        self.non_injury_crash_box = QtWidgets.QCheckBox(self.map_show_tab)
        self.non_injury_crash_box.setObjectName("non_injury_crash_box")
        self.verticalLayout_6.addWidget(self.non_injury_crash_box)
        self.minor_crash_box = QtWidgets.QCheckBox(self.map_show_tab)
        self.minor_crash_box.setObjectName("minor_crash_box")
        self.verticalLayout_6.addWidget(self.minor_crash_box)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem2)
        self.horizontalLayout_5.addLayout(self.verticalLayout_6)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.weather_select_label = QtWidgets.QLabel(self.map_show_tab)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.weather_select_label.setFont(font)
        self.weather_select_label.setObjectName("weather_select_label")
        self.verticalLayout_5.addWidget(self.weather_select_label)
        self.fine_box = QtWidgets.QCheckBox(self.map_show_tab)
        self.fine_box.setObjectName("fine_box")
        self.verticalLayout_5.addWidget(self.fine_box)
        self.heavy_rain_box = QtWidgets.QCheckBox(self.map_show_tab)
        self.heavy_rain_box.setObjectName("heavy_rain_box")
        self.verticalLayout_5.addWidget(self.heavy_rain_box)
        self.light_rain_box = QtWidgets.QCheckBox(self.map_show_tab)
        self.light_rain_box.setObjectName("light_rain_box")
        self.verticalLayout_5.addWidget(self.light_rain_box)
        self.snow_box = QtWidgets.QCheckBox(self.map_show_tab)
        self.snow_box.setObjectName("snow_box")
        self.verticalLayout_5.addWidget(self.snow_box)
        self.mist_or_fog_box = QtWidgets.QCheckBox(self.map_show_tab)
        self.mist_or_fog_box.setObjectName("mist_or_fog_box")
        self.verticalLayout_5.addWidget(self.mist_or_fog_box)
        self.hail_or_sleet_box = QtWidgets.QCheckBox(self.map_show_tab)
        self.hail_or_sleet_box.setObjectName("hail_or_sleet_box")
        self.verticalLayout_5.addWidget(self.hail_or_sleet_box)
        self.weather_unknown_box = QtWidgets.QCheckBox(self.map_show_tab)
        self.weather_unknown_box.setObjectName("weather_unknown_box")
        self.verticalLayout_5.addWidget(self.weather_unknown_box)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem3)
        self.horizontalLayout_5.addLayout(self.verticalLayout_5)
        self.verticalLayout_9.addLayout(self.horizontalLayout_5)
        self.verticalLayout_11.addLayout(self.verticalLayout_9)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_2 = QtWidgets.QLabel(self.map_show_tab)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_7.addWidget(self.label_2)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.map_show_tab)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.min_speed = QtWidgets.QLCDNumber(self.map_show_tab)
        self.min_speed.setObjectName("min_speed")
        self.min_speed.display(0)
        self.horizontalLayout_3.addWidget(self.min_speed)
        self.label_4 = QtWidgets.QLabel(self.map_show_tab)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.max_speed = QtWidgets.QLCDNumber(self.map_show_tab)
        self.max_speed.setObjectName("max_speed")
        self.max_speed.display(0)
        self.horizontalLayout_3.addWidget(self.max_speed)
        self.label_5 = QtWidgets.QLabel(self.map_show_tab)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.speed_slider = QRangeSlider(self.map_show_tab)
        self.speed_slider.setOrientation(QtCore.Qt.Horizontal)
        self.speed_slider.setObjectName("speed_slider")
        self.speed_slider.setValue((0, 99))
        self.speed_slider.valueChanged.connect(self.ui_function.update_speed_value)
        self.verticalLayout_2.addWidget(self.speed_slider)
        self.verticalLayout_8.addLayout(self.verticalLayout_2)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label = QtWidgets.QLabel(self.map_show_tab)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_10.addWidget(self.label)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem5)
        self.label_6 = QtWidgets.QLabel(self.map_show_tab)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_9.addWidget(self.label_6)
        self.min_year = QtWidgets.QLCDNumber(self.map_show_tab)
        self.min_year.setObjectName("min_year")
        self.min_year.display(0)
        self.horizontalLayout_9.addWidget(self.min_year)
        self.label_7 = QtWidgets.QLabel(self.map_show_tab)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_9.addWidget(self.label_7)
        self.max_year = QtWidgets.QLCDNumber(self.map_show_tab)
        self.max_year.setObjectName("max_year")
        self.max_year.display(0)
        self.horizontalLayout_9.addWidget(self.max_year)
        self.horizontalLayout_10.addLayout(self.horizontalLayout_9)
        self.verticalLayout_7.addLayout(self.horizontalLayout_10)
        self.year_slider = QRangeSlider(self.map_show_tab)
        self.year_slider.setOrientation(QtCore.Qt.Horizontal)
        self.year_slider.setValue((0, 99))
        self.year_slider.setObjectName("year_slider")
        self.year_slider.valueChanged.connect(self.ui_function.update_year_value)
        self.verticalLayout_7.addWidget(self.year_slider)
        self.verticalLayout_8.addLayout(self.verticalLayout_7)
        self.verticalLayout_10.addLayout(self.verticalLayout_8)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem6)
        self.show_map_button = QtWidgets.QPushButton(self.map_show_tab)
        self.show_map_button.setObjectName("show_map_button")
        self.show_map_button.clicked.connect(self.ui_function.start_filter)
        self.verticalLayout_10.addWidget(self.show_map_button)
        self.verticalLayout_11.addLayout(self.verticalLayout_10)
        self.horizontalLayout_11.addLayout(self.verticalLayout_11)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.line_2 = QtWidgets.QFrame(self.map_show_tab)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_2.addWidget(self.line_2)
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.map_view = QtWebEngineWidgets.QWebEngineView(self.map_show_tab)
        self.map_view.setObjectName("map_view")
        self.verticalLayout_12.addWidget(self.map_view)
        self.horizontalLayout_2.addLayout(self.verticalLayout_12)
        self.horizontalLayout_11.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_11.setStretch(0, 1)
        self.horizontalLayout_11.setStretch(1, 10)
        self.verticalLayout_14.addLayout(self.horizontalLayout_11)
        self.verticalLayout_14.setStretch(0, 1)
        self.verticalLayout_14.setStretch(1, 10)
        self.horizontalLayout_12.addLayout(self.verticalLayout_14)
        self.tabWidget.addTab(self.map_show_tab, "")
        self.horizontalLayout_8.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Set the default state of the checkboxes
        self.bright_sun_box.setChecked(True)
        self.dark_box.setChecked(True)
        self.overcast_box.setChecked(True)
        self.twilight_box.setChecked(True)
        self.light_unknown_box.setChecked(True)
        self.null_box.setChecked(True)
        self.on_box.setChecked(True)
        self.off_box.setChecked(True)
        self.road_light_unknown_box.setChecked(True)
        self.fatal_crash_box.setChecked(True)
        self.serious_crash_box.setChecked(True)
        self.non_injury_crash_box.setChecked(True)
        self.minor_crash_box.setChecked(True)
        self.fine_box.setChecked(True)
        self.heavy_rain_box.setChecked(True)
        self.light_rain_box.setChecked(True)
        self.snow_box.setChecked(True)
        self.mist_or_fog_box.setChecked(True)
        self.hail_or_sleet_box.setChecked(True)
        self.weather_unknown_box.setChecked(True)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.choose_file_button.setText(_translate("MainWindow", "Choose file"))
        self.open_file_button.setText(_translate("MainWindow", "Open file"))
        self.data_detail_showbox.setPlainText(_translate("MainWindow", "The detail of the data will be shown here"))
        self.light_select_label.setText(_translate("MainWindow", "Light"))
        self.bright_sun_box.setText(_translate("MainWindow", "Bright sun"))
        self.dark_box.setText(_translate("MainWindow", "Dark"))
        self.overcast_box.setText(_translate("MainWindow", "Overcast"))
        self.twilight_box.setText(_translate("MainWindow", "Twilight"))
        self.light_unknown_box.setText(_translate("MainWindow", "Unknown"))
        self.road_light_select_label.setText(_translate("MainWindow", "Road light"))
        self.null_box.setText(_translate("MainWindow", "Null"))
        self.on_box.setText(_translate("MainWindow", "On"))
        self.off_box.setText(_translate("MainWindow", "Off"))
        self.road_light_unknown_box.setText(_translate("MainWindow", "Unknown"))
        self.crash_severity_select_label.setText(_translate("MainWindow", "Crash severity"))
        self.fatal_crash_box.setText(_translate("MainWindow", "Fatal Crash"))
        self.serious_crash_box.setText(_translate("MainWindow", "Serious Crash"))
        self.non_injury_crash_box.setText(_translate("MainWindow", "Non-Injury Crash"))
        self.minor_crash_box.setText(_translate("MainWindow", "Minor Crash"))
        self.weather_select_label.setText(_translate("MainWindow", "Weather"))
        self.fine_box.setText(_translate("MainWindow", "Fine"))
        self.heavy_rain_box.setText(_translate("MainWindow", "Heavy rain"))
        self.light_rain_box.setText(_translate("MainWindow", "Light rain"))
        self.snow_box.setText(_translate("MainWindow", "Snow"))
        self.mist_or_fog_box.setText(_translate("MainWindow", "Mist or Fog"))
        self.hail_or_sleet_box.setText(_translate("MainWindow", "Hail or Sleet"))
        self.weather_unknown_box.setText(_translate("MainWindow", "Unknown"))
        self.label_2.setText(_translate("MainWindow", "Speed limit:"))
        self.label_3.setText(_translate("MainWindow", "From"))
        self.label_4.setText(_translate("MainWindow", "to"))
        self.label_5.setText(_translate("MainWindow", "km/h"))
        self.label.setText(_translate("MainWindow", "Crash year:"))
        self.label_6.setText(_translate("MainWindow", "From"))
        self.label_7.setText(_translate("MainWindow", "to"))
        self.show_map_button.setText(_translate("MainWindow", "Show map"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.map_show_tab), _translate("MainWindow", "MapShow"))

