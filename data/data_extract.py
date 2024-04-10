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
        self.file_path = file_path
        self.data = pd.read_csv(file_path)

    def get_max_min_values(self):
        y_max = self.data['Y'].max()
        y_min = self.data['Y'].min()
        x_max = self.data['X'].max()
        x_min = self.data['X'].min()

        return {'Y': (y_min, y_max), 'X': (x_min, x_max)}

    def get_selected_fields(self):
        selected_fields = ['Y', 'X', 'crashSeverity', 'crashYear', 'light', 'speedLimit', 'streetLight', 'weatherA']
        selected_data = self.data[selected_fields]
        return selected_data.to_dict('records')

    def get_unique_values(self):
        fields = ['crashSeverity', 'crashYear', 'light', 'speedLimit', 'streetLight', 'weatherA']
        unique_values = {field: self.data[field].unique().tolist() for field in fields}
        return unique_values


if __name__ == '__main__':
    data_extractor = DataExtractor('CHCH_CAS_Data.csv')
    # print(data_extractor.get_max_min_values())
    # print(data_extractor.get_selected_fields()[:5])
    print(data_extractor.get_unique_values())