import pymysql

class Database():

    def __init__(self):
        self.connection = pymysql.connect(
            host = "localhost",
            user = "root",
            password = "",
            db = "tf_test2"
        )

        self.cursor = self.connection.cursor()

    def select_user(self, usuario, password):
        sql = f"""SELECT * FROM usuario WHERE user = "{usuario}" AND pass = "{password}";""" #Sentencia SQL

        try:
            self.cursor.execute(sql)
            r = self.cursor.fetchone() #Un unico registro
            return r

        except Exception as e:
            raise

    def close(self):
        self.connection.close() #Es necesario terminar la conección con la base de datos