import string
import itertools

def fuerza_bruta(contrañesa_objetivo):
    caracteres = string.ascii_letters + string.digits
    intentos = 0
    print("Iniciando ataque de contraseña...")
    
    for longitud in range(1, 20):
        for intento in map(''.join, itertools.product(caracteres, repeat=longitud)):
            intentos += 1
            if intento == contrañesa_objetivo:
                print(f"Contraseña encontrada: {intento}")
                print(f"he tardado: {intentos} intentos")
                return
    print ("No se ha encontrado la contraseña")

contraseña = input("Contraseña a adivinar: ")
fuerza_bruta(contraseña)
