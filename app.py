import streamlit as st

st.set_page_config(page_title="Interpolation", page_icon="📊", layout="centered")

# ---------- Modern CSS Styling ----------
st.markdown("""
<style>

.stApp{
background: linear-gradient(180deg,#EAF3FF,#D4E6FF,#F4F9FF);
font-family: 'Segoe UI', sans-serif;
}

.main-title{
font-size:50px;
font-weight:700;
text-align:center;
color:#1A3A6E;
margin-bottom:8px;
}

.subtitle{
text-align:center;
font-size:20px;
color:#3B4A6B;
margin-bottom:40px;
}

.section-card{
background:white;
padding:30px;
border-radius:14px;
margin-bottom:25px;
box-shadow:0px 6px 18px rgba(0,0,0,0.08);
border-left:6px solid #3A7BD5;
}

.section-title{
font-size:24px;
font-weight:600;
color:#1A3A6E;
margin-bottom:10px;
}

.section-text{
font-size:17px;
line-height:1.7;
color:#333333;
}

.chat-container{
text-align:center;
margin-top:40px;
}

.chat-btn{
background: linear-gradient(90deg,#3A7BD5,#00B4DB);
color:white;
padding:15px 32px;
font-size:18px;
border:none;
border-radius:10px;
cursor:pointer;
box-shadow:0px 4px 10px rgba(0,0,0,0.15);
}

.chat-btn:hover{
transform:scale(1.05);
}

</style>
""", unsafe_allow_html=True)

# ---------- Title ----------
st.markdown('<div class="main-title">Interpolation</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Understanding Numerical Interpolation</div>', unsafe_allow_html=True)

# ---------- Section 1 ----------
st.markdown("""
<div class="section-card">
<div class="section-title">What is Interpolation?</div>
<div class="section-text">
Interpolation is a mathematical technique used to estimate unknown values
between known data points. In many scientific and real-world situations,
data is only available at specific intervals. Interpolation helps construct
a smooth and meaningful estimate of values that fall between these points.

By analysing existing data and applying mathematical formulas,
interpolation creates a continuous function that approximates the trend
of the data. This makes it possible to predict intermediate values
with reasonable accuracy.
</div>
</div>
""", unsafe_allow_html=True)

# ---------- Section 2 ----------
st.markdown("""
<div class="section-card">
<div class="section-title">Why is Interpolation Important?</div>
<div class="section-text">
In real-world applications, measurements are often limited and cannot be
recorded for every possible value. Interpolation allows scientists and
engineers to estimate missing values and analyse patterns within the data.

It plays a crucial role in fields such as scientific computing,
engineering simulations, weather forecasting, economics, and
data science. By filling the gaps between known data points,
interpolation helps create models that represent real-world
phenomena more accurately.
</div>
</div>
""", unsafe_allow_html=True)

# ---------- Section 3 ----------
st.markdown("""
<div class="section-card">
<div class="section-title">Common Types of Interpolation</div>
<div class="section-text">

• Linear Interpolation – Uses a straight line between two known points.  
• Polynomial Interpolation – Fits a polynomial curve through multiple data points.  
• Lagrange Interpolation – Constructs a polynomial that passes through all given points.

Different interpolation methods are used depending on the number
of data points available and the level of accuracy required.
</div>
</div>
""", unsafe_allow_html=True)

# ---------- Section 4 ----------
st.markdown("""
<div class="section-card">
<div class="section-title">Applications of Interpolation</div>
<div class="section-text">
Interpolation is widely used in engineering design, scientific experiments,
data analysis, and computer graphics. It helps approximate unknown values
in datasets, create smooth curves in graphical applications, and estimate
missing information in research studies.

Modern technologies such as GPS navigation, animation systems,
and predictive data models rely heavily on interpolation
to generate continuous and meaningful results.
</div>
</div>
""", unsafe_allow_html=True)

# ---------- Chatbot ----------
chatbot_url = "https://cdn.botpress.cloud/webchat/v3.6/shareable.html?configUrl=https://files.bpcontent.cloud/2026/03/06/13/20260306133552-TPFY7SEH.json"

st.markdown(
f"""
<div class="chat-container">
<a href="{chatbot_url}" target="_blank">
<button class="chat-btn">Ask the Interpolation Chatbot</button>
</a>
</div>
""",
unsafe_allow_html=True
)
