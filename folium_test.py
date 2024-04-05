import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl
import folium
import os

# Create a Folium map and save it as an HTML file
m = folium.Map(
    location=(-43.53, 172.63),
    zoom_start=12,
    min_lat=-43.65,
    max_lat=-43.45,
    min_lon=172.45,
    max_lon=172.75,
)
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