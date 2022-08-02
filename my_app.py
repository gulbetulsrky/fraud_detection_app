import streamlit as st
import numpy as np
import pandas as pd
import pickle
from PIL import Image



model = pickle.load(open("rf_model.pkl", "rb"))
image = Image.open('img 7.jpg')
html_temp = """
<div style="background-color:Blue;padding:10px">
<h2 style="color:white;text-align:center;">Fraud Detection - GROUP-9 </h2>
</div><br>"""
st.set_page_config(page_title='Fraud Detection', page_icon='👩‍💻')
st.image(image)
st.markdown('***')
st.markdown('# <center><span style="color:#286608">Fraud Detection</span></center>',unsafe_allow_html=True )
st.markdown("#### <center>Use the sidebar to enter required informations.</center>",unsafe_allow_html=True)
st.markdown('***')

# columns = ["v14", ‘v17’, ‘v12’, ‘v10’, ‘v11’, ‘v4’, ‘v3’, ‘v7’, ‘v16’]
v3 = st.sidebar.slider(label="v3", min_value=-49.00, max_value=10.00, step=0.01)
v4 = st.sidebar.slider(label="v4", min_value=-6.00, max_value=17.00, step=0.01)
v7 = st.sidebar.slider(label="v7", min_value=-44.00, max_value=121.00, step=0.01)
v10 = st.sidebar.slider(label="v10", min_value=-25.00, max_value=24.00, step=0.01)
v11 = st.sidebar.slider("v11", min_value=-5.00, max_value=13.00, step=0.01)
v12 = st.sidebar.slider("v12", min_value=-19.00, max_value=8.00, step=0.01)
v14 = st.sidebar.slider("v14", min_value=-20.00, max_value=11.00, step=0.01)
v16 = st.sidebar.slider("v16", min_value=-15.00, max_value=18.00, step=0.01)
v17 = st.sidebar.slider("v17", min_value=-26.00, max_value=10.00, step=0.01)

fraud = pd.DataFrame({"v14":[v14], "v17":[v17], "v12":[v12], "v10":[v10], "v11":[v11], "v4":[v4], "v3":[v3], "v7":[v7], "v1":[v16]})

hide_table_row_index = """
            <style>
            tbody th {display:none}
            .blank {display:none}
            </style>
            """        
st.markdown(hide_table_row_index, unsafe_allow_html=True)   

st.markdown("#### <center>Transaction Information</center>",unsafe_allow_html=True)
st.table(fraud)

prediction = model.predict(fraud)


st.subheader('Click PREDICT if configuration is OK')

if st.button('PREDICT'):
	if prediction[0]==0:
		st.success(prediction[0])
		st.success(f'It is a non fraudulent transaction.')
	elif prediction[0]==1:
		st.warning(prediction[0])
		st.warning(f'It is a fraudulent transaction.')


hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
