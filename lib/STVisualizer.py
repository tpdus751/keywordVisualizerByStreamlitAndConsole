# STVisualizer.py

import matplotlib.pyplot as plt
from wordcloud import WordCloud
import streamlit as st
from matplotlib import font_manager, rc


@st.cache_data # 오래 걸리는 데이터분석 한번만 실행하려할 때(재분석X) 캐시 기능
def visualize_barchart_streamlit(counter, title, xlabel, ylabel, top_n=20):
    most_common = counter.most_common(top_n)
    word_list = [word for word, _ in most_common]
    count_list = [count for _, count in most_common]

    # 한글 폰트 설정
    font_path = 'lib/assets/malgun.ttf'
    font_name = font_manager.FontProperties(fname=font_path).get_name()
    rc('font', family=font_name)

    fig, ax = plt.subplots()
    ax.barh(word_list[::-1], count_list[::-1])
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)

    st.pyplot(fig)


@st.cache_data # 오래 걸리는 데이터분석 한번만 실행하려할 때(재분석X) 캐시 기능
def visualize_wordcloud_streamlit(counter, max_words=50):
    font_path = "lib/assets/malgun.ttf"
    wordcloud = WordCloud(
        font_path=font_path,
        width=600,
        height=400,
        max_words=max_words,
        background_color="ivory"
    )

    wordcloud = wordcloud.generate_from_frequencies(counter)

    fig, ax = plt.subplots()
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis('off')

    st.pyplot(fig)
