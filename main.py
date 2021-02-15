##Mustafa Al-kishtainy
##professor Otoo 3368

import mysql.connector
from mysql.connector import Error
import datetime
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

create_connection("cis3368v1.cl3c9tgm8sn0.us-east-2.rds.amazonaws.com","admin","Daguy.jason.com","cis3368v1db")


contactDetail=""
creationDate=""

def Menu():
    print("Menu: ")
    print("a - Add contact")
    print("d - Delete contact")
    print("u - Update contact")
    print("b - Output all contacts in alphabetical order")
    print("c - Output all contacts by creation date")
    print("q - Quit")

Menu()
choice = input("Choose an option: ")
while choice != 'q':
    if choice == 'a':
        contactDetail= input("Enter contact details: ")
        creationDate = input("On what date was this document created?: ")
            
    elif choice == 'd':
        print('d')
    elif choice == 'u':
        print('u')
    elif choice == 'b':
        print('b')
    elif choice == 'c':
        print('c')
    else: 
        print("invalid")


    print()
    Menu()
    choice = input("Choose an option: ")


 

        


     





