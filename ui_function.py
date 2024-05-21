import os

from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QFileDialog
from PyQt5 import QtWidgets
from pandas.errors import ParserError

from data_processing import DataExtractor, filter_data
from folium_map_generator import FoliumMap


class UiFunction:
    """
    The UiFunction class is responsible for handling the user interface (UI) functionality of the application.
    It includes methods for browsing and opening files, displaying data on a map, and applying filters to the data.
    """
    def __init__(self, ui):
        self.ui = ui
        self.data_extractor = None
        self.min_speed_value = 0
        self.max_speed_value = 0
        self.min_year_value = 0
        self.max_year_value = 0
        self.file_name = None
        self.speed_filter = (10, 110)
        self.year_filter = (2000, 2023)
        self.data_extractor = None
        self.filtered_data = None
        self.filtered_point = []
        self.light_filter = []
        self.road_light_filter = []
        self.crash_severity_filter = []
        self.weather_filter = []

    def browse_file(self):
        """
        Open file browser, to get the directory of dataset file.
        :return: None
        """
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        self.file_name, _ = QFileDialog.getOpenFileName(None, "QFileDialog.getOpenFileName()", "", "All Files (*)",
                                                        options=options)
        if self.file_name:
            self.ui.file_dir_text.setText(self.file_name)

    def open_file(self):
        """
        open dataset file and load the information of the dataset.
        :return: None
        """
        file_path = self.ui.file_dir_text.text()
        try:
            data_extractor = DataExtractor(file_path)
            dataset_info = data_extractor.get_dataset_info()
            self.ui.data_detail_showbox.setPlainText(dataset_info)
            self.data_extractor = DataExtractor(file_path)
            self.filtered_data = self.data_extractor.data
            self.min_speed_value, self.max_speed_value = data_extractor.speed_limit_range()
            self.min_year_value, self.max_year_value = data_extractor.crash_year_range()
            self.ui.min_speed.display(self.min_speed_value)
            self.ui.max_speed.display(self.max_speed_value)
            self.ui.min_year.display(self.min_year_value)
            self.ui.max_year.display(self.max_year_value)
        except ParserError:
            error_dialog = QtWidgets.QMessageBox()
            error_dialog.setWindowTitle("Error")
            error_dialog.setText("Please choose a valid file.")
            error_dialog.setIcon(QtWidgets.QMessageBox.Critical)
            error_dialog.exec_()
        except Exception as e:
            error_dialog = QtWidgets.QMessageBox()
            error_dialog.setWindowTitle("Error")
            error_dialog.setText(f"Please choose a valid file.")
            error_dialog.setIcon(QtWidgets.QMessageBox.Critical)
            error_dialog.exec_()

    def update_speed_value(self, value):
        """
        Update the speed range to the range slide bar indicator.
        :param value: realtime value change of speed range value
        :return: None
        """
        min_value, max_value = value
        self.min_speed_value = (10 + (min_value / 99) * 100) // 10 * 10
        self.max_speed_value = (10 + (max_value / 99) * 100) // 10 * 10
        self.ui.min_speed.display(self.min_speed_value)
        self.ui.max_speed.display(self.max_speed_value)
        self.speed_filter = (self.min_speed_value, self.max_speed_value)

    def update_year_value(self, value):
        """
            Update the year range to the range slide bar indicator.
            :param value: realtime value change of year range value
            :return: None
        """
        min_value, max_value = value
        self.min_year_value = (2000 + (min_value / 99) * 23)
        self.max_year_value = (2000 + (max_value / 99) * 23)
        self.ui.min_year.display(self.min_year_value)
        self.ui.max_year.display(self.max_year_value)
        self.year_filter = (self.min_year_value, self.max_year_value)

    def get_filter_key(self):
        """
        Base on the checkboxes, get all filter keys. all information list below.
        {'crashSeverity': ['Serious Crash', 'Non-Injury Crash', 'Minor Crash', 'Fatal Crash'],
        'crashYear': [2012, 2011, 2013, 2014, 2015, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010,
                      2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023],
        'light': ['Bright sun', 'Dark', 'Overcast', 'Twilight', 'Unknown'],
        'speedLimit': [50.0, 80.0, 70.0, 100.0, 60.0, 40.0, 30.0, 20.0, 10.0, nan, 110.0, 90.0],
        'streetLight': ['Null', 'On', 'Off', nan],
        'weatherA': ['Fine', 'Heavy rain', 'Light rain', 'Snow', 'Mist or Fog', 'Null', 'Hail or Sleet']}

        :return:
        """
        light_checkboxes = [self.ui.bright_sun_box, self.ui.dark_box,
                            self.ui.overcast_box, self.ui.twilight_box, self.ui.light_unknown_box]
        road_light_checkboxes = [self.ui.null_box, self.ui.on_box, self.ui.off_box, self.ui.road_light_unknown_box]
        crash_severity_checkboxes = [self.ui.fatal_crash_box, self.ui.serious_crash_box,
                                     self.ui.non_injury_crash_box, self.ui.minor_crash_box, self.ui.fine_box]
        weather_checkboxes = [self.ui.fine_box, self.ui.heavy_rain_box, self.ui.light_rain_box, self.ui.snow_box,
                              self.ui.mist_or_fog_box,
                              self.ui.hail_or_sleet_box, self.ui.weather_unknown_box]
        self.light_filter = [box.text() for box in light_checkboxes if box.isChecked()]
        self.road_light_filter = [box.text() for box in road_light_checkboxes if box.isChecked()]
        self.crash_severity_filter = [box.text() for box in crash_severity_checkboxes if box.isChecked()]
        self.weather_filter = [box.text() for box in weather_checkboxes if box.isChecked()]

    def show_map(self):
        """
        Show every filtered data points on Folium map, and load it to widget.
        :return: None
        """
        cas_map = FoliumMap(self.data_extractor)
        cas_map.add_point(self.filtered_point)
        cas_map.save_map()
        current_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_dir, 'map.html')
        self.ui.map_view.load(QUrl.fromLocalFile(file_path))

    def filter_data_with_all_filters(self):
        """
        filter all data points, base on the filter keys
        :return: None
        """
        # (Y, X), crashSeverity, crashYear, light, speedLimit, streetLight, weatherA
        filtered_data = filter_data(self.filtered_data, 'light', self.light_filter)
        filtered_data = filter_data(filtered_data, 'streetLight', self.road_light_filter)
        filtered_data = filter_data(filtered_data, 'crashSeverity', self.crash_severity_filter)
        filtered_data = filter_data(filtered_data, 'weatherA', self.weather_filter)
        # Filter the data based on the year and speed limit
        # Convert the 'speedLimit' column to int
        filtered_data['speedLimit'] = filtered_data['speedLimit'].astype(float).astype(int)
        filtered_data['crashYear'] = filtered_data['crashYear'].astype(int)
        filtered_data = filtered_data[
            ((filtered_data['crashYear']) >= self.year_filter[0]) & (filtered_data['crashYear'] <= self.year_filter[1])]
        filtered_data = filtered_data[(filtered_data['speedLimit'] >= self.speed_filter[0]) & (
                filtered_data['speedLimit'] <= self.speed_filter[1])]
        self.filtered_point = [(y, x) for y, x in zip(filtered_data['Y'], filtered_data['X'])]

    def start_filter(self):
        """
        Get all filter information and apply the filter to the whole data
        :return: None
        """

        self.get_filter_key()

        try:
            self.filter_data_with_all_filters()
            filter_information = f"after filtered, there are {len(self.filtered_point)} left in all data"
            self.ui.data_detail_showbox.appendPlainText(filter_information)
            self.show_map()

        except:
            error_dialog = QtWidgets.QMessageBox()
            error_dialog.setWindowTitle("Error")
            error_dialog.setText("You didn't open any data.")
            error_dialog.setIcon(QtWidgets.QMessageBox.Critical)
            error_dialog.exec_()
