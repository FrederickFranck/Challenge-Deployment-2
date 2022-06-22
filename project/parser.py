import json
import pathlib
import logging
from pprint import pprint
import sys

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

        try:
            _price = item["price_overview"]["final"]

        except:
            _price = 0

        try:
            game = Game(
                item["steam_appid"],
                item["name"],
                item["developers"][0],
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

        games.append(game)
    return games


if __name__ == "__main__":
    main()
