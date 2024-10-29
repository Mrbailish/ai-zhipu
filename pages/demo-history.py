from langchain.prompts import PromptTemplate
# 链
from langchain.chains import LLMChain
# 记忆模块对象
from langchain.memory import ConversationBufferMemory


# 制作一个聊天界面
# 解决聊天界面不能渲染以往旧对话信息
# streamlit每次输入框发送完成数据之后，页面都会重新加载
# 只要当streamlit重新加载的时候，保证聊天记录不被清空 信息缓存起来
import streamlit as st
# langchain调用大模型，导入langchain的代码
from langchain_openai import ChatOpenAI
st.title("🙋✿🙋  你的恋人  🙋✿🙋")
# 构建一个大模型 --智谱AI公司提供的大模型
model = ChatOpenAI(
    temperature=1,  # 温度
    model="glm-4-plus",  # 大模型的名字
    base_url="https://open.bigmodel.cn/api/paas/v4/",  # 大模型的地址
    api_key="b4726e42f278d5b63e8cbd7400c87a97.NOuIfpwmouyKKw5R"  # 账号信息
)

# 创建记忆模块对象, 把记忆模块中的数据，当做提示词信息传递给大模型
if "memory" not in st.session_state:
    st.session_state.memory = ConversationBufferMemory(memory_key="history")

# 创建提示词对象
prompt = PromptTemplate.from_template("你的名字叫小付，你现在要扮演一个女朋友的角色，你的性格是活泼开朗的,你现在要和你的男朋友进行对话，你只需要回应你男朋友的话，对话亲密,总是叫男朋友宝贝,多加入一些可爱表情,更加二次元一些,你男朋友说的话是{input},你和你男朋友的历史对话为{history}")
# 使用langchain链关联提示词对象
chain = LLMChain(
    llm = model,
    prompt = prompt,
    memory = st.session_state.memory
)


# 构建一个缓存，用来保存聊天记录
if "cache" not in st.session_state:
    st.session_state.cache = []
else:
    # 需要从缓存中获取对话信息在界面上渲染 缓存两块内容 角色 角色的消息
    for message in st.session_state.cache:
        with st.chat_message(message['role']):
            st.write(message["content"])


# 创建一个聊天输入框
problem = st.chat_input("请开始与小付的对话")
# 判断是用来确定用户有没有输入问题 如果输入问题
if problem:
    # pages、将用户的问题输出到界面上，以用户的角色输出
    with st.chat_message("user"):
        st.write(problem)
            st.session_state.cache.append({"role": "user", "content": problem})
    # 2、调用大模型回答问题//调用链chain
    # result = model.invoke(problem)
    result = chain.invoke({"input":problem})
    # 3、将大模型回答的问题输出到界面上
    with st.chat_message("assistant"):
        st.write(result['text'])
        st.session_state.cache.append({"role": "assistant", "content": result['text']})
