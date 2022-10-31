# OB Curso de Python
## Ejercicio 5
**Enunciado del ejercicio:**

Escribe una función que pueda decirte si un año (número entero) es bisiesto o no.

### Codigo Python:

```python
def es_bisiesto(fecha = 0):
    return ( fecha > 0 and ( (fecha % 400) == 0 or (fecha % 4) == 0 and (fecha % 100) != 0 ))

if(es_bisiesto(408)):
    print("El años es bisiesto")
else:
    print("El año NO es bisiesto")
```
