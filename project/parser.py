import json
import pathlib
import logging
from pprint import pprint
import sys
from typing import Tuple
from unicodedata import category

from .game import Game


def main():
    return


database_file = pathlib.Path(__file__).parent / "./data/database.json"


def parse() -> list[Game]:
    games = []
    data = 0
    with open(database_file) as file:
        data = json.load(file)

    for item in data.items():
        item = item[1]

        # Get correct price
        if "price_overview" in item:
            _price = item["price_overview"]["final"]

        elif "is_free" in item:
            if item["is_free"]:
                _price = 0
            else:
                _price = -100

        # Get correct developers name
        if "developer" in item:
            _developer = item["developer"][0]

        elif "developers" in item:
            _developer = item["developers"][0]

        else:
            _developer = None

        try:
            game = Game(
                item["steam_appid"],
                item["name"],
                _developer,
                _price,
                item["detailed_description"],
                item["platforms"]["windows"],
                item["platforms"]["mac"],
                item["platforms"]["linux"],
                item["total_positive"],
                item["total_negative"],
            )
        except Exception as e:
            logging.error(f"{__name__:<15} Parsing Game {item['name']} Json: {e}")

        # get genres & categories
        if "genres" in item:
            genres = item["genres"]
            for genre in genres:
                game.add_genre((genre["id"], genre["description"]))

        if "categories" in item:
            categories = item["categories"]
            for category in categories:
                game.add_category((category["id"], category["description"]))

        games.append(game)
    return games


def extract_genres(games: list[Game]) -> list[Tuple[int, str]]:
    genres = []
    for game in games:
        for genre in game.genres:
            if genre not in genres:
                genres.append(genre)

    return genres


def extract_categories(games: list[Game]) -> list[Tuple[int, str]]:
    categories = []
    for game in games:
        for category in game.categories:
            if category not in categories:
                categories.append(category)

    return categories


if __name__ == "__main__":
    main()
