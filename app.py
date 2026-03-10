import streamlit as st

st.set_page_config(page_title="Interpolation Learning", page_icon="📊", layout="centered")

# Custom CSS for professional design
st.markdown("""
<style>

.main-title{
font-size:42px;
font-weight:700;
text-align:center;
color:#1F4E8C;
margin-bottom:10px;
}

.subtitle{
text-align:center;
font-size:18px;
color:#555;
margin-bottom:40px;
}

.card{
background-color:#F8FBFF;
padding:35px;
border-radius:12px;
box-shadow:0px 4px 12px rgba(0,0,0,0.08);
font-size:17px;
line-height:1.7;
}

.chat-button{
display:flex;
justify-content:center;
margin-top:40px;
}

.chat-button button{
background-color:#1F4E8C;
color:white;
padding:14px 28px;
font-size:18px;
border:none;
border-radius:8px;
cursor:pointer;
}

.chat-button button:hover{
background-color:#163B6B;
}

</style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="main-title">Interpolation</div>', unsafe_allow_html=True)

st.markdown('<div class="subtitle">Understanding Numerical Interpolation</div>', unsafe_allow_html=True)

# Introduction Card
st.markdown("""
<div class="card">

Interpolation is an important concept in numerical analysis used to estimate
unknown values that lie between known data points. When we have a set of
discrete observations, interpolation allows us to construct new values within
the range of the available data.

In many real-world situations, data is collected at specific points, but we
often need to determine values that fall between those points. Interpolation
provides mathematical techniques that approximate these intermediate values
with reasonable accuracy.

For example, if we know the temperature recorded at 10:00 AM and 12:00 PM,
interpolation can help estimate the temperature at 11:00 AM. This concept is
widely applied in scientific computing, engineering simulations, data
analysis, computer graphics, and economic forecasting.

Several interpolation methods exist depending on the complexity and number
of data points available. Some of the most common methods include:

• Linear Interpolation – estimates values using a straight line between two points  
• Polynomial Interpolation – fits a polynomial curve through multiple points  
• Lagrange Interpolation – constructs a polynomial passing through given data points  

By using these methods, interpolation helps create continuous approximations
from discrete data, making it an essential tool in computational mathematics.

</div>
""", unsafe_allow_html=True)

# Chatbot Button
chatbot_url = "https://cdn.botpress.cloud/webchat/v3.6/shareable.html?configUrl=https://files.bpcontent.cloud/2026/03/06/13/20260306133552-TPFY7SEH.json"

st.markdown(
    f"""
    <div class="chat-button">
        <a href="{chatbot_url}" target="_blank">
            <button>Ask the Interpolation Chatbot</button>
        </a>
    </div>
    """,
    unsafe_allow_html=True
)
