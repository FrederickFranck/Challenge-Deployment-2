import streamlit as st
import pandas as pd
import project.database as db

st.set_page_config(layout="wide")

_connection = db.connect()

games = db.get_games(_connection)
# Create a list of names of games
names = [list(game.keys())[0] for game in games]


def select_game():
    for game in games:
        if game_name in game:
            _game = db.get_game_by_id(game[game_name], _connection)

            return st.write(_game)

    return


st.write(
    """Hello There ! This is a Streamlit App that will help you to find the best games for you. """
)

game_name = st.selectbox("Game ? ", names, on_change=select_game)
