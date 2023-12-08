import streamlit as st
import os

os.environ["OPENAI_API_KEY"] = "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"

from langchain.chat_models import ChatOpenAI
from langchain.agents import load_tools
from langchain.agents import initialize_agent

llm = ChatOpenAI(temperature=1,model_name="gpt-3.5-turbo-1106")

def chat_ui():
    st.title("シンプルなチャットUI")

    # セッション状態を初期化
    if 'messages' not in st.session_state:
        st.session_state.messages = []

    # チャットボックス
    user_input = st.text_input("メッセージを入力してね")
    bot_output = ""; #OpenAI APIのレスポンスを格納する

    # ユーザーがメッセージを入力したらオウム返し
    if st.button("送信"):
        st.session_state.messages.append(("User", user_input))
        bot_res = llm.predict(user_input)
        st.session_state.messages.append(("Bot", bot_res))  # オウム返しも追加

    # メッセージ表示
    for sender, message in st.session_state.messages:
        st.write(f"{sender}:")
        if sender == "User":
            st.info(message)  # ユーザーのメッセージを枠で囲む
        else:
            st.success(message)  # オウムのメッセージを別の色で囲む

        #st.write(st.session_state.messages)

if __name__ == '__main__':
    chat_ui()