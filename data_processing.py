# X, Y, OBJECTID, advisorySpeed, areaUnitID, bicycle, bridge, bus,
# carStationWagon, cliffBank, crashDirectionDescription, crashFinancialYear,
# crashLocation1, crashLocation2, crashRoadSideRoad, crashSeverity,
# crashSHDescription, crashYear, debris, directionRoleDescription, ditch,
# fatalCount, fence, flatHill, guardRail, holiday, houseOrBuilding,
# intersection, kerb, light, meshblockId, minorInjuryCount, moped, motorcycle,
# NumberOfLanes, objectThrownOrDropped, otherObject, otherVehicleType, overBank,
# parkedVehicle, pedestrian, phoneBoxEtc, postOrPole, region, roadCharacter,
# roadLane, roadSurface, roadworks, schoolBus, seriousInjuryCount, slipOrFlood,
# speedLimit, strayAnimal, streetLight, suv, taxi, temporarySpeedLimit, tlaId,
# tlaName, trafficControl, trafficIsland, trafficSign, train, tree, truck,
# unknownVehicleType, urban, vanOrUtility, vehicle, waterRiver, weatherA, weatherB
import pandas as pd


# (Y, X), crashSeverity, crashYear, light, speedLimit, streetLight, weatherA

# class extract_data for the function which relative to data extraction from csv file


class DataExtractor:
    def __init__(self, file_path):
        """
            The DataExtractor class is responsible for extracting and processing data from a given CSV file.

            Attributes:
                file_path (str): The path to the CSV file to be processed.
                data (DataFrame): The data extracted from the CSV file.
        """
        self.file_path = file_path
        self.data = pd.read_csv(file_path)

    def get_max_min_coordinate(self):
        """
        get the min and max coordinate from whole data points
        :return: None
        """
        y_max = self.data['Y'].max()
        y_min = self.data['Y'].min()
        x_max = self.data['X'].max()
        x_min = self.data['X'].min()

        return {'Y': (y_min, y_max), 'X': (x_min, x_max)}

    def get_dataset_info(self):
        """
        get the basic information of the dataset.
        :return: None
        """
        min_year = self.data['crashYear'].min()
        max_year = self.data['crashYear'].max()
        total_count = self.data['crashYear'].count()

        return f"The dataset contains {total_count} data points, spanning from {min_year} to {max_year}"

    def get_selected_fields(self):
        """
        pick the useful information from the dataset.
        :return: None
        """
        selected_fields = ['Y', 'X', 'crashSeverity', 'crashYear', 'light', 'speedLimit', 'streetLight', 'weatherA']
        selected_data = self.data[selected_fields]
        return selected_data.to_dict('records')

    def get_unique_values(self):
        """
        get the unique values from each fields.
        :return: None
        """
        fields = ['crashSeverity', 'crashYear', 'light', 'speedLimit', 'streetLight', 'weatherA']
        unique_values = {field: self.data[field].unique().tolist() for field in fields}
        return unique_values

    def speed_limit_range(self):
        """
        get the speed limit range from whole dataset.
        :return: None
        """
        speed_limit_min = self.data['speedLimit'].min()
        speed_limit_max = self.data['speedLimit'].max()
        return speed_limit_min, speed_limit_max

    def crash_year_range(self):
        """
        get the crash year range from whole dataset
        :return: None
        """
        crash_year_min = self.data['crashYear'].min()
        crash_year_max = self.data['crashYear'].max()
        return crash_year_min, crash_year_max


def replace_null_with_unknown(file_path):
    """
    replace every null value to unknown
    :param file_path: csv file path
    :return: None
    """
    # Load the data from the CSV file
    data = pd.read_csv(file_path)

    # Replace 'Null' with 'Unknown' in the 'weatherA' column
    data['speedLimit'] = data['speedLimit'].replace('Unknown', '0')

    # Write the modified data back to the CSV file
    data.to_csv(file_path, index=False)


def replace_nan_with_unknown(file_path):
    """
        replace every nan value to unknown
        :param file_path: csv file path
        :return: None
    """
    # Load the data from the CSV file
    data = pd.read_csv(file_path)

    # Replace NaN with 'Unknown' in all columns
    data = data.fillna('Unknown')

    # Write the modified data back to the CSV file
    data.to_csv(file_path, index=False)


def filter_data(data_frame, column_name, filter_list):
    """
    base on filter list, filter the data by column name
    :param data_frame: pandas data frame
    :param column_name: column name of the filter data
    :param filter_list: filter key list
    :return: the data after filtered
    """
    filtered_data = data_frame[data_frame[column_name].isin(filter_list)]
    return filtered_data


if __name__ == '__main__':
    data_extractor = DataExtractor('CHCH_CAS_Data.csv')
    # print(data_extractor.get_max_min_values())
    # print(data_extractor.get_selected_fields()[:5])
    print(data_extractor.get_unique_values())
    # print(data_extractor.get_dataset_info())
    # twilight_data = filter_data(data_extractor.data, 'light', ['Twilight'])
    # twilight_data = filter_data(twilight_data, 'weatherA', ['Fine'])
    # filtered_point = [(y, x) for y, x in zip(twilight_data['Y'], twilight_data['X'])]
    # print(filtered_point)
    # replace_nan_with_unknown('CHCH_CAS_Data.csv')
    # replace_null_with_unknown('CHCH_CAS_Data.csv')
