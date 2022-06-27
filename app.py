import streamlit as st
import project.database as db

# Streamlit session state init
if "selected_game" not in st.session_state:
    st.session_state["selected_game"] = "Null"
    
if "select_main" not in st.session_state:
    st.session_state["select_main"] = 0
    
if "selected_genre" not in st.session_state:
    st.session_state["selected_genre"] = 0

if "selected_category" not in st.session_state:
    st.session_state["selected_category"] = 0
    

st.set_page_config(layout="wide")
st.title("""Welcome to the Steam Visualization App """)
st.write("""This app is designed to visualize the data from the Steam API.""")
st.header("Select genres or categories")

_connection = db.connect()


games = db.get_games(_connection)
st.write(games[0])
game_ids = [list(game.values())[0] for game in games]
st.write(game_ids[0])
ratings = db.get_game_ratings(game_ids[0], _connection)
supports = db.get_game_supported_platforms(game_ids[0], _connection)
st.write(ratings)
st.write(supports)

st.session_state["select_main"] = st.selectbox("Select a category or genre", ['Genres', 'Categories'],)


if st.session_state["select_main"] == "Genres":
    genres = db.get_genres(_connection)
    st.header("Select a genre")
    
    genre_names = [list(genre.keys())[0] for genre in genres]
    st.session_state["selected_genre"] = st.selectbox("Select a genre", genre_names)
    
if st.session_state["select_main"] == "Categories":
    categories = db.get_categories(_connection)
    st.header("Select a category")
    
    category_names = [list(category.keys())[0] for category in categories]
    st.session_state["selected_category"] = st.selectbox("Select a category", category_names)
