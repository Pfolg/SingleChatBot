# -*- coding: utf-8 -*-
# Environment    PyCharm
# File_name   MainProgram |User    Pfolg
# 2024/7/13   9:42
import ReadKey
import SendAi
import RecordLog
import ReplyMessage
import GainMessage

"""大概有三个重要参数要设定，必须！！！因人而异！"""

oldRequire = ""
while True:
    # 获取消息
    require = GainMessage.analyseLog("ZS", 932, 495)  # 这个坐标是消息界面的一个坐标，QQname就是昵称，别人@你 显示的那个
    if require != 0:
        if require != oldRequire:
            oldRequire = require

            ReadKey.pauseSecond()

            # 读取AI参数(客户端方)
            dictKey = ReadKey.get_keys()

            ReadKey.pauseSecond()

            # 向AI发送消息并获得回复
            reply = SendAi.send_getReply(dictKey, information=require)

            ReadKey.pauseSecond()

            # 回复消息
            if reply:
                print(reply)
                ReplyMessage.Reply(reply, 865, 735)  # 这个坐标需要获取，聊天框坐标

                ReadKey.pauseSecond()

                # 记录<聊天记录>

                RecordLog.writeLog(require, reply)
