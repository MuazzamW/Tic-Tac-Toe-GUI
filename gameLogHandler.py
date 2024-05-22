import json

class gameLogHandler:
    def __init__(self,fileName):
        self.__fileName = fileName
        with open(self.__fileName, 'r', encoding='utf-8') as f:
            self.__logs = json.load(f)

    def returnLogs(self):
        return self.__logs


# g1 = gameLogHandler("GameLog/data.json")
# print(g1.returnLogs()[2]["date"]) 