import pandas as pd
import psycopg2
import sqlite3
import tabulate


# log-in credentials for elephantsql
dbname = 'jwakmefc'
user = 'jwakmefc'
password = 'TODO - Refresh and re-enter'
host = 'salt.db.elephantsql.com'

# Connect to elephantsql and make a cursor
pg_conn = psycopg2.connect(dbname = dbname, user = user, password = password, host = host)
pg_curs = pg_conn.cursor()

# Create a database called titanic.sqlite3
ti_conn = sqlite3.connect('titanic.sqlite3')
ti_curs = ti_conn.cursor()

# import the titanic.csv and populate ti_conn
# removes the table if its already there, ie if you need to run this many times
del_table = 'DROP TABLE IF EXISTS titanic_table'
ti_curs.execute(del_table)

# reads in the csv
df_titanic = pd.read_csv('titanic.csv')

# eleminates the issue of the apostrophe in the passenger name
df_titanic.Name = df_titanic.Name.replace("'", '', regex=True)

# populates the
df_titanic.to_sql('Titanic', ti_conn, index_label='id')

#creating the postgres table columns and assigning their datatypes
create_titanic_table = '''
CREATE TABLE titanic_table (
    "survived" INT,
    "pclass" INT,
    "name" TEXT,
    "sex" TEXT,
    "age" INT,
    "siblingsspouses" INT,
    "parentschildren" INT,
    "fare" FLOAT
);
'''
pg_curs.execute(create_titanic_table)

#instantiating list of all data in titanic df with each line being a tuple
titanic_list = ti_curs.execute("SELECT * FROM Titanic;").fetchall()

print(titanic_list[0:5])

pg_curs.close()
pg_conn.commit()
