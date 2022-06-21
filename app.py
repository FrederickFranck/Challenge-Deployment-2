import logging
import pathlib

import project.database

logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', datefmt='%d/%m/%Y %H:%M:%S ',
                    filename=pathlib.Path(__file__).parent / 'logs/app.log', level=logging.DEBUG)

conn = project.database.connect()
cur = conn.cursor()
cur.execute("Show tables")
for r in cur:
    print(r)
project.database.disconnect(conn)
cur = conn.cursor()
cur.execute("Show tables")
for r in cur:
    print(r)