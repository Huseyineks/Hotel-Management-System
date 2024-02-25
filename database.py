import mysql.connector


db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "huseyinilkerh1905",
    database ="hotelmanagementdatabase"
)
db_2 =  mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "huseyinilkerh1905",
    database ="demand"
)


mycursor = db.cursor()
mycursor_2 = db_2.cursor()



class DATABASE:
    
    def __init__(self,messages):
        
        if len(str(messages).split(',')) == 3:
            self.People(messages)
        elif len(str(messages).split(',')) == 4:
            self.Demand(messages)
            
        else:
            pass        
    
    def People(self,messages):    
        messages = str(messages).split(',')
        
        mycursor.execute("INSERT INTO people(Name,Username,Email) VALUES(%s,%s,%s)",(messages[0],messages[1],messages[2]))
        db.commit()
        


    def Demand(self,messages):
        messages = str(messages).split(',')
        print(f"{messages}")
        mycursor_2.execute("INSERT INTO request(Child,Adult,Room,Date) VALUES(%s,%s,%s,%s)",(messages[0],messages[1],messages[2],messages[3]))
        db_2.commit()
          