# -*- coding: utf-8 -*-
# Environment    PyCharm
# File_name   RecordLog |User    Pfolg
# 2024/7/13   9:48
import json
import time


# 记录聊天记录
def writeLog(information=None, AIReply=None):
    now = time.localtime()
    formatTime = time.strftime("%Y-%m-%d %H:%M:%S", now)

    log = str({"Time": formatTime, "Sent": information, "Reply": AIReply})
    with open(".\\ChatLog.txt", "a", encoding="utf-8") as file:
        file.write(log)
        file.write("\n")
        print("\n" + "-" * 50, "\n聊天记录已记录至ChatLog.txt!")


# 浏览聊天记录
def readLogByJson():
    with open(".\\ChatLog.txt", "r", encoding="utf-8") as file:
        content = file.readlines()
        if content:
            for i in content:
                jc = json.dumps(eval(i), ensure_ascii=False, indent=4)
                print(jc)
                time.sleep(0.05)
        else:
            print("Null")


# 浏览聊天记录
def readLogByPrint():  # recommend
    with open(".\\ChatLog.txt", "r", encoding="utf-8") as file:
        content = file.readlines()
        if content:
            for i in content:
                dictLog = eval(i)
                print()
                print(">>> 时间:", dictLog.get("Time"))
                print(">>> 发送:", dictLog.get("Sent"))
                print(">>> 回复:", dictLog.get("Reply"))
                time.sleep(0.05)
        else:
            print("Null")


# 清空聊天记录
def clearLog():
    with open(".\\ChatLog.txt", "w", encoding="utf-8") as file:
        file.write("")


if __name__ == '__main__':
    pass
