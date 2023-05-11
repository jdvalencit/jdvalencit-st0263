## ST0263 Tópicos especiales en telemática

**Juan David Valencia Torres, [jdvalencit@eafit.edu.co](mailto:jdvalencit@eafit.edu.co)**

**Edwin Nelson Montoya Munera,** [emontoya@eafit.edu.co](mailto:emontoya@eafit.edu.co)

## Laboratorio 5 - Bigdata
### Creación de un cluster con AWS EMR
Escogemos amazon linux y las aplicaciones necesarias para cumplir con el reto
<br >
![1](https://github.com/jdvalencit/jdvalencit-st0263/assets/61478711/a75e31ec-e81e-46bb-b83b-df468ee08b68)
<br >
Utilizamos tipos de instancia m4.xlarge en los diferentes nodos y configuramos la persistencia por medio de un bucket S3 llamado st0263jdvalencit
<br >
![3](https://github.com/jdvalencit/jdvalencit-st0263/assets/61478711/de89f31e-3346-4a83-9eed-ceea0176e4ec)
<br >
Seleccionamos los roles por defecto para el servicio de EMR
<br >
![4](https://github.com/jdvalencit/jdvalencit-st0263/assets/61478711/d4c19a42-5bc2-40c8-9638-1fb8dd1d97ee)
### HUE
Una vez creado un usuario en HUE podemos acceder a la sección files donde encontraremos en HDFS
![5](https://github.com/jdvalencit/jdvalencit-st0263/assets/61478711/f60a482a-ff49-4070-b95e-1201eb5c8f24)
<br >
Creamos el directorio datasets
<br >
![6](https://github.com/jdvalencit/jdvalencit-st0263/assets/61478711/9aec994b-8f27-4085-8311-48663d401949)
<br >
Subimos todos los datasets a esta carpeta por medio de HUE
<br >
![7](https://github.com/jdvalencit/jdvalencit-st0263/assets/61478711/7b127e53-c141-4919-b5f8-c04e20eb466b)
### JupyterHub
Entramos a jupyterhub y creamos un nuevo notebook llamado test, corremos las variables de entonrno spark y sc para comprobar que estamos listos para utilizar spark en jupyter
![8](https://github.com/jdvalencit/jdvalencit-st0263/assets/61478711/a33fb33c-3c96-421d-825d-77d93d8e542c)
Si entramos a S3 podemos ver que contamos con un directorio llamado jovyan dentro de jupyter, en este se encuentra el notebook test creado anteriormente. 
![10](https://github.com/jdvalencit/jdvalencit-st0263/assets/61478711/437f53de-8a88-464b-bf9d-d13befd33f07)
### Zeppelin
Entramos a zeppelin y repetimos los pasos de jupyter para comprobar que estamos listos para utilizar spark en zeppelin y adicionalmente verificamos las bases de datos disponibles
![9](https://github.com/jdvalencit/jdvalencit-st0263/assets/61478711/32a21b0c-32dd-4963-9e9e-8d277674baec)
### SSH
Si entramos al cluster por medio de ssh podemos listar y ver que se encuentran todos los datasets subidos
![11](https://github.com/jdvalencit/jdvalencit-st0263/assets/61478711/dc977434-6cfc-4417-af07-10d43157855b)
Usando el siguiente comando podemos pasar archivos del HDFS al bucket de S3
```bash
hadoop distcp /user/jdvalencit/datasets/sample_data.csv s3a://st0263jdvalencit/datasets/sample_data.csv
```
![12](https://github.com/jdvalencit/jdvalencit-st0263/assets/61478711/2ef60020-372e-4e47-8da3-7558138b5657)
<br >
Luego de repetir esto podemos comprobar que se encuentran subidos todos los datasets a S3
![13](https://github.com/jdvalencit/jdvalencit-st0263/assets/61478711/9304b031-563f-4c6a-ace2-9b74a922a049)

