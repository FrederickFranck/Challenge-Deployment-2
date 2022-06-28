import streamlit as st
import project.database as db
import pandas as pd


# Streamlit session state init
if "selected_game" not in st.session_state:
    st.session_state["selected_game"] = "Null"

if "select_main" not in st.session_state:
    st.session_state["select_main"] = 0

if "selected_genres" not in st.session_state:
    st.session_state["selected_genres"] = []

if "selected_categories" not in st.session_state:
    st.session_state["selected_categories"] = []

st.set_page_config(layout="wide")
st.title("""Welcome to the Steam Visualization App """)
st.write("""This app is designed to visualize the data from the Steam API.""")


_connection = db.connect()
games = db.get_games(_connection)

game_ids = [list(game.values())[0] for game in games]
game_names = [list(game.keys())[0] for game in games]


def get_genre_ids() -> list[int]:
    ids = []
    for selected_genre in st.session_state["selected_genres"]:
        genre_id = [
            list(genre.values())[0]
            for genre in genres
            if list(genre.keys())[0] == selected_genre
        ][0]
        ids.append(genre_id)
    return ids


def get_category_ids() -> list[int]:
    ids = []
    for selected_category in st.session_state["selected_categories"]:
        category_id = [
            list(category.values())[0]
            for category in categories
            if list(category.keys())[0] == selected_category
        ][0]
        ids.append(category_id)
    return ids


start = False
if start:
    st.header("Select genres or categories")
    st.session_state["select_main"] = st.selectbox(
        "Select a category or genre",
        ["Genres", "Categories"],
    )
    st.markdown("##")

    if st.session_state["select_main"] == "Genres":

        # Plot Game by Genre
        df = pd.DataFrame(db.get_genres_count(_connection))
        df.columns = ["Genre", "Count"]
        df.set_index("Genre", inplace=True)
        st.bar_chart(df)

    if st.session_state["select_main"] == "Categories":

        # Plot Games by Category
        df = pd.DataFrame(db.get_categories_count(_connection))
        df.columns = ["Category", "Count"]
        df.set_index("Category", inplace=True)
        st.bar_chart(df)


st.title("Find your perfect game")

genre_select_col, category_select_col = st.columns(2)
game_names = [list(game.keys())[0] for game in games]
final = pd.DataFrame(game_names)
final[1] = True
final.set_index(0, inplace=True)
st.session_state["final_df"] = final
dataframes = []

with genre_select_col:
    # Create Select Box for Genres
    genres = db.get_genres(_connection)
    st.header("Select a genre")
    genre_names = [list(genre.keys())[0] for genre in genres]
    st.session_state["selected_genres"] = st.multiselect("Select genres", genre_names)

    for _genre_id in get_genre_ids():
        games = db.get_games_by_genre(_genre_id, _connection)

        game_names = pd.DataFrame([list(game.keys())[0] for game in games])
        game_names[1] = True
        game_names.set_index(0, inplace=True)
        dataframes.append(game_names)


with category_select_col:
    # Create Select Box for Categories
    # Create Selectionbox for Categories
    categories = db.get_categories(_connection)
    st.header("Select a category")
    category_names = [list(category.keys())[0] for category in categories]
    st.session_state["selected_categories"] = st.multiselect(
        "Select categories", category_names
    )

    for _category_id in get_category_ids():
        games = db.get_games_by_category(_category_id, _connection)

        game_names = pd.DataFrame([list(game.keys())[0] for game in games])
        game_names[1] = True
        game_names.set_index(0, inplace=True)
        dataframes.append(game_names)

st.markdown("##")


for dataframe in dataframes:
    final = final.join(dataframe, how="inner", lsuffix="_left", rsuffix="_right")

final.reset_index(inplace=True)
final.drop(columns=final.columns[1:], inplace=True)

final_list = final[0].tolist()


game_select_col, game_info_col, ratings = st.columns(3)
selected_game = None
with game_select_col:

    if len(final_list) <= 500:
        selected_game = st.radio("Select a game", final_list)

    else:
        st.write("Too many games to display, please select a genre or category")
with game_info_col:
    if selected_game != None:
        print(selected_game)
        game_id = [
            list(game.values())[0]
            for game in games
            if list(game.keys())[0] == selected_game
        ][0]
        supported_platforms = pd.DataFrame(
            db.get_supported_platforms(game_id, _connection)
        )
        game_genres = pd.DataFrame(db.get_game_genres(game_id, _connection))
        game_categories = pd.DataFrame(db.get_game_categories(game_id, _connection))
        supported_platforms.columns = ["Windows", "Mac", "Linux"]

        st.header("Supported Platforms")
        st.markdown(
            "- " + "Windows : " + ("yes" if supported_platforms["Windows"][0] else "no")
        )
        st.markdown(
            "- " + "Mac : " + ("yes" if supported_platforms["Mac"][0] else "no")
        )
        st.markdown(
            "- " + "Linux : " + ("yes" if supported_platforms["Linux"][0] else "no")
        )
        st.markdown("##")

        st.header("Genres")
        game_genres = game_genres[0].tolist()
        for genre in game_genres:
            st.markdown("- " + genre)
        st.markdown("##")

        st.header("Categories")
        game_categories = game_categories[0].tolist()
        for category in game_categories:
            st.markdown("- " + category)
        st.markdown("##")
    else:
        st.write("No game selected")

with ratings:
    if selected_game != None:
        game_id = [
            list(game.values())[0]
            for game in games
            if list(game.keys())[0] == selected_game
        ][0]
        ratings = pd.DataFrame(db.get_game_ratings(game_id, _connection))
        ratings.columns = ["Positive", "Negative"]
        st.header("Ratings")
        st.bar_chart(ratings)
    else:
        st.write("No game selected")
