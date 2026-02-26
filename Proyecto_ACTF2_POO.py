class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.calificaciones = []
        
    # Método para agregar calificación
    def agregar_calificacion(self, nota):
        self.calificaciones.append(nota)
        
    # Método para calcular promedio
    def calcular_promedio(self):
        if len(self.calificaciones) == 0:
            return 0
        return sum(self.calificaciones) / len(self.calificaciones)
    
    # Método para mostrar información
    def mostrar_info(self):
        print("\n--- Información del Estudiante ---")
        print(f"Nombre: {self.nombre}")
        print(f"Calificaciones: {self.calificaciones}")
        print(f"Promedio: {self.calcular_promedio():.2f}")
        
# Lista para guardar estudiantes
estudiantes = []

def buscar_estudiante(nombre):
    for est in estudiantes:
        if est.nombre.lower() == nombre.lower():
            return est
    return None

# Menú interactivo
while True:
    print("\n===== MENÚ =====")
    print("1. Crear estudiante")
    print("2. Agregar calificación")
    print("3. Mostrar estudiante")
    print("4. Mostrar todos los estudiantes")
    print("5. Salir")
    
    opcion = input("Elige una opción: ")
    
    if opcion == "1":
        nombre = input("Nombre del estudiante: ")
        if buscar_estudiante(nombre):
            print("El estudiante ya existe.")
        else:
            estudiantes.append(Estudiante(nombre))
            print("Estudiante creado con éxito.")
            
    elif opcion == "2":
        nombre = input("Nombre del estudiante: ")
        est = buscar_estudiante(nombre)
        
        if est:
            try:
                nota = float(input("Ingrese la calificación: "))
                est.agregar_calificacion(nota)
                print("Calificación agregada.")
            except ValueError:
                print("Entrada inválida. Debe ser un número.")
        else:
            print("Estudiante no encontrado.")
            
    elif opcion == "3":
        nombre = input("Nombre del estudiante: ")
        est = buscar_estudiante(nombre)
        
        if est:
            est.mostrar_info()
        else:
            print("Estudiante no encontrado.")
            
    elif opcion == "4":
        if not estudiantes:
            print("No hay estudiantes registrados.")
        else:
            for est in estudiantes:
                est.mostrar_info()
                
    elif opcion == "5":
        print("Saliendo del programa...")
        break
    
    else:
        print("Opción inválida. Intenta de nuevo.")
        