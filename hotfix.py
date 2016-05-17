# -*- coding: utf-8 -*-
# Author:An Shen
# Email: shen.an89@gmail.com

from callsalt import CallSalt

class HotFix(object):
    def __init__(self,SvrInfo):
        self.SvrInfo = SvrInfo

    def run(self):
        CommandStr = self.__BuildCommandStr()
        ToSalt = CallSalt(MinionID=self.SvrInfo["minion_id"], CommandStr=CommandStr)
        ToSalt.run()

    def __BuildCommandStr(self):
        CommandStr = "cd %s;./PyDebugger 127.0.0.1 %s reloadall.py" %(
            self.SvrInfo["Path"], self.SvrInfo["DebugPort"])
        return CommandStr