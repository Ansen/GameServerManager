# -*- coding: utf-8 -*-
# Author:An Shen
# Email: shen.an89@gmail.com

# import salt.client

class CallSalt(object):

    def __init__(self,MinionID,CommandStr):
        self.MinionID   = MinionID
        self.CommandStr = CommandStr
        # 输出颜色
        self.OKGREEN = "\033[32m"
        self.WARNING = '\033[33m'
        self.FAIL    = "\033[91m"
        self.ENDC    = "\033[0m"

    def run(self):
        result = self.__execute(command=self.CommandStr)
        self.__result_filter(result=result)

    def __execute(self,command):
        command = [command]
        # client = salt.client.LocalClient()
        # result = client.cmd(self.MinionID, "cmd.run_all", command)
        print self.MinionID,command
        result = {}
        return result

    def __result_filter(self,result):
        if result == {}:
            print( self.WARNING + "%s Can not connect." % self.MinionID + self.ENDC)
        else:
            run_status = result[self.MinionID]
            exit_code = run_status["retcode"]
            if exit_code == 0:
                # print( self.OKGREEN + "Success." + self.ENDC)
                print("%s" % run_status["stdout"])
            else:
                print( self.FAIL + "%s: Failed to perform the command!" % self.MinionID + self.ENDC),
                print("%s%s" % (run_status["stderr"], run_status["stdout"]))