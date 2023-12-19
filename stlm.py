import streamlit as st
from langchain.chat_models import ChatOpenAI

from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferWindowMemory
from langchain.chains import ConversationChain
from langchain.schema import HumanMessage
from langchain.schema import AIMessage

# memoryオブジェクトをキャッシュする関数を定義
def get_memory():
    return ConversationBufferWindowMemory(k=5, return_messages=True)

# キャッシュされたmemoryオブジェクトを取得
if 'memory' not in st.session_state:
    st.session_state.memory = get_memory() # memoryがsession_stateに追加されていない場合、get_memoryで初期化

memory = st.session_state.memory # session_stateからmemoryを取得

llm = ChatOpenAI(temperature=1,model_name="gpt-3.5-turbo-1106")

conversation = ConversationChain(
    llm=llm, 
    memory=memory
)

st.title("シンプルなチャットUI")

# チャットボックス
user_input = st.chat_input("Say something")
if user_input:
    response = conversation.predict(input=user_input)
    for message in memory.load_memory_variables({})["history"]:
        if isinstance(message, HumanMessage):
            with st.chat_message("user"):
                st.write(message.content)
        elif isinstance(message, AIMessage):
            with st.chat_message("ai"):
                st.write(message.content)
