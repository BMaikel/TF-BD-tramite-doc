MOLINA - UNALM
# TRABAJO FINAL: Sistema de Gestión de Base de Datos I
### Prototipo: Sistema de trámite documentario

Este prototipo es parte del trabajo final del curso: Sistema de Gestión de Base de Datos I, ciclo 2022-II

#### Integrantes:
| Nombre                              | Código      |
|-------------------------------------|-------------|
| Geraldine Gianella Geronimo Oscanoa | 20210836    |
| Michel Alexis Bañares Gutierrez     | 20210824    |
| André Benjamín Castillo Morín       |  20210829   |
| Alex Jesus Flores Taco              | 20210833    |
| Edwar Frank Carrasco Castañeda      |  20210827   |


![](/img_readme/Login.PNG)

![](/img_readme/dashboard.PNG)

![](/img_readme/registrar.PNG)
 
## PASOS PARA PROBAR EL PROYECTO:
1. Descargar el repositorio.

2. Deven descargar el modulo virtualenv, el proyecto usa un entorno virtual con todos los módulos a usar.

3. Abrir el proyecto con su editor favorito, en mi caso VsCode.

![](/img_readme/vscode_img.PNG)

4. En su editor de SQL favorito ejecutar el script "script_tf.sql" para crear la base de datos que utiliza el prototipo.

5. Ejecutar el archivo app.py ubicado dentro de la carpeta app.

6. Ingresar a: [](http://127.0.0.1:5000/login). Es aquí donde se despliega el proyecto.

7. Podemos empezar a probar las primeras funcionalidades del prototipo, como la busqueda de usuarios registrados en la base de datos, insertar un documento en la base de datos, etc.

8. Para salir, primero debes desactivar el entorno virtual.
~~~ python
#En la terminal ejecutar:
deactivate
~~~
