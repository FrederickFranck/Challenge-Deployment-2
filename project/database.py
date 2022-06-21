import mariadb
import toml
import pathlib
import logging


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

def insert():
    return


def query():
    return


if __name__ == "__main__":
    main()
