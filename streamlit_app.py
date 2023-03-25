import streamlit
import pandas
streamlit.title('My Parents New Healthy Diner')
streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega3 & blueberry oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard boiled free range egg')
streamlit.text('🥑🍞 Avocado toast')
streamlit.header('🍌🥭 Build your own fruit smoothie 🥑🍞')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt"
streamlit.dataframe(my_fruit_list)
