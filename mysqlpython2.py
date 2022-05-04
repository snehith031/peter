import mysql.connector

mydb = mysql.connector.connect(
 host="localhost",
 user="root",
 password="sonic031",
 database="hospital"
)
print(mydb)
var=mydb.cursor()
var.execute("Show databases")
for i in var:
 print(i)
print("")
var.execute("create table doctor(name varchar(30),id int(30))")
sql="insert into doctor(name,id) values(%s,%s)"
val=[("Ram",1234),("Ravi",1235),("Rahim",1236)]
var.executemany(sql,val)
mydb.commit()
var.execute("select * from doctor")
result=var.fetchall()
for i in result:
 print(i)
print("")
var.execute("create table patients(name varchar(30),id int(30),medicine varchar(30))")
sq="insert into patients(name,id,medicine) values(%s,%s,%s)"
va=[("Rahul",1234,"Dolo 650"),("Rashi",1235,"Benedryl"),("Rakhi",1236,"Limc")]
var.executemany(sq,va)
mydb.commit()
var.execute("select * from patients")
res=var.fetchall()
for i in res:
 print(i)
print("")