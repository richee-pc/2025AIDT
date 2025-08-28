# streamlit 라이브러리를 가져옵니다.
import streamlit as st
# HTML, CSS, Javascript 코드를 Streamlit 앱에 삽입하기 위한 components를 가져옵니다.
import streamlit.components.v1 as components
# 파일 경로를 다루기 위한 os 라이브러리를 가져옵니다.
import os

# --- 페이지 설정 ---
# Streamlit 앱의 페이지 구성을 설정합니다.
# page_title은 브라우저 탭에 표시될 제목입니다.
# layout="wide"는 콘텐츠를 화면 전체 너비로 표시하도록 설정합니다.
st.set_page_config(
    page_title="교사용 AI 활용 연수 워크숍",
    layout="wide"
)

# --- HTML 파일 로드 (경로 문제 해결) ---
# app.py 파일의 현재 위치를 기준으로 'index.html'의 절대 경로를 생성합니다.
# 이 방법은 Streamlit Cloud 배포 환경에서도 파일을 정확히 찾을 수 있게 해줍니다.
_RELEASE = True
if not _RELEASE:
    # 로컬에서 실행할 경우의 경로 (필요시 사용)
    _INDEX_HTML = os.path.join(os.path.dirname(__file__), "index.html")
else:
    # 배포 환경에서의 경로
    _INDEX_HTML = os.path.join(os.path.dirname(__file__), "index.html")


# 웹페이지를 구성하는 HTML 파일을 엽니다.
# 'utf-8' 인코딩을 사용하여 한글이 깨지지 않도록 합니다.
try:
    with open(_INDEX_HTML, 'r', encoding='utf-8') as f:
        html_code = f.read()
except FileNotFoundError:
    st.error("'index.html' 파일을 찾을 수 없습니다. app.py와 같은 폴더에 있는지 확인해주세요.")
    st.stop() # 파일이 없으면 앱 실행을 중지합니다.


# --- Streamlit에 HTML 렌더링 ---
# st.markdown을 사용하여 제목을 표시합니다. unsafe_allow_html=True를 통해 HTML 태그를 사용할 수 있습니다.
st.markdown("<h1>교사용 AI 활용 최종판: 제미나이 & 노트북LM 워크숍</h1>", unsafe_allow_html=True)
st.markdown("---")

# components.html을 사용하여 읽어온 HTML 코드를 앱에 표시합니다.
# height는 HTML 컴포넌트의 높이를 픽셀 단위로 설정합니다.
# scrolling=True는 내용이 높이를 초과할 경우 스크롤바를 생성하도록 합니다.
components.html(html_code, height=1200, scrolling=True)

# --- 푸터(Footer) ---
st.markdown("---")
st.markdown("Made with ❤️ by AI for Teachers")
