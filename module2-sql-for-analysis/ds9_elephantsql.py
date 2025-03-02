# -*- coding: utf-8 -*-
"""DS9_ElephantSQL.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11v7oXU7PhkwJ9Da3EPj86D8shXuOZ_J-
"""

!pip install psycopg2-binary

import psycopg2
dir(psycopg2)

help(psycopg2.connect)

dbname = 'askuvppm'
user = 'askuvppm'
password = 'wuWrTwrCn1UoR92DecFFLZaT4CRxZSOg'
host = 'rajje.db.elephantsql.com'

pg_conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)

pg_curs = pg_conn.cursor()

pg_curs.execute('SELECT * FROM test_table')

pg_curs.fetchall()

!wget https://github.com/LambdaSchool/DS-Unit-3-Sprint-2-SQL-and-Databases/blob/master/module1-introduction-to-sql/rpg_db.sqlite3?raw=true

!mv 'rpg_db.sqlite3?raw=true' rpg_db.sqlite3

import sqlite3
sl_conn  = sqlite3.connect('rpg_db.sqlite3')
sl_curs = sl_conn.cursor()

sl_curs.execute('SELECT COUNT(*) FROM charactercreator_character;').fetchall()

sl_curs.execute('SELECT COUNT(DISTINCT name) FROM charactercreator_character;').fetchall()

characters = sl_curs.execute('SELECT * FROM charactercreator_character;').fetchall()

characters[0]

characters[-1]

len(characters)

sl_curs.execute('PRAGMA table_info(charactercreator_character);').fetchall()

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

show_table = """
SELECT * 
FROM pg_catalog.pg_tables
WHERE schemaname != 'pg_catalog'
AND schemaname != 'information_schema';
"""

pg_curs.execute(show_table)
pg_curs.fetchall()

characters[0]

str(characters[0][1:])

example_insert = """
INSERT INTO charactercreator_character
(name, level, exp, hp, strength, intelligence, dexterity, wisdom)
VALUES """ + str(characters[0][1:]) + ";"

print(example_insert)

for character in characters:
  insert_character = """
    INSERT INTO charactercreator_character
    (name, level, exp, hp, strength, intelligence, dexterity, wisdom)
    VALUES """ + str(character[1:]) + ";"
  pg_curs.execute(insert_character)

pg_curs.execute('SELECT * from charactercreator_character;')
pg_curs.fetchall()

pg_curs.close()
pg_conn.commit()

pg_curs = pg_conn.cursor()
pg_curs.execute('SELECT * FROM charactercreator_character;')

pg_characters = pg_curs.fetchall()

pg_characters[0]

characters[0:3]

pg_characters[0:3]

for character, pg_character in zip(characters, pg_characters):
  assert character == pg_character







"""If I have an invalid SQL statement or typo and I get the current transaction aborted method,
close and reopen conn and curs
pg_curs.close() #closes the cursosr
pg_conn.commit() #commit changes to database
pg_conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host) #reopened connection
pg curs = pg_conn.cursor() #reopened the cursor
"""