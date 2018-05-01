

import sqlite3
conn=sqlite3.connect("students.db")
conn.execute(''' CREATE TABLE STUDENTS
	       ( ID INT PRIMARY KEY,
		 NAME TEXT ,
		 ROLL INT ,
                 ATTENDANCE  INT);''') 
		 
print "Table created succesfully" 

conn.commit()
conn.close()
