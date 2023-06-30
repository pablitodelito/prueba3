alumnos = []

def registrar_alumnos():
    nombre = input("Ingrese el nombre del alumno: ")
    apellido = input("Ingrese el apellido del alumnno: ")
    rut = input("Ingrese el rut del alumno, sin puntos solo coma: ")
    fecha_nacimiento = input("Ingrese la fecha de nacimiento del alumno: ")
    carrera = input("Ingrese la carrera del alumno: ")
    asignatura = input("Ingrese la asignatura: ")
    

    alumno = {
        "nombre": nombre,
        "apellido": apellido,
        "rut": rut,
        "fecha_nacimiento": fecha_nacimiento,
        "carrera": carrera,
        "asignatura": asignatura,
        "promedio": promedio

    }

    asignaturas = []
    promedio = 0.0

    num_asignaturas = int(input("Ingrese el número de asignaturas: "))
    for _ in range(num_asignaturas):
        asignatura = input("Ingrese el nombre de la asignatura: ")
        prom = float(input("Ingrese el promedio de la asignatura: "))
        while prom < 1.0 or prom > 7.0:
            print("Promedio inválido.")
            prom = float(input("Ingrese el promedio de la asignatura: "))
        asignaturas.append((asignatura, prom))
        promedio += prom

    promedio /= num_asignaturas

    alumnos.append(alumno, asignaturas, promedio)
    print("Alumno registrado con éxito: ")


def buscar_alumnos():
    rut_buscar = input("Ingrese el rut del alumno que desea buscar: ")

    for alumno in alumnos:
        if alumno['rut'] == rut_buscar:
            print("Informacion del alumno:")
            print(f"rut:{alumno['rut']}")
            print(f"nombre:{alumno['nombre']}")
            print(f"apellido:{alumno['apellido']}")
            print(f"fecha_nacimiento:{alumno['fecha_nacimiento']}")
            print(f"carrera:{alumno['carrera']}")
            print(f"asignatura:{alumno['asignatura']}")
            for asignatura, promedio in alumno["asignaturas"]:
                print(asignatura + ":" promedio)
            return
    print("Alumno no encontrado, por favor ingresar un rut válido: ")

def imprimir_certificados():
    rut_certificados = input("Ingrese el rut del alumno que desea buscar: ")

    for alumno in alumnos:
        if alumno['rut'] == rut_certificados:
            print("Certificado de alumno regular:")
            print(f"rut:{alumno['rut']}")
            print(f"nombre:{alumno['nombre']}")
            print(f"apellido:{alumno['apellido']}")
            print(f"fecha_nacimiento:{alumno['fecha_nacimiento']}")
            print(f"carrera:{alumno['carrera']}")
            print(f"asignatura:{alumno['asignatura']}")
            return
    print("Alumno no encontrado, por favor ingresar un rut válido: ")    

while True:
    print("------Menú------")
    print("1.-Registrar alumno")
    print("2.-Buscar alumno")
    print("3.-Imprimir certificado de alumno regular")
    print("4.-Salir")

    opción = input("Ingrese el numero de la opción que desea ejecutar: ")

    if opción == "1":
        registrar_alumnos()
    elif opción == "2":
        buscar_alumnos()
    elif opción == "3":
        imprimir_certificados()
    elif opción == "4":
        print("Gracias por utilizar el programa, hasta luego: ")
    else:
        print("Opción inválida. Por favor ingrese un número válido")











