import sqlite3

conn= sqlite3.connect('students.db')
print "\nOpened database succesfully"
print"\nCreating Records...."

def insertOrUpdate(ide,name,roll,att):
	cmd="SELECT * FROM STUDENTS WHERE ID =" +ide
  	cursor=conn.execute(cmd)
 	isRecordExist=0
 	for row in cursor:
 		isRecordExist=1
 	if(isRecordExist==1):
 		conn.execute("UPDATE STUDENTS SET NAME = ? WHERE ID = ?",(name, ide))
        	conn.execute("UPDATE STUDENTS SET ROLL = ? WHERE ID = ?",(roll, ide))
        	conn.execute("UPDATE STUDENTS SET ATTENDANCE = ? WHERE ID = ?",(att, ide))
        else :
        	params = (ide, name, roll,att)                                               
    		conn.execute("INSERT INTO STUDENTS VALUES(?, ?, ?,?)", params)
        conn.commit()
        
att=0
n=input ("How many records do you want to create ? ")
for i in range(0,n): 
	ide = raw_input('Enter user id : ')
	name = raw_input("Enter student's name : ")
	roll = raw_input("Enter student's roll no. : ")
	insertOrUpdate(ide, name, roll,att)
 	print " "
print "\nRecords created successfully"
conn.close()
