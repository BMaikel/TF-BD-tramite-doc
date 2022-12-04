LA MOLINA - UNALM
# TF_BBDD
Prototipo: Sistema de trámite documentario.\
Intento de realizar el prototipo en python usando el módulo Flask.

![](/img_readme/buscador_img.PNG)
![](/img_readme/login_img.PNG)
![](/img_readme/p1_img.PNG)
 
## PASOS PARA PROBAR EL PROYECTO:
1. Descargar el repositorio.
2. Deven descargar el modulo virtualenv, el proyecto usa un entorno virtual con todos los módulos a usar.
~~~ python
#Ver módulos instalados que tienes:
pip list
~~~
~~~ python
#Si no tienes virutalenv lo instalas:
pip install virtualenv
~~~
3. Abrir el proyecto con su editor favorito, en mi caso VsCode.
![](/img_readme/vscode_img.PNG)
4. Activar el entorno virtual.
~~~ python
#En la terminal ejecutar:
.\env\Scripts\activate
#Sabrán que se activó porque veran la terminal de esta forma:
~~~
![](/img_readme/terminal_img.PNG)
5. Ahora solo ejecutan el archivo app.py dentro de la carpeta app.

6. Para salir, primero debes desactivar el entorno virtual.
~~~ python
#En la terminal ejecutar:
deactivate
~~~