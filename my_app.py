import streamlit as st
import numpy as np
import pandas as pd
import pickle
from PIL import Image



model = pickle.load(open("rf_model.pkl", "rb"))
df = pd.read_csv("creditcard.csv")
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


# satisfaction_level = st.sidebar.slider(label="Satisfaction Level", min_value=0.0, max_value=1.0, step=0.01)
# last_evaluation = st.sidebar.slider(label="Last Evaluation", min_value=0.0, max_value=1.0, step=0.01)
# number_project = st.sidebar.slider(label="Number Of Project", min_value=0, max_value=10, step=1)
# average_montly_hours = st.sidebar.slider(label="Average Monthly Hours", min_value=0, max_value=350, step=10)
# time_spend_company = st.sidebar.slider("Time Spend in Company", min_value=1, max_value=10, step=1)

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
