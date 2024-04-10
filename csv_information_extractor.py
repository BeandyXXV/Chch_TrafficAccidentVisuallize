import pandas as pd


class CSVDataExtractor:
    def __init__(self, file_path):
        self.data = pd.read_csv(file_path)
        # point_list storge every point in the csv file
        self.point_list = []

    def get_max(self, column_name):
        return self.data[column_name].max()

    def get_min(self, column_name):
        return self.data[column_name].min()

    def get_min_max(self, column_name):
        return self.get_min(column_name), self.get_max(column_name)

    def get_yx_tuples(self):
        return [(y, x) for y, x in zip(self.data['Y'], self.data['X'])]

    def get_point_data(self):
        """
        from csv_file, get the point data, include location, crash year, fatal count, crash severity, light, speed limit
        streetlight, weather. save it in a dictionary and append it to the point_list
        :return: none
        """
        for i in range(len(self.data)):
            location = (self.data['Y'][i], self.data['X'][i])
            crash_year = self.data['crashYear'][i]
            fatal_count = self.data['fatalCount'][i]
            crash_severity = self.data['crashSeverity'][i]
            light = self.data['light'][i]
            speed_limit = self.data['speedLimit'][i]
            street_light = self.data['streetLight'][i]
            weather = self.data['weatherA'][i]
            point_data = {'location': location, 'crash_year': crash_year, 'fatal_count': fatal_count,
                          'crash_severity': crash_severity, 'light': light, 'speed_limit': speed_limit,
                          'street_light': street_light, 'weather': weather}
            self.point_list.append(point_data)


if __name__ == '__main__':
