import mysql.connector

#pip install mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", password="", database = "svkm_43")

mycursor = mydb.cursor()
# sql = "show databases"
# sql = "create database svkm_43"
# sql = "drop database svkm_43"

sql = "create table TYCOMP(ID int auto_increment primary key, Name varchar(50) not null, Email varchar(50), C_no int) values(%d, %s, %s, %d)"
mycursor.execute(sql)

sql = "show tables"
mycursor.execute(sql)

sql = "Insert into TYCOMP( ID, Name, Email, C_no)"
values = [
    (101, 'Rahul Patil', 'rahul123@gmail.com',9997457289)
    (102, 'Anu Kumari', 'anu1@gmail.com',9991247289)
    (103, 'Samar Patil', 'sam13@gmail.com',8887457289)
    (104, 'Reena Sehgal', 'reena90@gmail.com',8877457289)
    (105, 'Peter Parker', 'peterp3@gmail.com',3337457289)
]
mycursor.executemany(sql, values)
mydb.commit()
sql = "select * from TYCOMP"

for database in mycursor:
    print(database)

