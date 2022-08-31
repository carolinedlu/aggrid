import streamlit as st
import pandas as pd
from st_aggrid import AgGrid

df = pd.DataFrame({'col1': [1, 2, 3], 'col2': [4, 5, 6]})
grid_return = AgGrid(df, editable=True)
new_df = grid_return['data']


def exp_list():
    st.session_state['exp_list'] = ['2001','2002','2003']

first_sb = st.selectbox('please select an option', options= ['option1'], key ='first_sb', on_change=exp_list)
second_sb = st.selectbox('please select a year', options= ['option1','option2'], key ='second_sb')
