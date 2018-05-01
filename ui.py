
print('---------------------------------------------------------------------------')
print('\t\tATTENDANCE SYSTEM USING FACIAL RECOGNITION ')
print('---------------------------------------------------------------------------')
print('\t\t       SCHOOL OF ENGINEERING, CUSAT')
print('---------------------------------------------------------------------------')
print " \n\n"
print("MENU\n(1)MARK ATTENDANCE\n(2)VIEW ATTENDANCE\n(3)GENERATE REPORT\n(4)QUIT")
choice=input(">>>")
ch=1
while ch!=0 and choice !=4:
    if choice==1:
        import sqlpy as mark
        mark.first()
        choice=input("\nMENU\n(1)MARK ATTENDANCE\n(2)VIEW ATTENDANCE\n(3)GENERATE REPORT\n(4)QUIT\n\n>>>")
        continue
    elif choice==2:
    	import sqlpy as mark1
        mark1.displayDatabase()
        choice=input("\nMENU\n(1)MARK ATTENDANCE\n(2)VIEW ATTENDANCE\n(3)GENERATE REPORT\n(4)QUIT\n\n>>>")
        continue
    elif choice==3:
    	import report as mark2
        mark2.rep()
        print "\nReport generated successfully"
        choice=input("\nMENU\n(1)MARK ATTENDANCE\n(2)VIEW ATTENDANCE\n(3)GENERATE REPORT\n(4)QUIT\n\n>>>")
        continue
    else:
        print("Invalid choice, please choose again")
        print("\n")
print("")
print(".")
import sqlite3
conn= sqlite3.connect('students.db')
#for i in range(0, 2):
cnd="UPDATE STUDENTS SET ATTENDANCE = 0 WHERE ID = 1 OR ID = 2"
cursor=conn.execute(cnd)
conn.commit()
conn.close()

