import sqlite3

conn = sqlite3.connect('demo_data.sqlite3')
curs = conn.cursor()

curs.execute("""CREATE TABLE demo(
                s varchar(1),
                x int,
                y int);""")

curs.execute("""INSERT INTO demo (
                s, x, y)
                VALUES
                ('g', 3, 9),
                ('v', 5, 7),
                ('f', 8, 7);""")

row_count = curs.execute("""SELECT COUNT (*) FROM demo;""").fetchone()
row_count2 = curs.execute("""SELECT COUNT (*)
                             FROM demo
                             WHERE x >= 5
                             AND y >= 5;""").fetchone()
row_count_distinct = curs.execute("""SELECT COUNT (DISTINCT y)
                                     FROM demo;""").fetchone()


print(row_count[0], row_count2[0], row_count_distinct[0])
curs.close()
conn.commit()
