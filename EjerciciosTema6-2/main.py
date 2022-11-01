class Alumno():
    _nombre_completo = ''
    _nota = 0

    def __init__(self, nombre_completo='', nota=0):
        self._nombre_completo = nombre_completo
        self._nota = nota

    def aprobado(self):
        return self._nota > 6

    def mostrar_si_aprobado(self):
        if self.aprobado():
            return 'SI'
        else:
            return 'NO'

    def mostrar_ficha(self):
        return F'\n -Nombre Completa: {self._nombre_completo},\n -Nota: {self._nota},\n -¿Aprobado?: {self.mostrar_si_aprobado()}'


alu1 = Alumno('Pepe Gomez', 6.5)
print("Datos del Alumno: ", alu1.mostrar_ficha())
print('-------------------------------')
alu2 = Alumno('Mariano Lopez', 3)
print("Datos del Alumno: ", alu2.mostrar_ficha())
