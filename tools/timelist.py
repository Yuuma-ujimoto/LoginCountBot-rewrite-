import datetime

class timelist:
    def __init__(self):
        self.n = datetime.datetime.now()

    def CreateTimeList(self):
        l= [self.n.month,self.n.day]
        return l

    def GetNowTime(self):
        return self.n