import os
import requests
from csv import reader

class File:
    def __init__(self, name):
        self.name = name
        self.url = "https://github.com/franquicio/Miniproyecto2_Py_Sql/tree/main/Miniproyecto%202/file{}".format(name)

    def getPath(self):
        return os.path.join(
            os.path.dirname(__file__), self.name)

    def getRequest(self):
        decode = None
        response = requests.get(self.url)
        if response.status_code == 200:
            decode = response.content.decode("utf-8")
        return decode
    
    def read(self):
        rows = []
        file = open(self.getPath(), "r", encoding="utf-8", errors="replace")
        csvFile = reader(file, delimiter=";")
        next(csvFile)
        for line in csvFile:
            rows.append(line)
        return rows
    
    def readUrl(self):
        rows = []
        decode = self.getRequest()
        if decode is not None:
            csvFile = reader(decode.splitlines(), delimiter=";")
            next(csvFile)
            rows = list(csvFile)
        return rows
    
    def __str__(self):
        return f"name file is {self.name}"
    
if __name__ == "__main__":
    response = requests.get("https://github.com/franquicio/Miniproyecto2_Py_Sql/blob/main/Miniproyecto%202/file/actors.csv")
    decode = response.content.decode("utf-8")
    csvFile = reader(decode.splitlines(), delimiter=";")
    my_list = list(csvFile)
