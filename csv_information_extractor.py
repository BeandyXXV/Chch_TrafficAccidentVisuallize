import pandas as pd


class CSVDataExtractor:
    def __init__(self, file_path):
        self.data = pd.read_csv(file_path)

    def get_max(self, column_name):
        return self.data[column_name].max()

    def get_min(self, column_name):
        return self.data[column_name].min()

    def get_min_max(self, column_name):
        return self.get_min(column_name), self.get_max(column_name)

    def get_yx_tuples(self):
        return [(y, x) for y, x in zip(self.data['Y'], self.data['X'])]


if __name__ == '__main__':
    data_extractor = CSVDataExtractor('CHCH_CAS_Data.csv')
    print(len(data_extractor.get_yx_tuples()))
