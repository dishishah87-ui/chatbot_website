import streamlit as st

st.set_page_config(page_title="Interpolation", page_icon="📈", layout="centered")

# --------- Custom Styling ----------
st.markdown("""
<style>

.main-title{
font-size:48px;
font-weight:700;
text-align:center;
color:#1F4E8C;
margin-bottom:5px;
}

.subtitle{
text-align:center;
font-size:20px;
color:#4A4A4A;
margin-bottom:40px;
}

.section-card{
background-color:#F7FAFF;
padding:28px;
border-radius:12px;
margin-bottom:20px;
box-shadow:0px 4px 12px rgba(0,0,0,0.08);
}

.section-title{
font-size:24px;
font-weight:600;
color:#1F4E8C;
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
background-color:#1F4E8C;
color:white;
padding:14px 30px;
font-size:18px;
border:none;
border-radius:8px;
cursor:pointer;
}

.chat-btn:hover{
background-color:#163B6B;
}

</style>
""", unsafe_allow_html=True)

# --------- Title ----------
st.markdown('<div class="main-title">Interpolation</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">An Introduction to Numerical Interpolation</div>', unsafe_allow_html=True)

# --------- Section 1 ----------
st.markdown("""
<div class="section-card">
<div class="section-title">What is Interpolation?</div>
<div class="section-text">
Interpolation is a fundamental concept in numerical analysis used to estimate
unknown values that lie between known data points. When we collect data in
experiments or observations, the values are often recorded only at specific
points. However, real-world analysis frequently requires values in between
those recorded measurements.

Interpolation provides mathematical techniques to construct these missing
values in a logical and accurate way. By using known data points, interpolation
creates a continuous function that approximates the behaviour of the data.
</div>
</div>
""", unsafe_allow_html=True)

# --------- Section 2 ----------
st.markdown("""
<div class="section-card">
<div class="section-title">Why is Interpolation Important?</div>
<div class="section-text">
Interpolation plays an essential role in many areas of science and technology.
In engineering and scientific computing, measurements are rarely available for
every possible value. Interpolation helps fill these gaps and allows
researchers to make predictions based on existing data.

It is widely used in weather prediction, computer graphics, machine learning,
economic forecasting, and data analysis. Without interpolation, many systems
that rely on continuous data modelling would not function effectively.
</div>
</div>
""", unsafe_allow_html=True)

# --------- Section 3 ----------
st.markdown("""
<div class="section-card">
<div class="section-title">Common Types of Interpolation</div>
<div class="section-text">
Different interpolation methods are used depending on the number of data
points and the required accuracy. Some of the most commonly used techniques
include:

• Linear Interpolation – Estimates values using a straight line between two known points.  
• Polynomial Interpolation – Uses higher-degree polynomials to fit multiple data points.  
• Lagrange Interpolation – Constructs a polynomial that passes exactly through all given data points.  

Each method has its own advantages and is chosen based on the nature of the
problem being solved.
</div>
</div>
""", unsafe_allow_html=True)

# --------- Section 4 ----------
st.markdown("""
<div class="section-card">
<div class="section-title">Applications of Interpolation</div>
<div class="section-text">
Interpolation is applied in many real-world scenarios. Engineers use it to
estimate structural behaviour between measured points, while scientists apply
it to approximate values in experimental datasets.

It is also essential in computer graphics for smooth animations, in GPS
systems for location estimation, and in data science for analysing incomplete
datasets. Because of its ability to approximate unknown values, interpolation
has become a critical tool in modern computational methods.
</div>
</div>
""", unsafe_allow_html=True)

# --------- Chatbot Button ----------
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
