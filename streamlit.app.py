
import streamlit
streamlit.title(' My Parents New Healthy diner')
streamlit.header('🥣 Breakfast Favroites')
streamlit.text(' 🥣Omega 3 and blueberry oatmeal')
streamlit.text(' 🥗Kale, spinach and Rocket smoothie')
streamlit.text('🐔Hard Boiled Free-Range egg')
streamlit.text('🥑🍞 Avacado toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


import pandas
my_fruit_list = pandas.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
my_fruit_list = my_fruit_list.set_index('Fruit')
         
# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]


# Display the table on the page.
streamlit.dataframe(my_fruit_list)


streamlit.header("Fruityvice Fruit Advice!")

import requests
import pandas 
fruityvice_response=requests.get("https://fruityvice.com/api/fruit/kiwi")
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
streamlit.dataframe(fruityvice_normalized)
import snowflake.connector
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
#my_cur.execute("select * from pc_rivery_db.public.fruit_load_list")
my_cur.execute("insert into fruis load list values('from streamlit')")

my_data_row = my_cur.fetchall()
streamlit.header("The fruit load list contain:")
streamlit.dataframe(my_data_row)

#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/Kiwi")
#streamlit.text(fruityvice_response.json())


# take the json verion of respone for normalized it.
#fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# output it the screnn as table.
#streamlit.dataframe(fruityvice_normalized)




