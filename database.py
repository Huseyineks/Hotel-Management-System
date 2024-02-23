import mysql.connector


db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "huseyinilkerh1905",
    database ="hotelmanagementdatabase"
)


mycursor = db.cursor()



class DATABASE:
    def __init__(self,messages):
        messages = str(messages).split(',')
        print(f"{messages}")
        mycursor.execute("INSERT INTO people(Name,Username,Email) VALUES(%s,%s,%s)",(messages[0],messages[1],messages[2]))
        db.commit()
        