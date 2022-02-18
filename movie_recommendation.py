import streamlit as st
import requests
import pickle

with open('movies_details.pkl', 'rb') as f:
    movies_details = pickle.load(f)

with open('similarity_index.pkl', 'rb') as f:
    similarity_index = pickle.load(f)

st.title("MOVIE RECOMMENDATION")

selected_movie = st.selectbox(
    'Select The Movie You Watched', movies_details['title'])

if st.button('Submit'):
    movie_index = movies_details[movies_details['title']
                                 == selected_movie].index[0]

    top_5_index = similarity_index[movie_index]

    # col = []
    col = st.columns(4)

    # for i in top_5_index:
    for i in range(4):
        name = movies_details.title.iloc[top_5_index[i]]
        movie_id = str(movies_details.id.iloc[top_5_index[i]])

        url = "https://api.themoviedb.org/3/movie/" + \
            str(movie_id)+"?api_key=27f0aae8b133e8670d538a3b3ca928ba&language=en-US"

        response = requests.get(url)
        json = response.json()

        poster = json['poster_path']
        image = "https://image.tmdb.org/t/p/original/"+poster

        with col[i]:
            st.subheader(name)
            st.image(image)
