from dotenv import load_dotenv

# .envファイルの読み込み
load_dotenv()

import streamlit as st
from openai import OpenAI
import os


# OpenAIクライアント初期化
client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

st.title("専門家に質問しよう！")

# 操作ガイド
st.write("以下の専門家を選択し、質問を入力してください。AIが専門的な回答をしてくれます。")

# ラジオボタンで専門家を選択
expert = st.radio(
    "専門家を選んでください：",
    ("健康の専門家", "ラーメンの専門家")
)

# 入力フォーム
user_input = st.text_input("質問を入力してください：")

# 実行ボタン
if st.button("送信"):
    if user_input.strip() == "":
        st.warning("質問を入力してください。")
    else:
        # 専門家に応じてシステムプロンプトを設定
        if expert == "健康の専門家":
            system_message = "あなたは健康に関するアドバイザーです。安全なアドバイスを提供してください。"
        else:
            system_message = "あなたはラーメンの専門家です。全国のラーメンに関する詳しい情報を提供してください。"

        # OpenAI API で回答生成
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": user_input}
            ],
            temperature=0.5
        )

        # 結果表示
        answer = response.choices[0].message.content
        st.success("AIからの回答:")
        st.write(answer)
