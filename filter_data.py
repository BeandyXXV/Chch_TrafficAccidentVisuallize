from csv_information_extractor import CSVDataExtractor

# get the data from the csv file
file_path = 'data/CHCH_CAS_Data.csv'
data_extractor = CSVDataExtractor(file_path)
data_extractor.get_point_data()
point_list = data_extractor.point_list


# filter the point by the key in each dictionary in the point list
def filter_data(point_data, key, value):
    """
    filter the point list by the key in each dictionary in the point list
    :param point_data: list of dictionary
    :param key: key in the dictionary
    :param value: value of the key
    :return: list of dictionary
    """
    return [point for point in point_data if point[key] == value]

# test in if name == main
if __name__ == '__main__':
    # filter the point list by the key in each dictionary in the point list
    # filter the point list by crash_severity
    filtered_list = filter_data(point_list, 'crash_severity', 'Fatal Crash')
    print(filtered_list[:5], len(filtered_list))
    # filter the point list by light
    filtered_list = filter_data(point_list, 'light', 'Dark')
    print(filtered_list[:5], len(filtered_list))
    # filter the point list by weather
    filtered_list = filter_data(point_list, 'weather', 'Fine')
    print(filtered_list[:5], len(filtered_list))
    # filter the point list by crash_year
    filtered_list = filter_data(point_list, 'crash_year', 2000)
    print(filtered_list[:5], len(filtered_list))
    # filter the point list by fatal_count
    filtered_list = filter_data(point_list, 'fatal_count', 1)
    print(filtered_list[:5], len(filtered_list))
    # filter the point list by speed_limit
    filtered_list = filter_data(point_list, 'speed_limit', 50)
    print(filtered_list[:5], len(filtered_list))
    # filter the point list by street_light
    filtered_list = filter_data(point_list, 'street_light', 'No')
    print(filtered_list[:5], len(filtered_list))
