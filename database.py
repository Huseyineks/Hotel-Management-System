import mysql.connector


db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "huseyinilkerh1905",
    database ="HotelManagementDatabase"
)


mycursor = db.cursor()



class DATABASE:
    def __init__(self):
        pass