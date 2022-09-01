import streamlit as st
import pandas as pd
from st_aggrid import AgGrid

df = pd.DataFrame({'col1': [1, 2, 3], 'col2': [4, 5, 6]})
grid_return = AgGrid(df, editable=True)
new_df = grid_return['data']


# def on_change():
# #     st.session_state['exp_list'] = ['2001','2002','2003']
#     st.write("on change function called")

# first_sb = st.selectbox('please select an option', options= ['option1'], key ='first_sb', on_change=on_change)
# second_sb = st.selectbox('please select a year', options= ['option1','option2'], key ='second_sb')

# if first_sb:
#     st.write(first_sb)
