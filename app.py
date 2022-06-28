from numpy import inner
import streamlit as st
import project.database as db
import pandas as pd


# Streamlit session state init
if "selected_game" not in st.session_state:
    st.session_state["selected_game"] = "Null"
    
if "select_main" not in st.session_state:
    st.session_state["select_main"] = 0
    
if "selected_genre" not in st.session_state:
    st.session_state["selected_genre"] = 0

if "selected_category" not in st.session_state:
    st.session_state["selected_category"] = 0

if "selected_genres" not in st.session_state:
    st.session_state["selected_genres"] = [] 
    
if "selected_categories" not in st.session_state:
    st.session_state["selected_categories"] = [] 

st.set_page_config(layout="wide")
st.title("""Welcome to the Steam Visualization App """)
st.write("""This app is designed to visualize the data from the Steam API.""")
st.header("Select genres or categories")

_connection = db.connect()


games = db.get_games(_connection)
st.write(games[0])
game_ids = [list(game.values())[0] for game in games]
game_names = [list(game.keys())[0] for game in games]
st.write(game_ids[0])
ratings = db.get_game_ratings(game_ids[0], _connection)
supports = db.get_game_supported_platforms(game_ids[0], _connection)
st.write(ratings)
st.write(supports)


def get_genre_ids() -> list[int]:
    ids = []
    for selected_genre in st.session_state["selected_genres"]:
        genre_id = [list(genre.values())[0] for genre in genres if list(genre.keys())[0] == selected_genre][0]
        ids.append(genre_id)
    return ids

def get_category_ids() -> list[int]:
    ids = []
    for selected_category in st.session_state["selected_categories"]:
        category_id = [list(category.values())[0] for category in categories if list(category.keys())[0] == selected_category][0]
        ids.append(category_id)
    return ids


st.session_state["select_main"] = st.selectbox("Select a category or genre", ['Genres', 'Categories'],)
st.write("")
st.write("")
st.write("")


if st.session_state["select_main"] == "Genres":
    
    #Plot Game by Genre
    df = pd.DataFrame(db.get_genres_count(_connection))
    df.columns = (['Genre', 'Count'])
    df.set_index('Genre', inplace=True)
    st.bar_chart(df)
    
    
    
if st.session_state["select_main"] == "Categories":
    
    #Plot Games by Category
    df = pd.DataFrame(db.get_categories_count(_connection))
    df.columns = ['Category', 'Count']
    df.set_index('Category', inplace=True)
    st.bar_chart(df)
    
    


col1, col2 = st.columns(2)
game_names = [list(game.keys())[0] for game in games]
final = pd.DataFrame(game_names)
final[1] = True
final.set_index(0, inplace=True)
st.session_state["final_df"] = final
dataframes = []
#COL1
with col1:
    #Create Select Box for Genres
    genres = db.get_genres(_connection)
    st.header("Select a genre")    
    genre_names = [list(genre.keys())[0] for genre in genres]
    st.session_state["selected_genres"] = st.multiselect("Select a genre", genre_names)

    
    for _genre_id in get_genre_ids():
        games = db.get_games_by_genre(_genre_id, _connection)
        
        game_names = pd.DataFrame([list(game.keys())[0] for game in games])
        game_names[1] = True
        game_names.set_index(0, inplace=True)
        dataframes.append(game_names)


with col2:
    #Create Select Box for Categories
    #Create Selectionbox for Categories
    categories = db.get_categories(_connection)
    st.header("Select a category")
    category_names = [list(category.keys())[0] for category in categories]
    st.session_state["selected_categories"] = st.multiselect("Select a category", category_names)
    
    for _category_id in get_category_ids():
        games = db.get_games_by_category(_category_id, _connection)
        
        game_names = pd.DataFrame([list(game.keys())[0] for game in games])
        game_names[1] = True
        game_names.set_index(0, inplace=True)
        dataframes.append(game_names)
        



for dataframe in dataframes:
    final = final.join(dataframe,how='inner',lsuffix='_left', rsuffix='_right')
    
final.reset_index(inplace=True)
final.drop(columns = final.columns[1:],inplace=True)
st.write(final)

