##Mustafa Al-kishtainy
##professor Oto CIS3368

import mysql.connector
from mysql.connector import Error
import datetime as dt
from datetime import date



def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try: 
        connection= mysql.connector.connect(
        host= host_name,
        user=user_name,
        passwd=user_password,
        database=db_name
        )
        print("connection successful")
    except Error as e:
        print(f"the error '{e}' occured" )
    return connection

def execute_query(connection, query):
    mycursor=connection.cursor()
    try:
        mycursor.execute(query)
        connection.commit()
        print("Query ran successfuly")
    except Error as e:
        print(f"the error '{e}' occured")

def read_query(connection, query):
    mycursor= connection.cursor()
    result= None
    try:
        mycursor.execute(query)
        result = mycursor.fetchall()
        return result
    except Error as e:
        print(f"the error '{e}' occured")

################################# connects to workbench and AWS ###########################################
connection= create_connection("cis3368v1.cl3c9tgm8sn0.us-east-2.rds.amazonaws.com","admin","Daguy.jason.com","cis3368v1db")


contactDetail=""
creationDate=""

def Menu():
    print("Menu: ")
    print("a - Add contact")
    print("d - Delete contact")
    print("u - Update contact")
    print("b - Output all contacts in alphabetical order")
    print("c - Output all contacts by creation date")
    print("o - Output all contacts")
    print("q - Quit")

Menu()
choice = input("Choose an option: ")
while choice != 'q':
    
    ##################################### ADD CONTACTS ##########################################
    
    if choice == 'a':
        contactDetail= input("Enter contact details: ")
        creationDate = dt.date.today() ## automatically adds todays date 
        add_contact= "INSERT INTO contacts (contactDetails, creationDate) VALUES ('%s', '%s')" % (contactDetail, creationDate)    
        execute_query(connection,add_contact)   
    
    ##################################### DELETE CONTACT ##########################################         
    
    elif choice == 'd':
        choice = input("Enter the ID of the contact you would like to delete: ")
        del_contact = "DELETE FROM contacts WHERE id = %s" %(choice)
        execute_query(connection, del_contact)
    
    ##################################### UPDATE CONTACT #############################################
    
    elif choice == 'u':
        contact_id = input("Enter the contact you would like to edit: ")
        new_details = input("Enter the new contact deteails: ")
        update_contact= "UPDATE contacts SET contactDetails = '%s' WHERE id = '%s' " %(new_details, contact_id)
        execute_query(connection, update_contact)
   
    ############################## PRINT CONTACT NAME BY ALPHABETICAL ORDER ######################################
    
    elif choice == 'b':
        select_contacts= "SELECT * FROM contacts ORDER BY contactDetails"
        contacts =read_query(connection, select_contacts)
        print(" ID" + "   DETAILS"+"       CREATION DATE")
        print("------------------------------------")
        for contact in contacts:
            Id= contact[0]
            contactDetail = contact[1]
            creationDate= contact[2]
            
            print("{:^5} {:^5} {:>15}".format(str(Id), contactDetail, str(creationDate) )) 
   
    ################################### Output all contacts by creation date ################################################################
    
    elif choice == 'c':
        select_contacts= "SELECT * FROM contacts ORDER BY creationDate"
        contacts =read_query(connection, select_contacts)
        print(" ID" + "   DETAILS"+"       CREATION DATE")
        print("------------------------------------")
        for contact in contacts:
            Id= contact[0]
            contactDetail = contact[1]
            creationDate= contact[2]
            
            print("{:^5} {:^5} {:>15}".format(str(Id), contactDetail, str(creationDate) )) 
    
    ################################### OUTPUTS ALL CONTACTS ##################################
    
    elif choice =='o': 
        select_contacts= "SELECT * FROM contacts"
        contacts =read_query(connection, select_contacts)
        print(" ID" + "   DETAILS"+"       CREATION DATE")
        print("------------------------------------")
        for contact in contacts:
            Id= contact[0]
            contactDetail = contact[1]
            creationDate= contact[2]
            
            print("{:^5} {:^5} {:>15}".format(str(Id), contactDetail, str(creationDate) ))       
    else: 
        print("invalid")


    print()
    Menu()
    choice = input("Choose an option: ")


 

        


     





