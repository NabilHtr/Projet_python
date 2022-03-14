import pandas as pd 
import streamlit as st  
import numpy as np


df = pd.read_csv('Films.csv')

st.title('Dataframe top 100 Films')
st.dataframe(df)

st.title('Lineplot des rating')
st.line_chart(df['rating'])


st.title('Séléction des Films selon leur classement')
x = st.slider('x')  # 👈 this is a widget
st.dataframe(df[df['ranking'] <= x+1])


st.title('Recherche de films')
st.text_input("Chercher film", key="film")


# You can access the value at any point with:
st.dataframe(df[df['title'] == st.session_state.film])


st.title('Insertion d\'un film')

st.text_input("Ajouter du film", key="film2")
st.text_input("Ajouter rating", key="rating")
st.text_input("Ajouter ranking", key="ranking")
st.text_input("Ajouter director", key="director")
st.text_input("Ajouter actors", key="actors")
st.text_input("Ajouter country", key="country")
st.text_input("Ajouter language", key="language")
st.text_input("Ajouter date_sortie", key="date_sortie")
st.text_input("Ajouter production", key="production")
st.text_input("Ajouter synopsis", key="synopsis")



row = {
        'title' : st.session_state.film2,
        'rating' : st.session_state.rating,
        'ranking' : st.session_state.ranking,
        'director' : st.session_state.director,
        'actors' : st.session_state.actors,
        'country' : st.session_state.country,
        'language' : st.session_state.language,
        'date_sortie' : st.session_state.date_sortie,
        'production' : st.session_state.production,
        'synopsis' : st.session_state.synopsis
    }

df = df.append(row, ignore_index=True)

st.dataframe(df[df['title'] == st.session_state.film2])