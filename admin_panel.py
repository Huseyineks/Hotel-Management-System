import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "huseyinilkerh1905",
    database ="HotelManagementDatabase"
)

mycursor = db.cursor()

mycursor.execute("CREATE TABLE People (person_id int PRIMARY KEY AUTO_INCREMENT,Name VARCHAR(50) NOT NULL,Username VARCHAR(50) NOT NULL,Email VARCHAR(100) NOT NULL)")

class DATABASE:
    def __init__(self):
        pass