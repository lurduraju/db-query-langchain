import sqlite3

#connect ts sqlite 
connection=sqlite3.connect('dbname.db')

#create a cursor object for crud operations
cursor=connection.cursor()

#create a table 
table_info="""
create table students(rollno int,Name varchar(25),sec char,int age,marks int)"""

cursor.execute(table_info)

cursor.execute('''Insert into values(1,"kruthika",a,20,95)''')

print("The inserted records are")

data=cursor.execute('''select * from students''')
for row in data:
    print(row)
connection.commit()
connection.close()








