import sqlite3

conn = sqlite3.connect('pfsddd.db')
cursor = conn.cursor()
cursor.execute("Create table EMPLOYEE(FIRST_NAME varchar(30),LAST_NAME varchar(30),AGE int(30),SEX varchar(30),INCOME int(30))")
cursor.execute('''INSERT INTO EMPLOYEE(
   FIRST_NAME, LAST_NAME, AGE, SEX, INCOME) VALUES 
   ('Kumari', 'priya', 21, 'F', 7000)''')

cursor.execute('''INSERT INTO EMPLOYEE(
   FIRST_NAME, LAST_NAME, AGE, SEX, INCOME) VALUES 
   ('Sony', 'raj', 10, 'M', 8000)''')

cursor.execute('''INSERT INTO EMPLOYEE(
   FIRST_NAME, LAST_NAME, AGE, SEX, INCOME) VALUES 
   ('oriya', 'sigh', 24, 'M', 8300)''')

cursor.execute('''INSERT INTO EMPLOYEE(
   FIRST_NAME, LAST_NAME, AGE, SEX, INCOME) VALUES 
   ('abhiram', 'Sharma', 21, 'M', 9000)''')

cursor.execute('''INSERT INTO EMPLOYEE(
   FIRST_NAME, LAST_NAME, AGE, SEX, INCOME) VALUES 
   ('Tirmula', 'Ram', 22, 'F', 8000)''')

conn.commit()
print("Records inserted successfully")

conn.close()
