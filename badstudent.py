import requests, json
class BadStudent:
    gateway = "https://badstudent.co/data"
    def GetRank(self):
        return requests.get(self.gateway+"/home.json").json()["rank"]
    def GetReport(self):
        return requests.get(self.gateway+"/home.json").json()["report"]
    def GetTotal(self):
        return requests.get(self.gateway+"/home.json").json()["total"]
    def LastUpdate(self):
        return requests.get(self.gateway+"/home.json").json()["lastupdate"]