#clase alumno

class alumno:

    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def resultado(nota):
        if (nota >=5):
            print(f"el alumno {alumno_1.nombre} ha sacado un {nota} y por tanto ha aprobado.")
        else:
            print(f"el alumno {alumno_1.nombre} ha sacado un {nota} y por tanto ha suspendido.")

#creamos un objeto p1 que es una instancia de la clase persona
alumno_1 = alumno("Marta", 9)
    
print(f"El nombre del alumno es: {alumno_1.nombre}") #pedimos nombre
print(f"La nota de {alumno_1.nombre} es un {alumno_1.nota}") #pedimos edad



