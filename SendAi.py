# -*- coding: utf-8 -*-
# Environment    PyCharm
# File_name   SendAi |User    Pfolg
# 2024/7/13   9:47
from sparkai.llm.llm import ChatSparkLLM, ChunkPrintHandler
from sparkai.core.messages import ChatMessage


def send_getReply(key: dict, information):
    spark = ChatSparkLLM(
        spark_api_url=key.get("SPARKAI_URL"),
        spark_app_id=key.get("SPARKAI_APP_ID"),
        spark_api_key=key.get("SPARKAI_API_KEY"),
        spark_api_secret=key.get("SPARKAI_API_SECRET"),
        spark_llm_domain=key.get("SPARKAI_DOMAIN"),
        streaming=False,
    )
    style = "幽默风趣，简洁明了"
    firstContent = f"你被要求作为聊天对象，回复消息的风格为:{style}。对方的消息为:"
    messages = [ChatMessage(
        role="user",
        content=firstContent + information
    )]
    handler = ChunkPrintHandler()
    sp = spark.generate([messages], callbacks=[handler])
    reply = sp.generations[0][0].text
    return reply


if __name__ == '__main__':
    pass
