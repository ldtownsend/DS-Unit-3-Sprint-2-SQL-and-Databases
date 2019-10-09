import pandas as pd
import sqlite3

df = pd.read_csv('buddymove_holidayiq.csv')
assert df.shape == (249, 7)
for total in df.isnull().sum():
    assert total == 0

conn = sqlite3.connect('buddymove_holidayiq.sqlite3')
name = 'review'
df.to_sql(name=name, con=conn, if_exists='replace')
curs = conn.cursor()

row_count_query = "SELECT COUNT (*) FROM review;"
row_count = curs.execute(row_count_query).fetchone()
print("The number of rows is: ", row_count[0])

num_reviewed_query = """SELECT COUNT (*) FROM review WHERE Nature >= 100 AND Shopping >= 100"""
num_reviewed = curs.execute(num_reviewed_query).fetchone()

print("The number of users who reviewed at least 100 Nature movies and 100 Shopping movies: ", num_reviewed[0])
