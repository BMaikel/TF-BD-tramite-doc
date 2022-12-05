import pymysql

connection = pymysql.connect(
            host = "localhost",
            user = "root",
            password = "",
            db = "tf_test2")

cursor = connection.cursor()

sql = f"""SELECT * FROM usuario WHERE user = "alex1" AND pass = "alex1";""" #Sentencia SQL
cursor.execute(sql)
r = cursor.fetchone() #Un unico registro
print(r)
connection.close()