import streamlit as st
import pandas as pd
from collections import Counter
from soynlp.tokenizer import RegexTokenizer

import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from lib import myTextMining as tm
from lib import STVisualizer as sv

st.set_page_config(page_title="단어 빈도수 시각화", layout="wide")
st.title("단어 빈도수 시각화")

st.info("분석할 파일을 업로드하고, 시각화 수단을 선택한 후 **'분석 시작'** 버튼을 클릭하세요.")

# === Sidebar 설정 영역 ===
st.sidebar.header("📂 파일 선택")
uploaded_file = st.sidebar.file_uploader("Drag and drop file here", type=["csv"])

column_name = st.sidebar.text_input("데이터가 있는 컬럼명", value="description")
check_btn = st.sidebar.button("데이터 파일 확인")

st.sidebar.markdown("---")
st.sidebar.header("설정")

draw_bar = st.sidebar.checkbox("빈도수 그래프", value=True)
top_n_bar = st.sidebar.slider("단어 수", 10, 50, 20)

draw_wc = st.sidebar.checkbox("워드클라우드", value=False)
top_n_wc = st.sidebar.slider("단어 수", 20, 500, 50)

analyze_btn = st.sidebar.button("분석 시작")

# === Main 화면 ===
if uploaded_file and check_btn:
    try:
        df = pd.read_csv(uploaded_file)
        st.success(f"파일 로딩 완료 - shape: {df.shape}")
        st.dataframe(df.head())
    except Exception as e:
        st.error(f"파일 로딩 실패: {e}")

if uploaded_file and analyze_btn:
    try:
        df = pd.read_csv(uploaded_file)
        corpus = list(df[column_name].dropna())

        tokenizer = RegexTokenizer()
        stopwords = ['등', '및', '수', '의', '이', '를', '</', '...', '(<', '>)', '>)']
        counter = tm.analize_word_freq(corpus, tokenizer, stopwords)

        if draw_bar:
            st.subheader("단어 빈도수 그래프")
            sv.visualize_barchart_streamlit(counter, f"{uploaded_file.name} 단어 분석", "빈도수", "단어", top_n_bar)

        if draw_wc:
            st.subheader("워드 클라우드")
            sv.visualize_wordcloud_streamlit(counter, max_words=top_n_wc)

    except Exception as e:
        st.error(f"분석 중 오류 발생: {e}")
