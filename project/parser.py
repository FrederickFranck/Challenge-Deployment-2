import json
from game import Game


def main():
    data = 0
    with open("./data/database.json") as file:
        data = json.load(file)

    for item in data.items():
        game = Game(
            item["steam_appid"],
            item["name"],
            item["developers"][0],
            item["price_overview"]["final"],
            item["detailed_description"],
            item["platforms"]["windows"],
            item["platforms"]["mac"],
            item["platforms"]["Linux"],
            item["total_positive"],
            item["total_negative"],
        )


def parse():
    return


if __name__ == "__main__":
    main()
