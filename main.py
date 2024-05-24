import streamlit as st 
import langchain_helper

st.title("Resturant name generator")

cuisine=st.sidebar.selectbox("Pick a cuisine", ("Indian", "Italian", "Mexican","German","Arabian"))



if cuisine:
    response = langchain_helper.get_resturant_name_and_items(cuisine)
    st.header(response['resturant_name'])
    menu_items = response['menu_items'].split(",")
    st.subheader("Menu Items")
    for items in menu_items:
        st.write(items)