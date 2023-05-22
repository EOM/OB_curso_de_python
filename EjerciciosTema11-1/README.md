# OB Curso de Python
## Ejercicio 11.1
**Enunciado del ejercicio:**

En este ejercicio tendréis que crear una tabla llamada Alumnos que constará de tres columnas: 
la columna id de tipo entero, la columna nombre que será de tipo texto y la columna apellido 
que también será de tipo texto.

Una vez creada la tabla, tenéis que insertarle datos, como mínimo tenéis que insertar 8 alumnos a la tabla.

Por último, tienes que realizar una búsqueda de un alumno por nombre y mostrar los datos por consola.

### Codigo SQL:

```sql
CREATE TABLE Alumnos ( id INTEGER PRIMARY KEY, nombre TEXT NOT NULL, apellido TEXT NOT NULL );

INSERT INTO Alumnos ('nombre','apellido') VALUES ('nombre1','apellido1');
INSERT INTO Alumnos ('nombre','apellido') VALUES ('nombre2','apellido2'); 
INSERT INTO Alumnos ('nombre','apellido') VALUES ('nombre3','apellido3'); 
INSERT INTO Alumnos ('nombre','apellido') VALUES ('nombre4','apellido4'); 
INSERT INTO Alumnos ('nombre','apellido') VALUES ('nombre5','apellido5'); 
INSERT INTO Alumnos ('nombre','apellido') VALUES ('nombre6','apellido6'); 
INSERT INTO Alumnos ('nombre','apellido') VALUES ('nombre7','apellido7'); 
INSERT INTO Alumnos ('nombre','apellido') VALUES ('nombre8','apellido8');

select * FROM Alumnos where id = 8;
8|nombre8|apellido8
```

### Salida en consola:
![Print de pantall ejercicio](img.png)