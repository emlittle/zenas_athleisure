# Import python packages
import streamlit as st
from snowflake.snowpark.functions import col
import requests
import pandas as pd

# Write directly to the app
st.title("Zena's Amazing Athleisure Catalog")

cnx = st.connection('snowflake')
session = cnx.session
cursor = cnx.cursor()

cursor.execute("SELECT * FROM catalog_for_website")
my_dataframe = pd.DataFrame(cursor.fetchall(), columns=['color_or_style', 'price', 'file_name', 'file_url', 'size_list', 'upsell'])

style_chosen = st.selectbox('Pick a sweatsuit colour or style:', my_dataframe['color_or_style'])

if style_chosen:
  
  image = my_dataframe.loc[my_dataframe['color_or_style'] == style_chosen, 'file_url'].iloc[0]
  price = my_dataframe.loc[my_dataframe['color_or_style'] == style_chosen, 'price'].iloc[0]
  size_list = my_dataframe.loc[my_dataframe['color_or_style'] == style_chosen, 'size_list'].iloc[0]
  upsells = my_dataframe.loc[my_dataframe['color_or_style'] == style_chosen, 'upsell'].iloc[0]
  
  description = 'Our warm, comfortable, '+style_chosen+' sweatsuit!'
  st.image(image, width=400, caption=description)
  st.write('Price: $', price)
  st.write('Sizes Available: ', size_list)
  st.write(upsells)
