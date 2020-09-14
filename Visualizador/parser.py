import pandas as pd

class Parser():
    def __init__(self):
        pass

    def loadData(self, url):
        self.data = pd.read_csv(url)

    def getData(self):
        return self.data

    def timeSeries(self):
        return 'fecha' in list(self.data.columns)

    def headers(self):
        return list(self.data.columns[0:4])