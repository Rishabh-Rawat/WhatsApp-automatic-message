import mysql.connector as msq

def insert():
    cur.execute("desc birthday_database")   # store column names
    data=cur.fetchall()
    full_input=""                                                     
    for i in data:
        print("NOTE: Please enter string/varchar/date values (if any) in quotes")
        print("Enter the",i[0],end=" ")                        
        single_value=input()       # takes single attribute value input
        full_input=full_input+single_value+","     # concatenates to form single input statement
    full_input=full_input.rstrip(",")         # removes extra comma from input values statement
    cur.execute("Insert into birthday_database values({})".format(full_input)) 
    mycon.commit()
    print("Record successfully inserted")
   
def display():
    cur.execute("Select * from birthday_database")  # extracts all records from table
    for i in cur.fetchall():
        print(i)

def modify():
    print("Columns present in table:")     # displays column names
    cur.execute("desc birthday_database")                                            
    data=cur.fetchall()                                                              
    for i in data:                                                      
        print("\t",i[0])
    mod=input("Enter the field name to modify ")     # this attribute is to be modified
    find=input("Enter the column name using which you want to find the record ") #to search record 
    print("Enter the",find,"of that record",end=" ")                            
    find_value=input()      # takes the value of attribute using which we will search for a record
    print("Enter the new",mod,end=" ")
    mod_value=input()     # takes new value of attribute to be modified
    cur.execute("update birthday_database set {}='{}' where {}='{}'".format(mod,mod_value,find,find_value))
    mycon.commit()
    print("Record sucessfully modified")

def delete():
    print("Columns present in table:")   # displays column names
    cur.execute("desc birthday_database")                                               
    data=cur.fetchall()                                                                
    for i in data:
        print("\t",i[0])
    find=input("Enter the column name using which you want to find the record") #to search record
    print("NOTE: NO TWO RECORDS SHOULD HAVE SAME VALUE FOR THIS COLUMN ")
    print("Enter the",find,"of that record",end=" ")
    find_value=input()      # takes the value of attribute using which we will search for a record
    cur.execute("delete from birthday_database where {}='{}'".format(find,find_value))
    mycon.commit()
    print("Record successfully deleted")
    

#__main__
database_name=input("Enter the database ")
my_sql_password=input("Enter the password for MySQL ")
mycon=msq.connect(host="localhost",user="root",database=database_name,passwd=my_sql_password)
cur=mycon.cursor()
if mycon.is_connected():
    print("Successfully Connected to Database")
else:
    print("Connection Faliled")
while True:
    print("\t\t1. Insert Record")
    print("\t\t2. Display Records")
    print("\t\t3. Modify Record")
    print("\t\t4. Delete Recod")
    print("\t\t5. Exit\n")
    ch=int(input("Enter the choice "))
    if ch==1:
        insert()     # calls function for inserting a record
    elif ch==2:
        display()    # calls function to display all records
    elif ch==3:
        modify()   # calls function to modify a record
    elif ch==4:
        delete()      # call function to delete a record
    elif ch==5:
        mycon.close()    # closes the connection between python and MySQL
        break
    else:
        print("Invalid choice entered")