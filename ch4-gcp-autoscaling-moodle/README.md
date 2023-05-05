## ST0263 Tópicos especiales en telemática
```
Presentado por:
- Juan David Valencia Torres, [jdvalencit@eafit.edu.co](mailto:jdvalencit@eafit.edu.co)
- David Cardona Nieves, [djcardonan@eafit.edu.co](mailto:djcardonan@eafit.edu.co)

Presentado a:
- Edwin Nelson Montoya Múnero, [emontoya@eafit.edu.co](mailto:emontoya@eafit.edu.co)
```

## 1) Description

Este reto consistió en el despliegue de Moodle utilizando servicios de Google Cloud Platform (GCP). Entre las herramientas utilizadas encontramos:

- [x] Balanceador de carga.
- [x] Servidor NFS usando Filestore.
- [x] Base de datos (MySQL) usando Cloud SQL. 

Este despliegue se realizó cumpliendo con los siguientes requisitos propuestos:

- [x] NFS deployment via a [GCP/NetApp](https://cloud.google.com/architecture/partners/netapp-cloud-volumes/creating-nfs-volumes) volume.
- [x] MySQL database deployment via [GCP Cloud SQL](https://cloud.google.com/sql) service.
- [x] Autoscaling of Moodle instances via [GCP instance groups](https://cloud.google.com/compute/docs/instance-groups).
- [x] Load balancing of instance group via a [GCP load balancer](https://cloud.google.com/load-balancing)
- [x] LMS can be reached via sub-domain `reto4.sebastianpg.pro`.
- [x] SSL certificates for wildcard domain `*.sebastianpg.pro`.
- [x] DNS zone management via [Google Cloud DNS](https://cloud.google.com/dns).

## 2) Architecture

La arquitectura propuesta se compone por máximo 4 instancias de Moodle que conectándose tanto a la base de datos como a la instancia NFS permiten a un cliente que
se conecta por medio de un navegador web visualizar el aplicativo de Moodle accediendo al dominio [dominuwu.online](dominuwu.online).

A continuación se presenta el diseño implementado para esta arquitectura:

## 3) Development environment

Este reto fué desarrollado bajo los siguientes lineamientos:
- Versión Ubuntu: 22.04
- Versión MySQL: 8.0
- Versión Docker: 20.10.21
- Versión Docker-compose 1.29.2
- Versión Nfs-common: 2.6.1

## 4) Deployment details

### 4.1) NFS server

Para el NFS decidimos implementar el servicio de FileStore ofrecido por GCP. Las instancias de Filestore son servidores de archivos NFS completamente administrados
en Google Cloud para usarlos con aplicaciones que se ejecutan en instancias de máquinas virtuales (VM) de Compute Engine o clústeres de Google Kubernetes Engine.

Además de utilizar el paquete **nfs-common** creamos el archivo **fstab** para permitir que las instancias realicen el montaje del NFS de forma autónoma cada vez que son iniciadas.

### 4.2) Mysql Cloud Service

Para la base de datos utilizamos CloudSQL donde creamos una instancia llamada "moodle db". Dentro de esta instancia creamos la base de datos asignándole el mismo nombre (moodledb).
Para esta mantuvimos el usuario por default, es decir, el usuario **root*.

### 4.3) Virtual machine image and instance template

Una imagen es una instantánea o copia de seguridad de una instancia de máquina virtual (VM) en GCP. Esta imagen puede utilizarse para crear una nueva instancia de VM con la misma configuración
y aplicaciones que la instancia original. En nuestro caso creamos la imagen moodle-image1.

### 4.4) Instance groups

Los grupos de instancias nos permiten proporcionar al sistema escalabilidad automática y alta disponibilidad al distribuir la carga de trabajo en múltiples instancias (en nuestro caso, desde
un mínimo de 1 instancia y un máximo de 4). En nuestro caso creamos el grupo **moodle-group** siguiendo la plantilla moodle-template. Este grupo cuenta con autoescalado horizontal que le permite
añadir nuevas instancias una vez que se llega a un techo de uso de CPU (siendo este de alrededor del 60%).

### 4.5) Static external IP


### 4.6) Hostinger DNS

Conservamos el DNS ofrecido por el host utilizado para el dominio, es decir, Hostinger. Para la configuración de este pusimos el registro tipo A apuntando a la IP externa de nuestro balanceador
de carga.

### 4.7) SSL certificates and Domain


### 4.8) Load balancer

Para el balanceador de carga establecimos una división en 2 "secciones", siendo estas el backend y el frontend, de forma que:

- **Backend:** está conformado por el grupo de instancias que reciben el tráfico de red del balanceador de carga. Es decir, es el destino final de las solicitudes que son recibidas y procesadas
por el balanceador de carga. Para esto se creó un servicio de backend llamado moodle-service que toma el moodle-group y permite el balanceo de la carga entre las instancias activas de este grupo.
De igual forma este cuenta con un estado de verificación llamado moodle-state.
- **Frontend:** está conformado por la interfaz de red a través de la cuál el balanceador de carga recibe y procesa el tráfico de los clientes. Es decir, es el punto de entrada de las
solicitudes que son recibidas desde la red externa al sistema.

Configuramos la ip estática 34.149.194.81 con el protocolo HTTPS y un certificado SSL llamado cert obtenido a partir de las herramientas de Certificate Manager de GCP.

## 5) Demo video with explanation

## 6) References
