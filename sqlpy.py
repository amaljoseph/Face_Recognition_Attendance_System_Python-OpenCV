#!/usr/bin/python
import sqlite3
import facemaster as facemaster
list = facemaster.label
print list
print "\n"

def displayDatabase():
	conn= sqlite3.connect('students.db')
	cmd="SELECT * FROM STUDENTS "
	cursor=conn.execute(cmd)
	print "ID\tNAME\t\t\tROLLNO\tATTENDANCE"
	for row in cursor:
		if(row[3]==1):
   			print row[0],"\t",row[1],"\t\t\t",row[2],"\tPRESENT"
   		else:
   		   print row[0],"\t",row[1],"\t\t\t",row[2],"\tABSENT"	
   		print "  "
	conn.commit()
	conn.close()
  	
def addManually():
	rollno=input( "\nEnter the Roll No. of student to mark attendance : ")
	conn= sqlite3.connect('students.db')
 	cmd="SELECT * FROM STUDENTS WHERE ROLL =" +str(rollno)
  	cursor=conn.execute(cmd)
 	isRecordExist=0
 	for row in cursor:
 		isRecordExist=1
 	if (isRecordExist==1):
 		conn.execute("UPDATE STUDENTS SET ATTENDANCE = 1 WHERE ROLL = " + str(rollno))
 		print "\nUpdated database successfully"
 	else :
 		print "\nStudent record does not exist "
 	conn.commit()
 	conn.close()
  	
	


	

def updateAttendance(roll):
	conn= sqlite3.connect('students.db')
	cmd="SELECT * FROM STUDENTS WHERE ROLL = " +str(roll)
	cursor=conn.execute(cmd)
	isRecordExist=0
	for row in cursor:
		isRecordExist=1
		if (isRecordExist==1):
			conn.execute("UPDATE STUDENTS SET ATTENDANCE = 1 WHERE ROLL=? " ,str(roll))
		else:
			print "\nStudent record does not exist "
	conn.commit()
	conn.close()
	
	
 		

def first():
	n = len(list)
	for i in range(0, n):
		updateAttendance(list[i])
	displayDatabase()
	c=input("\nPress '1' to mark more attendance manually : ")
	if(c==1):
		addManually()
