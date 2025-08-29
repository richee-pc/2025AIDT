# streamlit 라이브러리를 가져옵니다.
import streamlit as st
# HTML, CSS, Javascript 코드를 Streamlit 앱에 삽입하기 위한 components를 가져옵니다.
import streamlit.components.v1 as components
import os

# --- 페이지 설정 ---
# Streamlit 앱의 페이지 구성을 설정합니다.
st.set_page_config(
    page_title="🍎 AI 활용 연수 웹 🍎",
    layout="wide",
    page_icon="🍎" # 귀여운 페이지 아이콘 추가
)

# --- 폰트 및 전체적인 디자인 CSS 주입 ---
st.markdown("""
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Gowun+Dodum&display=swap" rel="stylesheet">
<style>
    /* 전체 폰트 적용 */
    html, body, [class*="st-"], button, input, textarea {
        font-family: 'Gowun Dodum', sans-serif;
    }
    /* 메인 타이틀 스타일 */
    .main-title {
        font-size: 2.8rem;
        font-weight: bold;
        color: #c026d3; /* Fuchsia-600 */
        text-align: center;
        padding: 1.5rem;
        background: linear-gradient(135deg, #fdf4ff 0%, #fce7f3 100%); /* Pink gradient */
        border-radius: 20px;
        border: 2px dashed #f9a8d4; /* Pink-300 */
        margin-bottom: 2rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
    }
    /* 탭(Tab) 메뉴 스타일 꾸미기 */
    button[data-baseweb="tab"] {
        font-size: 1.1rem !important;
        font-weight: bold !important;
        background-color: #faf5ff; /* Purple-50 */
        border-radius: 10px 10px 0 0 !important;
        border: 1px solid #e9d5ff;
        border-bottom: none !important;
        margin-right: 5px !important;
        transition: all 0.3s ease;
    }
    button[data-baseweb="tab"]:hover {
        background-color: #f3e8ff; /* Purple-100 */
    }
    button[data-baseweb="tab"][aria-selected="true"] {
        background-color: #a855f7; /* Purple-600 */
        color: white;
        border-color: #a855f7;
    }
    /* Streamlit 기본 헤더 숨기기 */
    .stApp > header {
        background-color: transparent;
    }
</style>
""", unsafe_allow_html=True)


# --- HTML 파일 로드 함수 (오류 수정된 부분) ---
def load_html(path):
    """지정된 경로의 HTML 파일을 읽어 그 내용을 반환하는 함수"""
    # 현재 스크립트(app.py) 파일의 디렉토리 경로를 가져옵니다.
    script_dir = os.path.dirname(__file__)
    # 스크립트 디렉토리와 상대 경로를 합쳐 파일의 절대 경로를 만듭니다.
    abs_path = os.path.join(script_dir, path)
    
    if not os.path.exists(abs_path):
        st.error(f"'{os.path.basename(path)}' 파일을 찾을 수 없습니다. 경로를 확인해주세요: {abs_path}")
        return None # 오류 발생 시 None 반환
    try:
        with open(abs_path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        st.error(f"파일을 읽는 중 오류가 발생했습니다: {e}")
        return None

# --- 메인 화면 구성 ---
# 커스텀 HTML로 디자인된 제목 표시
st.markdown('<p class="main-title">🍎 생성형 AI 활용 연수 학습 웹 🍎</p>', unsafe_allow_html=True)

# 안내 메시지
st.info("안녕하세요, 선생님! 🐰 아래 탭에서 원하시는 연수 자료를 선택해서 학습을 시작해보세요! 각 탭을 클릭하면 해당 자료가 나타납니다.", icon="💡")

# --- 탭(Tab) 메뉴로 페이지 분리 ---
tab1, tab2 = st.tabs(["🎨 구글 Gemini & Notebooklm 활용 매뉴얼", "✨ Claude AI 활용 매뉴얼"])

# '기존 연수 자료' 탭
with tab1:
    # 이제 상대 경로를 사용해도 절대 경로로 변환되어 파일을 잘 찾습니다.
    html_code_1 = load_html('htmls/index.html')
    if html_code_1:
        components.html(html_code_1, height=1200, scrolling=True)
    else:
        st.warning("기존 연수 자료(index.html)를 불러올 수 없습니다.")

# 'Claude AI 활용 매뉴얼' 탭
with tab2:
    html_code_2 = load_html('htmls/index2.html')
    if html_code_2:
        components.html(html_code_2, height=1200, scrolling=True)
    else:
        st.warning("Claude AI 활용 매뉴얼(index2.html)을 불러올 수 없습니다.")


# --- 푸터(Footer) ---
st.markdown("---")
st.markdown("<div style='text-align: center; font-family: \"Gowun Dodum\", sans-serif;'>Made with 🩵🐰🩵 by AI for Teachers</div>", unsafe_allow_html=True)
