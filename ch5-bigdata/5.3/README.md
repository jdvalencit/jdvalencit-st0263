# Reto 5.3
## Parte 2
![1](https://github.com/jdvalencit/jdvalencit-st0263/assets/61478711/fd769bb9-344b-495f-8f5e-3aea92ef91c7)
![2](https://github.com/jdvalencit/jdvalencit-st0263/assets/61478711/a7deb228-a11d-4d09-b6c4-e0b3e44c9b1c)
**1. ejecutar el wordcount por linea de comando con datos en HDFS.**
![3](https://github.com/jdvalencit/jdvalencit-st0263/assets/61478711/6c9ec14a-b859-4979-b9e1-da1475896ec0)
**2. ejecutar el wordcount por linea de comando con datos en S3.**
![4](https://github.com/jdvalencit/jdvalencit-st0263/assets/61478711/92064587-06d8-4443-ae11-b689b569256e)
**3. ejecutar el wordcount en JupyterHub Notebooks con datos en S3.**
![5](https://github.com/jdvalencit/jdvalencit-st0263/assets/61478711/2473621d-6613-4537-aebe-5b91323ef4bb)
**4. Explicación paso a paso de Data_processing_using_PySpark.ipynb.**
1. Importar la clase SparkSession de la biblioteca pyspark.sql
2. Crear una instancia de SparkSession llamada "spark"
3. Cargar un archivo CSV en un DataFrame llamado "df"
4. Obtener los nombres de las columnas del DataFrame
5. Obtener el número de columnas del DataFrame
6. Obtener el número de registros en el DataFrame
7. Imprimir la forma (número de registros y número de columnas) del DataFrame
8. Imprimir el esquema del DataFrame
9. Mostrar las primeras 5 filas del DataFrame
10. Seleccionar solo 2 columnas ('age' y 'mobile') del DataFrame y mostrar las primeras 5 filas
11. Mostrar información estadística sobre el DataFrame
12. Importar tipos de datos (StringType, DoubleType, IntegerType) de la clase pyspark.sql.types
13. Agregar una nueva columna al DataFrame que calcule la edad después de 10 años
14. Agregar una nueva columna al DataFrame que convierta la columna 'age' a tipo Double
15. Filtrar registros del DataFrame donde el valor de la columna 'mobile' sea 'Vivo'
16. Filtrar registros del DataFrame que cumplan múltiples condiciones (valor de 'mobile' es 'Vivo' y valor de 'experience' es mayor a 10)
17. Filtrar registros del DataFrame que cumplan múltiples condiciones usando operadores lógicos
18. Mostrar los valores distintos en la columna 'mobile'
19. Contar el número de valores distintos en la columna 'mobile'
20. Agrupar por la columna 'mobile' y contar el número de registros en cada grup
21. Agrupar por la columna 'mobile' y calcular la media de cada columna numérica en cada grupo
22. Guardar el DataFrame como un archivo CSV
23. Guardar el DataFrame como un archivo Parquet
