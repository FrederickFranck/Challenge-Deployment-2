import mariadb
import toml
import pathlib
import logging

from project.game import Game


# Read local `config.toml` file.
config = toml.load(pathlib.Path(__file__).parent / "dbcredentials.toml")


def main():
    return


def connect() -> mariadb.connection:
    try:
        conn = mariadb.connect(
            user=config["DB"]["username"],
            password=config["DB"]["password"],
            host=config["DB"]["ipaddress"],
            port=config["DB"]["port"],
            database=config["DB"]["dbname"],
        )
        return conn

    except mariadb.Error as e:
        logging.error(f"{__name__:<15} connecting to MariaDB Platform: {e}")
        return


def disconnect(_connection: mariadb.connection):
    _connection.close()
    return


def insert(_game: Game, _connection : mariadb.connection) -> bool:
    SQL = "INSERT INTO Games (ID, NAME, Description, Price, Developer, Win_Support, Mac_Support, Linux_Support, Pos_Review, Neg_Review )" \
    "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
    
    cursor = _connection.cursor()
    cursor.execute(SQL,(_game.id, _game.name, _game.description, _game.price, _game.developer, _game.win_support, _game.mac_support, _game.linux_support, _game.positive_reviews, _game.negative_reviews))
    
    for result in cursor:
        print(result)
        
    #_connection.close()
    return


def query():
    return


if __name__ == "__main__":
    main()
