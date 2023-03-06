## ST0263 Tópicos especiales en telemática

**Juan David Valencia Torres, [jdvalencit@eafit.edu.co](mailto:jdvalencit@eafit.edu.co)**

**Edwin Nelson Montoya Munera,** [emontoya@eafit.edu.co](mailto:emontoya@eafit.edu.co)

## Laboratorio de implementación de MOM y gRPC

### 1. Descripción de la Actividad

En el reto se diseñó e implementó una API Gateway utilizando fastAPI, que se integró con dos microservicios: uno implementado en gRPC y el otro en RabbitMQ. La API Gateway se configuró para enrutar las solicitudes recibidas a los microservicios correspondientes permitiendo que los clientes de la API interactúen con ambos microservicios a través de una sola interfaz.

Para integrar el servicio gRPC con la API Gateway, se creó y configuró un cliente gRPC con sus respectivos protobuffers para establecer una comunicación estable con el servidor gRPC ubicado en el microservicio.

Por otro lado, para integrar el servicio RabbitMQ con la API Gateway, se creó un cliente rpc que permitió la comunicación entre la API Gateway y el servicio RabbitMQ, para establecer la comunicación con el microservicio.

### 1.1. Aspectos cumplidos

- La API Gateway debe ser capaz de enrutar las solicitudes recibidas a los microservicios usando balanceo de carga.
- La API Gateway debe ser capaz de integrarse con dos microservicios diferentes: uno implementado en gRPC y otro en RabbitMQ.
- La API Gateway debe ser capaz de listar los archivos que se encuentran en una carpeta especificada en la configuración, esto implementados en ambos microservicios.
- La API Gateway debe ser capaz de buscar un archivo concreto en una carpeta especificada en la configuración, esto implementados en ambos microservicios.
- Tanto la API Gateway como los dos microservicios deben soportar múltiples peticiones simultaneas y dar respuesta a todas ellas.

### 1.2. Aspectos por cumplir

- Se puede presentar un despliegue más profesional usando herramientas como docker.
- Realizar un script bootstrap que pueda encender el sistema al iniciar el equipo, en lugar de presentar un script manual para hacerlo.

### 2. Estructura de la aplicación

```mermaid
graph TD
		API_GateWay --> MOM --> microservicio1
	  API_GateWay --> gRPC --> microservicio2
		
```

### 3. Ambiente de desarrollo

**3.1. A continuación se presenta la lista de las tecnologías usadas para el desarrollo del reto:**

- pyhton, versión: 3.11.2,
- fastAPI, versión: 0.92.0
- pika, versión: 1.3.1
- grpcio, versión: 1.51.3
- uvicorn, versión: 0.20.0
- nginx, versión: 1.18.0
- rabbitMQ, versión: 3.9.13

**3.2 Compilación y ejecución**

Al ser desarrollado en python no se debe compilar ningún archivo, solo se debe correr el archivo [start.sh](http://start.sh) presente en /home/ubuntu

```bash
/home/ubuntu:~$ ./start.sh
```

Este archivo se encarga de activar todos los recursos y necesarios para la correcta ejecución del proyecto.

**3.3 Configuración**

El proyecto cuenta con archivos config.json ubicados en diferentes puntos para ser usados como archivos de configuración.

El proyecto cuenta con los siguientes archivos:

- Configuración del cliente de la comunicación rpc de rabbiMQ

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/9bb32869-b153-4ccf-ae53-086971a20c72/Untitled.png)

- Configuración para los dos microservicios (RPC y gRPC)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/533f8b49-cb4c-40bd-8a07-96aaef35b8e3/Untitled.png)

- Configuración del cliente de la comunicación gRPC.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/b017134d-3676-4b24-92a2-f2ebc1173373/Untitled.png)

**3.4 Estructura completa de directorios**

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/99c01d11-74d3-464e-9481-1884bfd7bf7a/Untitled.png)

### 4. IP del proyecto

Para el desarrollo del proyecto se hizo uso de una ip eslástca otorgada por AWS para así mantener una consistencia en cuanto la ip usada para acceder a la api.

**4.1 Proyecto en ejecución**

Si llamamos el servicio con la url:

```bash
http://52.203.226.106/list
```

La API GateWay nos dirigirá a uno de los microservicios para obtener respuesta de nuestra petición

```json
["method: MOM ","dir: /home/ubuntu/jdvalencit-st0263/ch2-mom-grcp/microservices/files","files: ['file2.txt', 'file3.txt', 'file1.txt']","dir: /home/ubuntu/jdvalencit-st0263/ch2-mom-grcp/microservices/files/newfiles","files: ['nf5.txt', 'nf4.txt']"]
```

Un posible resultado a una petición list es la anterior, cuenta con el método usado para obtener respuesta, ya sea por medio del MOM o por medio de gRPC y la información de los directorios y archivos presentes. 

### 5. Guía de uso

La API GateWay expone dos funciones para los usuarios, list y search.

- [http://52.203.226.106/list](http://52.203.226.106/list): Esta función lista todos los archivos y directorios que se encuentren en el directorio path_dir de la configuración.
- [http://52.203.226.106/search/{nombre del archivo a buscar}/](http://52.203.226.106/list): Esta función busca el archivo especificado en directorios que se encuentren en el directorio path_dir de la configuración.

### Referencias:

- Tutorial de RabbitMQ: [https://www.rabbitmq.com/tutorials/tutorial-six-python.html](https://www.rabbitmq.com/tutorials/tutorial-six-python.html)
- Configuración de nginx para el despliegue de la api: [https://www.youtube.com/watch?v=SgSnz7kW-Ko](https://www.youtube.com/watch?v=SgSnz7kW-Ko)
- Guía en python de gRPC: [https://grpc.io/docs/languages/python/quickstart/](https://grpc.io/docs/languages/python/quickstart/)

V**ersión [README.md](http://readme.md/) -> 1.0 (2023-Marzo)**
