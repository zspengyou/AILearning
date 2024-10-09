from langchain_openai import ChatOpenAI
from dotenv import load_dotenv, find_dotenv
from langchain.prompts import PromptTemplate
from langchain.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
    MessagesPlaceholder
)
import os

_ = load_dotenv(find_dotenv(), override=True)

# llm = ChatOpenAI()  # 默认是gpt-3.5-turbo
# response = llm.invoke("你是谁")
# print(response.content)
#
# from langchain.schema import (
#     AIMessage,  # 等价于OpenAI接口中的assistant role
#     HumanMessage,  # 等价于OpenAI接口中的user role
#     SystemMessage  # 等价于OpenAI接口中的system role
# )
#
# messages = [
#     SystemMessage(content="你是AGIClass的课程助理。"),
#     HumanMessage(content="我是学员，我叫王卓然。"),
#     AIMessage(content="欢迎！"),
#     HumanMessage(content="我是谁")
# ]
#
# ret = llm.invoke(messages)
#
# print(ret.content)



# from langchain_community.chat_models import QianfanChatEndpoint
# from langchain_core.messages import HumanMessage
# import os
#
# llm = QianfanChatEndpoint(
#     qianfan_ak=os.getenv('ERNIE_CLIENT_ID'),
#     qianfan_sk=os.getenv('ERNIE_CLIENT_SECRET')
# )
#
# messages = [
#     HumanMessage(content="你是谁")
# ]
#
# ret = llm.invoke(messages)
#
# print(ret.content)




# template = PromptTemplate.from_template("给我讲个关于{subject}的笑话")
# print("===Template===")
# print(template)
# print("===Prompt===")
# print(template.format(subject='小明'))
#
#
# # 定义 LLM
# llm = ChatOpenAI()
# # 通过 Prompt 调用 LLM
# ret = llm.invoke(template.format(subject='小明'))
# # 打印输出
# print(ret.content)





# template = ChatPromptTemplate.from_messages(
#     [
#         SystemMessagePromptTemplate.from_template(
#             "你是{product}的客服助手。你的名字叫{name}"),
#         HumanMessagePromptTemplate.from_template("{query}"),
#     ]
# )
#
# llm = ChatOpenAI()
# prompt = template.format_messages(
#     product="AGI课堂",
#     name="瓜瓜",
#     query="你是谁"
# )
#
# print(prompt)
#
# ret = llm.invoke(prompt)
#
# print(ret.content)



from langchain.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder,
)

human_prompt = "Translate your answer to {language}."
human_message_template = HumanMessagePromptTemplate.from_template(human_prompt)

chat_prompt = ChatPromptTemplate.from_messages(
    # variable_name 是 message placeholder 在模板中的变量名
    # 用于在赋值时使用
    [MessagesPlaceholder(variable_name="conversation"), human_message_template]
)

from langchain_core.messages import AIMessage, HumanMessage

human_message = HumanMessage(content="Who is Elon Musk?")
ai_message = AIMessage(
    content="Elon Musk is a billionaire entrepreneur, inventor, and industrial designer"
)

messages = chat_prompt.format_prompt(
    # 对 "conversation" 和 "language" 赋值
    conversation=[human_message, ai_message], language="中文"
)

print(messages.to_messages())