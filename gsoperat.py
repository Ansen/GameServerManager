# -*- coding: utf-8 -*-
# Author:An Shen
# Email: shen.an89@gmail.com

from callsalt import CallSalt

class GameServerControl(object):

    def __init__(self,SvrInfo,Operat):
        self.SvrInfo = SvrInfo
        self.Operat  = Operat

    def run(self):
        CommandStr = self.__BuildCommandStr()
        ToSalt = CallSalt(MinionID=self.SvrInfo["minion_id"], CommandStr=CommandStr)
        ToSalt.run()

    def __BuildCommandStr(self):
        CommandStr = "cd %s;./gamestart.sh %s" %(
            self.SvrInfo["Path"], self.Operat)
        return CommandStr