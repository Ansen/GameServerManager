# -*- coding: utf-8 -*-
# Author:An Shen
# Email: shen.an89@gmail.com

Select_Type       = ["update", "up", "hotfix", "game"]
channeles         = ["ios", "hf", "yyb", "mha"]
King_Download_Url = "http://192.168.1.1/static/update/"
TX_Download_Url   = "http://192.168.1.1/static/update/"

server_info       = {
    "ios":{
        1:{
            "minion_id":"minion_id",
            "DebugPort":1234,
            "Merged":0,# 0 表示未被合服，1表示已经被合服且服务器不存在
            "Path":"Path",
            "ip":"192.168.1.2" # 内网IP
        },
        2:{
            "minion_id":"minion_id",
            "DebugPort":123,
            "Merged":0,
            "Path":"Path",
            "ip":"192.168.1.2"
        }

    },
    "hunfu":{
        1:{
            "minion_id":"minion_id",
            "DebugPort":123,
            "Merged":0,
            "Path":"Path",
            "ip":"192.168.1.2"
        }
    },
    "mha":{
        1:{
            "minion_id":"minion_id",
            "DebugPort":123,
            "Merged":0,
            "Path":"Path",
            "ip":"192.168.1.2"
        }
    },
    "yyb":{
        1:{
            "minion_id":"minion_id",
            "DebugPort":123,
            "Merged":0,
            "Path":"Path",
            "ip":"192.168.1.2"
        }
    }
}