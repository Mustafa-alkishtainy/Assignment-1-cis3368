##Mustafa Al-kishtainy
##professor Otoo 3368

import mysql.connector
import datetime
from datetime import date

db= mysql.connector.connect( 
    host="cis3368v1.cl3c9tgm8sn0.us-east-2.rds.amazonaws.com",
    user="admin",
    passwd="Daguy.jason.com",
    database="cis3368v1db"
)

cursor=db.cursor()

cd= datetime.datetime(2000,1,21)
str_cd= cd.date().isoformat()
addContact = "INSERT INTO contacts (contactDetails, creationDate) VALUES ('Tom cruse', '2021-02-14')"
cursor.execute(db,addContact)

db.commit()



 


        


     





