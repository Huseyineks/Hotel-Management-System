import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "huseyinilkerh1905",
    
)

mycursor = db.cursor()

# mycursor.execute("CREATE TABLE People (person_id int PRIMARY KEY AUTO_INCREMENT,Name VARCHAR(50) NOT NULL,Username VARCHAR(50) NOT NULL,E-mail VARCHAR(100) NOT NULL)")
mycursor.execute("CREATE DATABASE HotelManagementDatabase")
class DATABASE:
    def __init__(self):
        pass