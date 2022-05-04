import mysql.connector

con = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "sonic031",
        database = "lab"
)

cur = con.cursor()
#cur.execute("create table labby(i int primary key,name text)")
#cur.execute("insert into labby values(1,'test')")
cur.execute("insert into labby values(2,'test1')")

cur.execute("select * from labby")

for i in cur:
        print(i)