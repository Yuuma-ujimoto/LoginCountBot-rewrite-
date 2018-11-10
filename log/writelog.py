import tools.timelist
import codecs
import os
class writelog:
    def __init__(self):
        self.n = tools.timelist.timelist().GetNowTime()
    def Log(self,UserName,ServerName,Command):
        print(os.listdir("../"))
        logmessage = "["+UserName+"] -> "+Command+"/ time->"+str(self.n)
        print("console log ->"+logmessage)
        print("-----------------------------------------")
        f1 = codecs.open("../log/All/Log.txt","a","utf-8")
        f2 = codecs.open("../log/Server/Log"+ServerName+".txt","a","utf-8")
        f3 = codecs.open("../log/User/Log("+UserName+").txt","a","utf-8")
        filelist=[f1, f2, f3]

        for x in filelist:

            x.write(logmessage)
