import pymysql

connection = pymysql.connect(
            host = "localhost",
            user = "root",
            password = "",
            db = "bbdd_09_12")

cursor = connection.cursor()

sql = f"""SELECT * FROM emp;""" #Sentencia SQL
cursor.execute(sql)
r = cursor.fetchall() #Un unico registro
connection.close()

print(type(r))