import streamlit as st

# Page settings
st.set_page_config(page_title="Interpolation Learning", page_icon="📈")

st.title("Interpolation Methods")
st.write("Learn about numerical interpolation and practice with examples.")

# Sidebar
st.sidebar.title("Topics")
topic = st.sidebar.radio(
    "Select Topic",
    ["Introduction", "Linear Interpolation", "Polynomial Interpolation"]
)

# Content
if topic == "Introduction":
    st.header("What is Interpolation?")
    st.write("""
    Interpolation is a method used in numerical analysis to estimate
    unknown values that fall between known data points.
    
    It is commonly used in:
    - Engineering
    - Data science
    - Graph analysis
    - Scientific computing
    """)

elif topic == "Linear Interpolation":
    st.header("Linear Interpolation")
    st.latex(r"y = y_1 + \frac{(x-x_1)}{(x_2-x_1)} (y_2-y_1)")
    st.write("""
    Linear interpolation assumes the data points form a straight line
    and estimates values between two known points.
    """)

elif topic == "Polynomial Interpolation":
    st.header("Polynomial Interpolation")
    st.write("""
    Polynomial interpolation fits a polynomial through a set of points.
    
    Common methods include:
    - Newton's Forward Interpolation
    - Newton's Backward Interpolation
    - Lagrange Interpolation
    """)

st.divider()

# Chatbot Button
chatbot_url = "https://cdn.botpress.cloud/webchat/v3.6/shareable.html?configUrl=https://files.bpcontent.cloud/2026/03/06/13/20260306133552-TPFY7SEH.json"

st.markdown(
    f"""
    <a href="{chatbot_url}" target="_blank">
        <button style="
            background-color:#4CAF50;
            color:white;
            padding:12px 24px;
            border:none;
            border-radius:8px;
            font-size:16px;
            cursor:pointer;">
            Ask Interpolation Chatbot
        </button>
    </a>
    """,
    unsafe_allow_html=True
)
