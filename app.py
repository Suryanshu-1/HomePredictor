import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="HomePredictor",
    page_icon="🏡",
    layout="centered"
)

model = joblib.load("model.pkl")

# -----------------------------
# Custom CSS
# -----------------------------
st.markdown("""
<style>

/* ---------- Main Background ---------- */
.stApp{
    background: linear-gradient(135deg,#0f2027,#203a43,#2c5364);
    background-attachment: fixed;
}

/* ---------- Main Container ---------- */
.main > div{
    background: rgba(255,255,255,0.10);
    padding:40px;
    border-radius:20px;
    backdrop-filter: blur(15px);
    box-shadow:0 8px 32px rgba(0,0,0,0.35);
}

/* ---------- Title ---------- */
h1{
    color:white;
    text-align:center;
    font-size:42px;
    font-weight:700;
}

/* ---------- Labels ---------- */
label,
p{
    color:white !important;
    font-size:16px;
    font-weight:500;
}

/* ---------- Number Input ---------- */
.stNumberInput input{
    background: rgba(255,255,255,0.08) !important;
    color:white !important;
    border:1px solid rgba(255,255,255,0.25) !important;
    border-radius:10px !important;
}

.stNumberInput input:focus{
    border:1px solid #00C6FF !important;
    box-shadow:0 0 10px rgba(0,198,255,0.4);
}

/* ---------- Select Box ---------- */
div[data-baseweb="select"] > div{
    background: rgba(255,255,255,0.08) !important;
    color:white !important;
    border:1px solid rgba(255,255,255,0.25) !important;
    border-radius:10px !important;
}

/* Selected value */
div[data-baseweb="select"] span{
    color:white !important;
}

/* Dropdown menu */
div[role="listbox"]{
    background:#233847 !important;
    color:white !important;
}

div[role="option"]{
    color:white !important;
}

div[role="option"]:hover{
    background:#33556d !important;
}

/* ---------- Predict Button ---------- */
.stButton>button{
    width:100%;
    background:linear-gradient(90deg,#00c6ff,#0072ff);
    color:white;
    border:none;
    border-radius:12px;
    font-size:18px;
    font-weight:bold;
    padding:12px;
    transition:all 0.3s ease;
}

.stButton>button:hover{
    background:linear-gradient(90deg,#00dbde,#fc00ff);
    transform:translateY(-2px);
    box-shadow:0 8px 20px rgba(0,0,0,0.3);
}

/* ---------- Success Box ---------- */
.stAlert{
    border-radius:15px;
}

/* ---------- Remove Streamlit Header ---------- */
header{
    visibility:hidden;
}

footer{
    visibility:hidden;
}

</style>
""", unsafe_allow_html=True)

st.markdown(
    """
    <h1>🏡 HomePredictor</h1>
    <p style='text-align:center;color:white;font-size:18px'>
    Predict the market value of your dream home in seconds.
    </p>
    """,
    unsafe_allow_html=True
)
col1, col2 = st.columns(2)


with col1:
    area = st.number_input("Area (sq.ft)",1000,20000,5000)
    bedrooms = st.selectbox("Bedrooms",[1,2,3,4,5,6])
    bathrooms = st.selectbox("Bathrooms",[1,2,3,4])
    stories = st.selectbox("Stories",[1,2,3,4])
    parking = st.selectbox("Parking",[0,1,2,3])

with col2:
    mainroad = st.selectbox("Main Road",["yes","no"])
    guestroom = st.selectbox("Guest Room",["yes","no"])
    basement = st.selectbox("Basement",["yes","no"])
    hotwaterheating = st.selectbox("Hot Water Heating",["yes","no"])
    airconditioning = st.selectbox("Air Conditioning",["yes","no"])

prefarea = st.selectbox("Preferred Area",["yes","no"])

furnishingstatus = st.selectbox(
    "Furnishing Status",
    ["furnished","semi-furnished","unfurnished"]
)

if st.button("Predict House Price"):

    data = pd.DataFrame({
        "area":[area],
        "bedrooms":[bedrooms],
        "bathrooms":[bathrooms],
        "stories":[stories],
        "mainroad":[mainroad],
        "guestroom":[guestroom],
        "basement":[basement],
        "hotwaterheating":[hotwaterheating],
        "airconditioning":[airconditioning],
        "parking":[parking],
        "prefarea":[prefarea],
        "furnishingstatus":[furnishingstatus]
    })

    prediction = model.predict(data)[0]

    st.markdown(f"""
    <div style="
        background:linear-gradient(135deg,#00c9ff,#92fe9d);
        padding:25px;
        border-radius:18px;
        text-align:center;
        color:black;
        font-size:28px;
        font-weight:bold;
        margin-top:20px;">
        Estimated House Price<br>
        ₹ {prediction:,.2f}
    </div>
    """, unsafe_allow_html=True)