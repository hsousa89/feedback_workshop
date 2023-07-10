import csv


class CustomCSVReader:
    def __init__(self, file_path, encoding="utf-8-sig"):
        self.file_path = file_path
        self.encoding = encoding

    @property
    def data_as_list(self):
        data = []
        with open(self.file_path, "r", encoding=self.encoding) as file:
            reader = csv.reader(file)
            for row in reader:
                data.append(row)
        return data

    @property
    def data_as_dict(self):
        data = []
        with open(self.file_path, "r", encoding=self.encoding) as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(dict(row))
        return data
