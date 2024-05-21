import folium
import os
from data_processing import DataExtractor


class FoliumMap:
    def __init__(self, data_extractor):
        """
        generate the map of Christchurch and set the move limitation.
        :param data_extractor: dataset
        """
        self.data_extractor = data_extractor
        buffer = 0.1
        min_lon, max_lon = self.data_extractor.get_max_min_coordinate()['X']
        min_lat, max_lat = self.data_extractor.get_max_min_coordinate()['Y']
        # Add a buffer to the min and max values
        min_lon -= buffer
        max_lon += buffer
        min_lat -= buffer
        max_lat += buffer

        self.m = folium.Map(
            max_bounds=True,
            location=(-43.53, 172.63),
            min_lat=min_lat,
            max_lat=max_lat,
            min_lon=min_lon,
            max_lon=max_lon,
        )

        # add four circles markers to the map base on the min and max values of the X and Y columns
        folium.CircleMarker((max_lat, min_lon), tooltip="Upper Left Corner").add_to(self.m)
        folium.CircleMarker((min_lat, min_lon), tooltip="Lower Left Corner").add_to(self.m)
        folium.CircleMarker((min_lat, max_lon), tooltip="Lower Right Corner").add_to(self.m)
        folium.CircleMarker((max_lat, max_lon), tooltip="Upper Right Corner").add_to(self.m)

    def add_point(self, point_list):
        """
        add the point to the map, base on the point list
        :param point_list: point list
        :return: None
        """
        for point in point_list:
            folium.CircleMarker(point, radius=4).add_to(self.m)

    def save_map(self):
        """
        save map to html file
        :return: None
        """
        root_dir = os.path.dirname(os.path.abspath(__file__))  # get the project root directory
        map_path = os.path.join(root_dir, 'map.html')  # create the full path
        self.m.save(map_path)  # save the map to the root directory
