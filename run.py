#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author:An Shen
# Email: shen.an89@gmail.com

import sys

from conf import *
from gsoperat import GameServerControl
from hotfix import HotFix
from update import UpdateServer

def CheckSvrList(SvrType):
    if SvrType == "all":
        pass
    elif SvrType in channeles:
        pass
    else:
        print ("Error Chaneles!")
        exit(1)

def CallUpdate(SvrType,PakgeName):
        for x in server_info[SvrType]:
            print("Updating %s ..." %(server_info[SvrType][x]["minion_id"]))
            if SvrType == "yyb":
                Download_Url = TX_Download_Url
            else:
                Download_Url = King_Download_Url
            SvrInfo = server_info[SvrType][x]
            BegainUpdate = UpdateServer(SvrInfo=SvrInfo, PackgeName=PakgeName,Download_Url=Download_Url)
            BegainUpdate.run()
def ToUpdate(Parameters):
    SvrType = Parameters[1]
    # SvrNum = Parameters[2]
    PakgeName = Parameters[2]

    CheckSvrList(SvrType=SvrType)
    if SvrType == "all":
        for x in server_info:
            CallUpdate(SvrType=x,PakgeName=PakgeName)
    else:
        CallUpdate(SvrType=SvrType,PakgeName=PakgeName)

def CallHotfix(SvrType):
    for x in server_info[SvrType]:
        print("HotFix %s ..." %(server_info[SvrType][x]["minion_id"]))
        BegainHotfix = HotFix(SvrInfo=server_info[SvrType][x])
        BegainHotfix.run()
def ToHotfix(Parameters):
    SvrType = Parameters[1]
    CheckSvrList(SvrType=SvrType)

    if SvrType == "all":
        for x in server_info:
            CallHotfix(SvrType=x)
    else:
        CallHotfix(SvrType=SvrType)

def CallGSOperation(SvrType, Operation):
    for x in server_info[SvrType]:
        print("\033[91m" + "\n%s:%s" %(SvrType, x) +"\033[0m")
        BegainOperation = GameServerControl(SvrInfo=server_info[SvrType][x],Operat=Operation)
        BegainOperation.run()
def ToGSOperation(Parameters):
    SvrType = Parameters[1]
    Operation = Parameters[2]

    CheckSvrList(SvrType=SvrType)

    if SvrType == "all":
        for x in server_info:
            CallGSOperation(SvrType=x, Operation=Operation)
    else:
        CallGSOperation(SvrType=SvrType, Operation=Operation)




Parameters = sys.argv[1:]

if Parameters[0] in ["up","update"]:
    ToUpdate(Parameters)
elif Parameters[0] == "hotfix":
    ToHotfix(Parameters)
elif Parameters[0] == "game":
    ToGSOperation(Parameters)
else:
    print ("Error Operation Type!")
    exit(1)