import lib.myTextMining as tm
import lib.NaverNewsCrawler as nnc
from lib.APIKey import NaverAPI as npi 
from konlpy.tag import Okt, Komoran
from sklearn.feature_extraction.text import TfidfVectorizer

keyword = input("검색어를 입력하세요 : ")

client_id = npi.client_id
client_secret = npi.client_secret

# 검색 결과를 저장할 list 초기화
resultAll = []

# 첫 검색 API 호출
start = 1
display = 10

resultJSON = nnc.searchNaverNews(keyword, start, display, client_id, client_secret)

while (resultJSON != None) and (resultJSON['display'] > 0):
    # 응답데이터 정리하여 리스트 저장
    nnc.setNewsSearchResult(resultAll, resultJSON)
 
    # 다음 검색 API 호출을 위한 파라미터 조정
    start += resultJSON['display']
    # API 호출
    resultJSON = nnc.searchNaverNews(keyword, start, display, client_id, client_secret)
    
    # API 호출 성공 여부 출력
    if resultJSON != None:
        print(f'{keyword} [{start}] : Search Request Success')
    else:
        print(f"{keyword} [{start}] : Error ~~~~")

# 리스트를 csv 파일로 저장
filename = f"../data/{keyword}_naver_news.csv"
nnc.saveSearchResult_CSV(resultAll, filename)

# 코퍼스(말뭉치) 로딩
input_filename = keyword + "_naver_news.csv"
corpus_list = tm.load_corpus_from_csv("../data/" + input_filename, 'description')
print(corpus_list[:10])

my_tokenizer = Okt().pos # 함수 포인터?

my_tags = ['Noun']

my_stopwords = ['등', '및', '수', '의', '이', '를'] # 예시

# 빈도수 추출
counter = tm.analize_word_freq(corpus_list,  my_tokenizer, my_tags, my_stopwords)
#tm.visualize_barchart(counter, f"네이버 뉴스 {keyword} 키워드 분석", "빈도수", "키워드")
tm.visualize_wordcloud(counter)