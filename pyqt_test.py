import os
import sys

import numpy as np
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QPushButton, QFileDialog, QMainWindow, QApplication, QVBoxLayout, QWidget
import folium

from csv_information_extractor import CSVDataExtractor


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Folium map in PyQt')

        # Create a QPushButton
        self.button = QPushButton('Import CSV', self)
        self.button.clicked.connect(self.import_csv)

        # Create a QWebEngineView widget
        self.view = QWebEngineView()

        # Create a QVBoxLayout
        layout = QVBoxLayout()

        # Add the button and the view to the layout
        layout.addWidget(self.button)
        layout.addWidget(self.view)

        # Create a central widget for the main window and set the layout
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def import_csv(self):
        # Open a QFileDialog to select a CSV file
        file_path, _ = QFileDialog.getOpenFileName(self, 'Open CSV file', '', 'CSV files (*.csv)')

        if file_path:
            # Use the CSVDataExtractor class to extract the points from the CSV file
            data_extractor = CSVDataExtractor(file_path)
            points = data_extractor.get_yx_tuples()

            # Clear the existing markers from the map
            for marker in self.m.get_root().find_all('CircleMarker'):
                self.m.get_root().remove_child(marker)

            # Add new markers for each point in the CSV file
            for point in points:
                folium.CircleMarker(point, radius=1).add_to(self.m)

            # Save the map as an HTML file and load it in the QWebEngineView widget
            self.m.save('map.html')
            self.view.load(QUrl.fromLocalFile(os.path.abspath('map.html')))


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Create a MainWindow instance
    window = MainWindow()

    # Show the window
    window.show()

    # Run the application
    sys.exit(app.exec_())