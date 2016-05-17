# -*- coding: utf-8 -*-
# Author:An Shen
# Email: shen.an89@gmail.com

from callsalt import CallSalt

class UpdateServer(object):
    def __init__(self,SvrInfo, PackgeName, Download_Url):
        self.SvrInfo    = SvrInfo
        self.PackgeName = PackgeName
        self.Download_Url  = Download_Url

    def run(self):
        CommandStr = self.__BuildCommandStr()
        ToSalt = CallSalt(MinionID=self.SvrInfo["minion_id"], CommandStr=CommandStr)
        ToSalt.run()

    def __BuildCommandStr(self):
        CommandStr = "cd %s ; wget -q %s%s" %(
            self.SvrInfo["Path"],self.Download_Url,self.PackgeName
        )
        return CommandStr
