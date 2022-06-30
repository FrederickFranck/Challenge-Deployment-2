import logging
import pathlib
import database
from parser import extract_categories, extract_genres, parse

logging.basicConfig(
    format="%(asctime)s:%(levelname)s:%(message)s",
    datefmt="%d/%m/%Y %H:%M:%S ",
    filename=pathlib.Path(__file__).parent / "../logs/app.log",
    level=logging.DEBUG,
)


def main():
    # Parse the json to extract all games
    games = parse()

    # Connect to Database
    conn = database.connect()

    # Extract genres from all the games & insert them into the database
    database.insert_genres(extract_genres(games), conn)

    # Extract categories from all the games & insert them into the database
    database.insert_categories(extract_categories(games), conn)

    # Insert all the games & their relation to categories and genres into the database
    database.insert_games(games, conn)

    # Close the connection to the database
    database.disconnect(conn)


if __name__ == "__main__":
    main()
