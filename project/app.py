import streamlit as st
import os
import codecs # 파일 인코딩 처리를 위해 codecs 사용

# Streamlit 페이지 설정 (전체 너비 사용)
st.set_page_config(
    page_title="카페인 뇌파 분석 시뮬레이터", 
    layout="wide"
)

def load_html_file(filepath):
    """
    지정된 HTML 파일의 내용을 읽어 반환합니다. 
    (인코딩 문제를 방지하기 위해 'utf-8'로 지정합니다.)
    """
    try:
        # 현재 스크립트(app.py)의 절대 경로를 기준으로 파일 경로를 구성합니다.
        current_dir = os.path.dirname(os.path.abspath(__file__))
        full_path = os.path.join(current_dir, filepath)
        
        with codecs.open(full_path, 'r', 'utf-8') as f:
            html_content = f.read()
        return html_content
    except FileNotFoundError:
        st.error(f"HTML 파일을 찾을 수 없습니다: '{filepath}' 경로를 확인해주세요.")
        return None
    except Exception as e:
        st.error(f"파일을 읽는 중 오류가 발생했습니다: {e}")
        return None

# HTML 파일 경로 (htmls 폴더 내에 위치)
HTML_FILE_PATH = "htmls/eeg_analysis_report_integrated.html"

# HTML 내용 로드
html_code = load_html_file(HTML_FILE_PATH)

st.header("📚 진로 주제탐구: 카페인 뇌파 분석 및 보고서 시뮬레이터")

if html_code:
    st.markdown(
        """
        이 Streamlit 애플리케이션은 HTML, CSS, JavaScript로 구현된 **'카페인 뇌파 분석 시뮬레이터와 보고서'**를 포함하고 있습니다.
        실제 분석 과정을 시뮬레이션하고 보고서 내용을 확인하며 탐구 활동을 심화할 수 있습니다.
        """
    )
    
    # Streamlit 컴포넌트를 사용하여 HTML 코드를 렌더링합니다.
    # HTML 내용이 충분히 길기 때문에 height를 1000px로 설정하고 스크롤을 허용합니다.
    st.components.v1.html(
        html_code, 
        height=1000, 
        scrolling=True
    )
    
    st.caption("시뮬레이터는 가상의 데이터를 기반으로 작동하며, 모든 분석 결과는 보고서의 탐구 주제에 맞게 설정되었습니다.")

else:
    st.warning("HTML 파일 로드에 실패하여 시뮬레이터를 표시할 수 없습니다.")
