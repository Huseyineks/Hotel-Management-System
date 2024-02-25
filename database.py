import mysql.connector


db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "huseyinilkerh1905",
    database ="demand"
)


mycursor = db.cursor()


mycursor.execute("CREATE TABLE REQUEST (person_id int PRIMARY KEY AUTO_INCREMENT,Child int NOT NULL,Adult int NOT NULL,Room  int NOT NULL, Date VARCHAR(100) NOT NULL)")

class DATABASE:
    def __init__(self,messages):
        messages = str(messages).split(',')
        print(f"{messages}")
        mycursor.execute("INSERT INTO people(Name,Username,Email) VALUES(%s,%s,%s)",(messages[0],messages[1],messages[2]))
        db.commit()
        