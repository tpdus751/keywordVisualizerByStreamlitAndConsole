from collections import Counter
from konlpy.tag import Okt

def load_corpus_from_csv(corpus_file, col_name):
    import pandas as pd
    data_df = pd.read_csv(corpus_file)
    result_list = list(data_df[col_name])
    return result_list

def tokenize_korean_corpus(corpus_list, tokenizer, tags, stopwords):
    text_pos_list = []
    for sentence in corpus_list:
        text_pos = tokenizer(sentence)
        text_pos_list += text_pos # .extend() 도 가능

    token_list = [token for token, tag in text_pos_list if tag in tags and token not in stopwords and len(token) > 1]
    return token_list

def analize_word_freq(corpus_list, tokenizer, stopwords):
    token_list = tokenize_korean_corpus(corpus_list, tokenizer, stopwords)
    counter = Counter(token_list)
    return counter

def visualize_barchart(counter, title, xlabel, ylabel):
    # 데이터 준비
    most_common = counter.most_common(20)
    word_list = [word for word, _ in counter.most_common(20)]
    count_list = [count for _, count in counter.most_common(20)]

    # 한글 폰트 설정하기
    # matplotlib 한글 폰트 설정
    from matplotlib import font_manager, rc
    font_path = "c:/Windows/Fonts/malgun.ttf"
    font_name = font_manager.FontProperties(fname=font_path).get_name()
    rc('font', family=font_name)

    # barh 만들기
    import matplotlib.pyplot as plt
    plt.barh(word_list[::-1], count_list[::-1])

    # 그래프 정보 설정
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    # 그리기
    plt.show()

def visualize_wordcloud(counter):
    from wordcloud import WordCloud
    import matplotlib.pyplot as plt

    # 한글 폰트 path 지정
    font_path = "c:/Windows/fonts/malgun.ttf"

    # WordCloud 객체 생성
    wordcloud = WordCloud(font_path, width=600, height=400, max_words=50, background_color="ivory")

    # 빈도 데이터로 워드클라우드 시각화
    wordcloud = wordcloud.generate_from_frequencies(counter)
    plt.imshow(wordcloud)
    plt.axis('off') # x축 y축 없애기
    plt.show()
