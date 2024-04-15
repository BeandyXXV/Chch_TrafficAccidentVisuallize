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
def filter_data(data_frame, column_name, filter_list):
    filtered_data = data_frame[data_frame[column_name].isin(filter_list)]
    return filtered_data


class DataExtractor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = pd.read_csv(file_path)

    def get_max_min_coordinate(self):
        y_max = self.data['Y'].max()
        y_min = self.data['Y'].min()
        x_max = self.data['X'].max()
        x_min = self.data['X'].min()

        return {'Y': (y_min, y_max), 'X': (x_min, x_max)}

    def get_dataset_info(self):
        min_year = self.data['crashYear'].min()
        max_year = self.data['crashYear'].max()
        total_count = self.data['crashYear'].count()

        return f"The dataset contains {total_count} data points, spanning from {min_year} to {max_year}"

    def get_selected_fields(self):
        selected_fields = ['Y', 'X', 'crashSeverity', 'crashYear', 'light', 'speedLimit', 'streetLight', 'weatherA']
        selected_data = self.data[selected_fields]
        return selected_data.to_dict('records')

    def get_unique_values(self):
        fields = ['crashSeverity', 'crashYear', 'light', 'speedLimit', 'streetLight', 'weatherA']
        unique_values = {field: self.data[field].unique().tolist() for field in fields}
        return unique_values


def replace_null_with_unknown(file_path):
    # Load the data from the CSV file
    data = pd.read_csv(file_path)

    # Replace 'Null' with 'Unknown' in the 'weatherA' column
    data['speedLimit'] = data['speedLimit'].replace('Unknown', '0')

    # Write the modified data back to the CSV file
    data.to_csv(file_path, index=False)


def replace_nan_with_unknown(file_path):
    # Load the data from the CSV file
    data = pd.read_csv(file_path)

    # Replace NaN with 'Unknown' in all columns
    data = data.fillna('Unknown')

    # Write the modified data back to the CSV file
    data.to_csv(file_path, index=False)


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
