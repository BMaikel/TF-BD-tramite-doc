import pymysql

class Database():

    def __init__(self):
        self.connection = pymysql.connect(
            host = "localhost",
            user = "root",
            password = "",
            db = "bd_trabajofinal"
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
    
    def buscar_empleado(self, idUser):
        sql = f"""SELECT * FROM usuario WHERE user = "{idUser}";""" #Sentencia SQL

        try:
            self.cursor.execute(sql)
            r1 = self.cursor.fetchone() #Un unico registro
            
            id_emp = r1[3]
            sql2 = f"""SELECT * FROM empleado WHERE id_emp = "{id_emp}";"""

            self.cursor.execute(sql2)
            r2 = self.cursor.fetchone()

            return r2

        except Exception as e:
            raise

    def mostrar_documentos(self):
        sql = f"""SELECT * FROM documento"""
        try:
            self.cursor.execute(sql)
            r = self.cursor.fetchall()
            
            return r #Todos los registros

        except Exception as e:
            raise

    def insertar_documento(self, id_doc1, emisor, receptor, proveido, motivo, palabra_clave, tipo_documento):
        sql = f"""INSERT INTO documento (id_doc, emisor, receptor, proveido, motivo, palabra_clave, tipo_documento) 
        VALUES ("{id_doc1}", "{emisor}", "{receptor}","{proveido}", "{motivo}","{palabra_clave}", "{tipo_documento}");"""
        try:
            self.cursor.execute(sql)
            self.connection.commit()

        except Exception as e:
            raise

    def close(self):
        self.connection.close() #Es necesario terminar la conección con la base de datos