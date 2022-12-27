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

    def buscar_documento(self, busqueda):
        nn = [i for i, e in enumerate(busqueda) if e != ""]
        valores = ["motivo","emisor","tipo_documento","palabra_clave"]
        r = []
        if len(nn) != 0:
            for i in nn:
                r.append(valores[i])
            
            if len(r) == 1:
                sql = f"""SELECT * FROM documento WHERE {r[0]} = "{busqueda[nn[0]]}" """
                try:
                    self.cursor.execute(sql)
                    respuesta = self.cursor.fetchall()
            
                    return respuesta #Todos los registros

                except Exception as e:
                    raise

            elif len(r) == 2:
                sql = f"""SELECT * FROM documento WHERE {r[0]} = "{busqueda[nn[0]]}" AND {r[1]} = "{busqueda[nn[1]]}" """
                try:
                    self.cursor.execute(sql)
                    respuesta = self.cursor.fetchall()
            
                    return respuesta #Todos los registros

                except Exception as e:
                    raise

            if len(r) == 3:
                sql = f"""SELECT * FROM documento WHERE {r[0]} = "{busqueda[nn[0]]}" AND {r[1]} = "{busqueda[nn[1]]}" AND
                {r[2]} = "{busqueda[nn[2]]}" """
                try:
                    self.cursor.execute(sql)
                    respuesta = self.cursor.fetchall()
            
                    return respuesta #Todos los registros

                except Exception as e:
                    raise
            
            if len(r) == 4:
                sql = f"""SELECT * FROM documento WHERE {r[0]} = "{busqueda[nn[0]]}" AND {r[1]} = "{busqueda[nn[1]]}" AND
                {r[2]} = "{busqueda[nn[2]]}" AND {r[3]} = "{busqueda[nn[3]]}" """
                try:
                    self.cursor.execute(sql)
                    respuesta = self.cursor.fetchall()
            
                    return respuesta #Todos los registros

                except Exception as e:
                    raise

        else:
            sql = f"""SELECT * FROM documento"""
            try:
                self.cursor.execute(sql)
                respuesta = self.cursor.fetchall()
            
                return respuesta #Todos los registros

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

    def editar_documento(self, id, emisor, receptor, proveido, motivo, palabra_clave, tipo_documento):
        sql = f"""UPDATE documento SET emisor = "{emisor}", receptor = "{receptor}", 
        proveido = "{proveido}", motivo = "{motivo}", palabra_clave = "{palabra_clave}",
        tipo_documento = "{tipo_documento}" WHERE id_doc = "{id}" """
        try:
            self.cursor.execute(sql)
            self.connection.commit()

        except Exception as e:
            raise        

    def eliminar_documento(self, idDoc):
        sql = f"""DELETE FROM documento WHERE id_doc='{idDoc}';"""
        try:
            self.cursor.execute(sql)
            self.connection.commit()

        except Exception as e:
            raise

    def close(self):
        self.connection.close() #Es necesario terminar la conección con la base de datos