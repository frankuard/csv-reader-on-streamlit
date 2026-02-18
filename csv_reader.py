import streamlit as st
import pandas as pd



st.markdown('<h1 class="app-title">CSV Reader</h1>', unsafe_allow_html=True)

uploaded_file = st.file_uploader("Upload CSV",type=["csv"])

df= pd.read_csv(uploaded_file)

st.dataframe(df)

if "column_entered" not in st.session_state:
    st.session_state.column_entered = False

ask_user_column = st.text_input("What would you like to view by?")



if st.button("Enter",key="key1"):
    st.session_state.column_entered = True

if st.session_state.column_entered:
    value= st.text_input("What value do you wanna view?")
    
    if st.button("Enter",key="key2"):
        if value.lower() == "all":
            st.dataframe(df[[ask_user_column]])
        else:
            st.dataframe(df[df[ask_user_column].astype(str)==value])

