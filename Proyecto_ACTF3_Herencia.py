# Clase base
class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.calificaciones = []
        
    def agregar_calificacion(self, nota):
        self.calificaciones.append(nota)
        
    def calcular_promedio(self):
        if len(self.calificaciones) == 0:
            return 0
        return sum(self.calificaciones) / len(self.calificaciones)
    
    def mostrar_info(self):
        print(f"\nNombre: {self.nombre}")
        print(f"Calificaciones: {self.calificaciones}")
        print(f"Promedio: {self.calcular_promedio():.2f}")
        
# Primera clase derivada
class EstudiantePregrado(Estudiante):
    def __init__(self, nombre, carrera):
        super().__init__(nombre)   # Reutiliza constructor de la clase base
        self.carrera = carrera
        
    def mostrar_info(self):
        super().mostrar_info()
        print(f"Carrera: {self.carrera}")
        print("Tipo: Estudiante de Pregrado")
        
# Segunda clase derivada
class EstudiantePosgrado(Estudiante):
    def __init__(self, nombre, investigacion):
        super().__init__(nombre)
        self.investigacion = investigacion
        
    def mostrar_info(self):
        super().mostrar_info()
        print(f"Línea de investigación: {self.investigacion}")
        print("Tipo: Estudiante de Posgrado")
        
# Lista para almacenar estudiantes
estudiantes = []

def buscar_estudiante(nombre):
    for e in estudiantes:
        if e.nombre.lower() == nombre.lower():
            return e
    return None

# Menú interactivo
while True:
    
    print("\n===== MENÚ =====")
    print("1. Crear estudiante de pregrado")
    print("2. Crear estudiante de posgrado")
    print("3. Agregar calificación")
    print("4. Mostrar estudiantes")
    print("5. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        nombre = input("Nombre: ")
        carrera = input("Carrera: ")
        
        estudiante = EstudiantePregrado(nombre, carrera)
        estudiantes.append(estudiante)
        
        print("Estudiante de pregrado creado.")
        
    elif opcion == "2":
        nombre = input("Nombre: ")
        investigacion = input("Línea de investigación: ")
        
        estudiante = EstudiantePosgrado(nombre, investigacion)
        estudiantes.append(estudiante)
        
        print("Estudiante de posgrado creado.")
        
    elif opcion == "3":
        nombre = input("Nombre del estudiante: ")
        
        estudiante = buscar_estudiante(nombre)
        
        if estudiante:
            nota = float(input("Ingrese la calificación: "))
            estudiante.agregar_calificacion(nota)
            print("Calificación agregada.")
        else:
            print("Estudiante no encontrado.")
            
    elif opcion == "4":
        for e in estudiantes:
            e.mostrar_info()
            
    elif opcion == "5":
        print("Saliendo del programa...")
        break
    
    else:
        print("Opción inválida.")
        