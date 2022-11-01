# OB Curso de Python
## Ejercicio 6.1
**Enunciado del ejercicio:**

En este ejercicio vais a crear la clase Vehículo la cual tendrá los siguientes atributos:

- Color
- Ruedas
- Puertas

Por otro lado crearéis la clase Coche la cual heredará de Vehículo y tendrá los siguientes atributos:

- Velocidad
- Cilindrada

Por último, tendrás que crear un objeto de la clase Coche y mostrarlo por consola.

### Codigo Python:

```python
class Vehiculo():
    _color = ''
    _ruedas = 0
    _puertas = 0

    def __init__(self, color='', ruedas=0, puertas=0):
        self._color = color
        self._ruedas = ruedas
        self._puertas = puertas

    def caracteristicas(self):
        return F'Color:{self._color}, Ruedas:{self._ruedas}, Puertas:{self._puertas}'

    def __str__(self):
        return F'{self.__class__}: {self.caracteristicas()}'


class Coche(Vehiculo):
    def __init__(self, color='', ruedas=4, puertas=4):
        super().__init__(color, ruedas, puertas)

    def caracteristicas(self):
        return F'Caracteristicas del Coche: {super().caracteristicas()}'


coche_familiar = Coche('Rojo')
print("Auto Familiar: ", coche_familiar.caracteristicas())

print('-------------------------------')

coche_deportivo = Coche('Amarillo', 4, 2)
print("Auto Deportivo: ", coche_deportivo.caracteristicas())
```
