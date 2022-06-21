import logging
import pathlib

import project.database
from project.parser import parse

logging.basicConfig(
    format="%(asctime)s:%(levelname)s:%(message)s",
    datefmt="%d/%m/%Y %H:%M:%S ",
    filename=pathlib.Path(__file__).parent / "logs/app.log",
    level=logging.DEBUG,
)

def main():
    conn = project.database.connect()
    games = parse()
    for game in games:
        project.database.insert(game, conn)

    project.database.disconnect(conn)


if __name__ == '__main__':
    main()