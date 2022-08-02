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

# columns = [‘v14’, ‘v17’, ‘v12’, ‘v10’, ‘v11’, ‘v4’, ‘v3’, ‘v7’, ‘v16’]
v3 = st.sidebar.slider(label="v3", min_value=-48.326, max_value=9.383, step=0.01)
v4 = st.sidebar.slider(label="v4", min_value=-5.683, max_value=16.875, step=0.01)
v7 = st.sidebar.slider(label="v7", min_value=-43.557, max_value=120.589, step=1)
v10 = st.sidebar.slider(label="v10", min_value=-24.588, max_value=23.745, step=10)
v11 = st.sidebar.slider("v11", min_value=1, max_value=10, step=1)
v12 = st.sidebar.slider("v12", min_value=1, max_value=10, step=1)
v14 = st.sidebar.slider("v14", min_value=1, max_value=10, step=1)
v16 = st.sidebar.slider("v16", min_value=1, max_value=10, step=1)
v17 = st.sidebar.slider("v17", min_value=1, max_value=10, step=1)

# fraud = pd.DataFrame({"satisfaction_level" : [satisfaction_level],
                   # "last_evaluation" : [last_evaluation],
                    #"number_project" : [number_project],
                    #"average_montly_hours" : [average_montly_hours],
                    #"time_spend_company" : [time_spend_company],
                    #})

hide_table_row_index = """
            <style>
            tbody th {display:none}
            .blank {display:none}
            </style>
            """        
st.markdown(hide_table_row_index, unsafe_allow_html=True)   

#showdf = fraud.rename(columns={'satisfaction_level': 'Satisfaction Level',
 #                            'last_evaluation': 'Last Evaluation',
  #                           'number_project': 'Number Of Project',
   #                          'average_montly_hours': 'Average Monthly Hours',
    #                         'time_spend_company': 'Time Spend in Company'})
st.markdown("#### <center>Transaction Information</center>",unsafe_allow_html=True)
#st.table(fraud)

#prediction = model.predict(fraud)


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
