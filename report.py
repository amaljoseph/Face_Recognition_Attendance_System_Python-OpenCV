def rep():
	import csv
	import sqlite3
	list = []
	#templist = []
	def displayDatabase():
		conn= sqlite3.connect('students.db')
		cmd="SELECT * FROM STUDENTS "
		cursor=conn.execute(cmd)
		for row in cursor:
			templist = []
			if row[3] == 1:
				status = "PRESENT"
			else:
				status = "ABSENT"	
			templist.append(row[2])
			templist.append(row[1])
			templist.append(status)
			list.append(templist)
		conn.commit()
		conn.close()

	reportfile = open('report.csv', 'w')
	reportwriter = csv.writer(reportfile)
	reportwriter.writerow(['ROLL NO', 'STUDENT NAME','ABSENT / PRESENT'])
	for i in range(0, 2):
		displayDatabase()
		reportwriter.writerow(list[i])
		list = []
	reportfile.close()
	
