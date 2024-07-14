# -*- coding: utf-8 -*-
# Environment    PyCharm
# File_name   ReadKey |User    Pfolg
# 2024/7/13   9:47
import time

"""
这个程序用于获取API，也就是秘钥
这里用的是sparkAI（星火）https://www.xfyun.cn/
不知道怎么配就上网查
"""


def get_keys():
    time.sleep(2)
    with open(".\\Secret.txt", "r", encoding="utf-8") as file:
        content = file.readline()

    listCon = content.split("'")
    listKey = ["SPARKAI_URL", "SPARKAI_APP_ID", "SPARKAI_API_SECRET", "SPARKAI_API_KEY", "SPARKAI_DOMAIN"]
    listValue = []
    for i in range(len(listCon)):
        if i % 2 != 0:
            listValue.append(listCon[i])
        else:
            pass

    dictKey = dict(zip(listKey, listValue))
    return dictKey


def pauseSecond():
    time.sleep(0.5)


if __name__ == '__main__':
    pass
