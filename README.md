# 🔍 Keyword Visualizer by Streamlit & Console

한국어 뉴스 기사 데이터(csv)를 기반으로 **핵심 키워드를 추출하고 시각화**하는 애플리케이션입니다.  
Streamlit 웹 앱과 콘솔 기반 분석 프로그램이 함께 제공됩니다.

---

## 🚀 배포 링크

👉 [Streamlit에서 바로 실행하기](https://keywordvisualizerbyapp-bm3n3c6tx9mknqemljxccb.streamlit.app/)  
※ 앱 배포 플랫폼: **Streamlit Cloud**

---

## 💾 실행에 필요한 데이터

- 이 프로젝트는 **한국어 뉴스 기사 데이터**가 담긴 CSV 파일을 필요로 합니다.
- 파일: [Uploading LLM[Uploading LLM_naver_news.csv…]()
_naver_news.csv…]()


## 📦 주요 기능

- ✅ 뉴스 CSV 파일 업로드 및 분석
- ✅ 형태소 분석 기반 키워드 추출 (`soynlp` 사용)
- ✅ 불용어 제거 및 상위 키워드 시각화
- ✅ 막대그래프 & 워드클라우드 제공
- ✅ 콘솔 기반 키워드 분석 프로그램도 함께 제공

---

## 🧪 사용된 주요 라이브러리

- `streamlit`
- `soynlp`
- `matplotlib`
- `wordcloud`
- `pandas`
- `collections.Counter`

---

## 💻 실행 방법

### 📁 1. 로컬 실행
```bash
# 가상환경 추천
pip install -r requirements.txt
streamlit run KeywordVisualizerSTApp.py
