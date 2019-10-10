import psycopg2
import sqlite3

dbname = 'jwakmefc'
user = 'jwakmefc'
password = 'TODO - refresh with password'
host = 'salt.db.elephantsql.com'



# This is the the first example of connecting to a database using elephantsql

pg_conn = psycopg2.connect(dbname = dbname, user = user, password = password, host = host)

pg_curs = pg_conn.cursor()

# pg_curs.execute('SELECT * FROM test_table;')
#
# print(pg_curs.fetchall())




# This is the second example from class

sl_conn = sqlite3.connect('rpg_db.sqlite3')
sl_curs= sl_conn.cursor()

# sl_curs.execute('SELECT COUNT(*) FROM charactercreator_character;')
# print(sl_curs.fetchall()[0])


characters = sl_curs.execute('SELECT * FROM charactercreator_character;').fetchall()
# print(characters[-1])


# sl_curs.execute('PRAGMA table_info(charactercreator_character);')
# print(sl_curs.fetchall())

create_character_table = """
CREATE TABLE charactercreator_character (
    character_id SERIAL PRIMARY KEY,
    name VARCHAR(30),
    level INT,
    exp INT,
    hp INT,
    strength INT,
    intelligence INT,
    dexterity INT,
    wisdom INT
);
"""

pg_curs.execute(create_character_table)

show_tables = """
SELECT *
FROM pg_catalog.pg_tables
WHERE schemaname != 'pg_catalog'
AND schemaname != 'information_schema';
"""

# pg_curs.execute(show_tables)
#
# print(pg_curs.fetchall())

# print(str(characters[0][1:]))

example_insert = """
INSERT INTO charactercreator_character
(name, level, exp, hp, strength, intelligence, dexterity, wisdom)
VALUES """ + str(characters[0][1:]) + ';'

# print(example_insert)

for character in characters:
    insert_character = """
    INSERT INTO charactercreator_character
    (name, level, exp, hp, strength, intelligence, dexterity, wisdom)
    VALUES """ + str(character[1:]) + ';'
    pg_curs.execute(insert_character)

pg_curs.execute('SELECT * FROM charactercreator_character;')

populated = pg_curs.fetchall()

print(populated)
