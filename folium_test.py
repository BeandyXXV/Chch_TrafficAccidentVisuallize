import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl
import folium
import os

from folium.plugins import MarkerCluster

from csv_information_extractor import CSVDataExtractor

buffer = 0.1  # Adjust this value as needed

# from the csv file, get the min and max values of the X and Y columns
data_extractor = CSVDataExtractor('data/CHCH_CAS_Data.csv')
min_lon, max_lon = data_extractor.get_min_max('X')
min_lat, max_lat = data_extractor.get_min_max('Y')

# Add a buffer to the min and max values
min_lon -= buffer
max_lon += buffer
min_lat -= buffer
max_lat += buffer

# Create a Folium map and save it as an HTML file
m = folium.Map(
    max_bounds=True,
    location=(-43.53, 172.63),
    min_lat=min_lat,
    max_lat=max_lat,
    min_lon=min_lon,
    max_lon=max_lon,
)
marker_cluster = MarkerCluster().add_to(m)

# add four circles markers to the map base on the min and max values of the X and Y columns
folium.CircleMarker((max_lat, min_lon), tooltip="Upper Left Corner").add_to(m)
folium.CircleMarker((min_lat, min_lon), tooltip="Lower Left Corner").add_to(m)
folium.CircleMarker((min_lat, max_lon), tooltip="Lower Right Corner").add_to(m)
folium.CircleMarker((max_lat, max_lon), tooltip="Upper Right Corner").add_to(m)

# Get all the points from the CSV file
points = data_extractor.get_yx_tuples()

# Iterate over the points and add each one to the map
for point in points:
    folium.CircleMarker(point, radius=1).add_to(m)
    folium.CircleMarker(point, radius=1).add_to(marker_cluster)

m.save('map.html')

# Create a PyQt application
app = QApplication(sys.argv)

# Create a window
window = QMainWindow()
window.setWindowTitle('Folium map in PyQt')

# Create a QWebEngineView widget
view = QWebEngineView()

# Load the Folium map HTML file
file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "map.html"))
view.load(QUrl.fromLocalFile(file_path))

# Set the QWebEngineView widget as the central widget of the window
window.setCentralWidget(view)

# Show the window
window.show()

# Run the application
sys.exit(app.exec_())
