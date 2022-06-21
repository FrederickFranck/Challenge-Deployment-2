import mariadb
import sys
import toml
import pathlib

# Read local `config.toml` file.
config = toml.load(pathlib.Path(__file__).parent / "dbcredentials.toml")


def main():
    try:
        conn = mariadb.connect(
            user=config["DB"]["username"],
            password=config["DB"]["password"],
            host=config["DB"]["ipaddress"],
            port=config["DB"]["port"],
            database=config["DB"]["dbname"],
        )
        
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)

    # Get Cursor
    cur = conn.cursor()
    cur.execute("Show tables")

    for r in cur:
        print(r)


def connect():
    return


def disconnect():
    return


def insert():
    return


def query():
    return


if __name__ == "__main__":
    main()
