import streamlit as st
import pandas as pd

# 파일 로드 (이 부분은 데이터를 직접 불러올 수 있도록 수정해야 합니다)
@st.cache
def load_data():
    # 데이터 파일을 GitHub에 업로드하고 여기에 그 URL을 넣으세요
    url = 'https://raw.githubusercontent.com/your-repo-path/CRS_2022_data.txt'
    return pd.read_csv(url, delimiter='|')

# 애플리케이션 제목
st.title("CRS 2022 Data Analysis")

# 데이터 불러오기
data = load_data()

# 데이터프레임 표시
st.write("Data Sample:")
st.dataframe(data.head())

# 데이터 설명 통계
st.write("Data Summary:")
st.write(data.describe())
