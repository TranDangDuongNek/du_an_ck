import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# =======================
# LOAD DATA
# =======================
@st.cache_data
def load_data():
    df = pd.read_csv("data/du_lieu_vay.csv")
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
    return df

df = load_data()

# --------------------
# TIÊU ĐỀ

title = "Phân tích tác động kinh tế của dịch COVID-19 qua dữ liệu vay EIDL (2020)"
st.markdown(f"<h1 style='text-align: center;'>{title}</h1>", unsafe_allow_html=True)
st.markdown("---")

# ----------------------
# TIỀN XỬ LÝ

numerical_cols = [
    'federalactionobligation',
    'nonfederalfundingamount',
    'facevalueofdirectloanorloanguarantee',
    'originalloansubsidycost'
]

for col in numerical_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')

df_clean = df.dropna(subset=numerical_cols)

# ----------------------
# 1. HEATMAP – MỐI TƯƠNG QUAN

header1 = "1. Mối tương quan giữa các yếu tố tài chính"
st.markdown(f"<h2 style='background:black; color:white'>{header1}</h2>", unsafe_allow_html=True)



corr = df_clean[numerical_cols].corr()

fig, ax = plt.subplots(figsize=(7, 5))
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f",
            linewidths=0.5, ax=ax)
st.pyplot(fig)

st.markdown("""
**Nhận xét:**
- Chi phí trợ cấp ban đầu và giá trị khoản vay có mối tương quan mạnh.
- Điều này cho thấy chính sách tài trợ của chính phủ ảnh hưởng trực tiếp đến quy mô hỗ trợ doanh nghiệp trong đại dịch.
""")

# ----------------------
# 2. TOP 10 BANG CHỊU ẢNH HƯỞNG NẶNG

header2 = "2. Top 10 bang có tổng giá trị vay cao nhất"
st.markdown(f"<h2 style='background:black; color:white'>{header2}</h2>", unsafe_allow_html=True)

st.image(
    "data/top10_bang.png",
    caption="Top 10 bang có tổng giá trị khoản vay EIDL cao nhất",
    use_container_width=True
)



fig2, ax2 = plt.subplots(figsize=(8, 4))
top_states.plot(kind='bar', ax=ax2)
ax2.set_title("Top 10 Bang chịu ảnh hưởng kinh tế nặng nhất")
#  -thêm ảnh
ax2.set_ylabel("Tổng giá trị khoản vay ($)")
ax2.set_xlabel("Bang")
st.pyplot(fig2)

st.markdown("""
**Nhận xét:**
- Các bang đứng đầu có tổng giá trị khoản vay cao, phản ánh mức độ thiệt hại kinh tế nghiêm trọng.
- Đây là những khu vực cần sự hỗ trợ tài chính lớn trong thời kỳ COVID-19.
""")

# ----------------------
# 3. KẾT LUẬN CHUNG

header3 = "3. Kết luận tổng quan"
st.markdown(f"<h2 style='background:black; color:white'>{header3}</h2>", unsafe_allow_html=True)

st.success("""
🔹 Đại dịch COVID-19 đã gây ảnh hưởng nghiêm trọng đến hoạt động kinh tế tại nhiều bang ở Mỹ.  
🔹 Dữ liệu vay EIDL cho thấy mức độ hỗ trợ tài chính tập trung mạnh vào các khu vực chịu thiệt hại lớn.  
🔹 Mối tương quan giữa chi phí trợ cấp và giá trị khoản vay là cơ sở quan trọng để xây dựng mô hình dự đoán kinh tế.  
🔹 Phân tích này đóng vai trò tiền đề cho bước dự đoán bằng mô hình học máy ở phần tiếp theo.
""")
