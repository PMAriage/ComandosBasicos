"""Paul Kelem Mariage Pimentel"""

import subprocess

def ejecutar(comando):
    resultado = subprocess.run(comando, shell=True, stdout=subprocess.PIPE, text=True)
    print(resultado.stdout)

def mostrar_menu():
    print("1. Crear archivo promedio")
    print("2. Crear carpeta calificaciones")
    print("3. Crear carpeta primer parcial")
    print("4. Mover archivo a primer parcial")
    print("5. Crear archivo comandos.py")
    print("6. Listar carpetas")
    print("7. Abrir calculadora")
    print("8. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            ejecutar("touch ~/promedio.txt")
        elif opcion == "2":
            ejecutar("mkdir ~/calificaciones")
        elif opcion == "3":
            ejecutar("mkdir ~/calificaciones/primer_parcial")
        elif opcion == "4":
            ejecutar("mv ~/promedio.txt ~/calificaciones/primer_parcial")
        elif opcion == "5":
            ejecutar("touch ~/calificaciones/comandos.py")
        elif opcion == "6":
            ejecutar("ls -l")
        elif opcion == "7":
            ejecutar("python3 /home/ubuntu/calculadora.py")
        elif opcion == "8":
            print("Saliendo...")
            break
        else:
            print("Opción no válida")
            
main()
