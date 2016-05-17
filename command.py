# -*- coding: utf-8 -*-
# Author:An Shen
# Email: shen.an89@gmail.com

from callsalt import CallSalt

class Command(object):

    def __init__(self,SvrInfo,Command):
        self.SvrInfo = SvrInfo
        self.Command  = Command

    def run(self):
        CommandStr = self.__BuildCommandStr()
        ToSalt = CallSalt(MinionID=self.SvrInfo["minion_id"], CommandStr=CommandStr)
        ToSalt.run()

    def __BuildCommandStr(self):
        CommandStr = "cd %s; %s" %(
            self.SvrInfo["Path"], self.Command)
        return CommandStr