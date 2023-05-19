# para limpiar la termina#para limpiar la terminall
import os

# para añadir delay al presentar las respuestas
import time

clearConsole = lambda: os.system("cls" if os.name in ("nt", "dos") else "clear")


def continu():
    time.sleep(1)
    clearConsole()
    print(
        "------------------------------------------------.\n¿desea continuar en el menú principal?"
    )
    Lv_select = input("y/n >>")
    if (Lv_select == "y") or (Lv_select == "Y"):
        return True
    elif Lv_select == "n" or (Lv_select == "N"):
        return False
    else:
        print(
            "--------------------------------------------------------\nelección no valida"
        )
        return None


def menuBreakCont():
    Ln_continue = True
    print("-------------Ejercicios con Break-Continue---------------")
    print(" 1. escojer donde se detiene la iteración de una lista")
    Ln_option = int(input(">>"))
    if Ln_option == 0:
        return False
    elif Ln_option == 1:
        print(
            "presentaremos una lista de nombres, escoje uno para detener la iteración en ese nombre e imprimirlo"
        )
        Lst_1 = ["María", "Pedro", "Damian", "Juan"]
        print(Lst_1)
        Lv_nombre = input(">>")
        for nombre in Lst_1:
            if nombre == Lv_nombre:
                print(nombre)
                break
        time.sleep(1)
    elif Ln_option == 2:
        pass
    elif Ln_option == 3:
        pass
    elif Ln_option == 4:
        pass
    elif Ln_option == 5:
        pass
    elif Ln_option == 0:
        pass
    else:
        print("La opción ingresada no es valida")
        time.sleep(3)
    return True


def menuWith():
    Ln_continueWith = True
    print("-------------Ejercicios con with---------------")
    print(
        " 1. ingresar el nombre de un archivo que se creará\n 2. leer archivo de txt y presentarlo "
    )
    Ln_option = int(input(">>"))
    if Ln_option == 0:
        return False
    elif Ln_option == 1:
        print("escriba el nombre del archivo que se creará")
        Lv_nombre = input(">>")
        # crea archivo nuevo con el nombre dado por el usuario
        with open(f"{Lv_nombre}.txt", "t+w") as newFile:
            FL_1 = newFile.write("Hola mundo")
        print("Su archivo fué creado")
        time.sleep(1)
    elif Ln_option == 2:
        # crea nuevo archivo y escribe en el
        with open("newFile.txt", "w") as newFile:
            newFile.write("Hola!!")
        with open("newFile.txt", "a") as newFile:
            newFile.write("\n contenido del archivo .txt")
        # leer el archivo y presentarlo por consola
        with open("newFile.txt", "r") as newFile:
            Lv_file = newFile.read()
        print(Lv_file)
        time.sleep(1)

    elif Ln_option == 3:
        print("")
    elif Ln_option == 4:
        pass
    elif Ln_option == 5:
        pass
    else:
        print("La opción ingresada no es valida")
        time.sleep(3)
    return True


def menuInput():
    print("\n-------------Ejercicios con input---------------")
    print(
        " 1. ingresar numeros y obtener la multiplicación y suma de dos números \n 2. ingresar cadena y obtener su número de vocales\n 3. ingresar cadenas y obtener una nueva\n 4. ingresar un número y obtener su tabla de multiplicar\n 5. ingresar un número y mostrar su factorial "
    )
    Ln_option = int(input(">>"))
    if Ln_option == 0:
        ##finalza ejecución de este submenú y vuelve al menu anterior
        return False
    elif Ln_option == 1:
        print(
            "a continuación ingrese dos números, se mostrará la multiplicación y suma de estos"
        )
        Ln_val = int(input("primer número>>"))
        Ln_val2 = int(input("segundo número>>"))
        print(
            f"la suma de los números ingresados es: {Ln_val+Ln_val2}, y la multiplicación de estos es: {Ln_val2*Ln_val}"
        )
        time.sleep(2)
    elif Ln_option == 2:
        print(
            "a continuación escriba una cadena de texto, se mostrará la cantidad de vocales de dicha cadena"
        )
        Lv_val = input("cadena >>")
        Ln_voc = 0
        Lv_val = Lv_val.upper()
        for i in Lv_val:
            if (i == "A") or (i == "E") or (i == "I") or (i == "O") or (i == "U"):
                Ln_voc += 1
        print(f"la cantidad de vocales en la cadena es: {Ln_voc}")

        time.sleep(2)
    elif Ln_option == 3:
        print(
            "ingrese dos cadenas de texto, se devolverán las dos cadenas como una sola"
        )

        Lv_cad1 = input("cadena 1 >>")
        Lv_cad2 = input("cadena 2 >>")
        Lv_combinación = Lv_cad1 + Lv_cad2
        print(f"la combinación de las cadenas es: {Lv_combinación}")

        time.sleep(2)
    elif Ln_option == 4:
        print(
            "ahora escriba un número, se mostrará la tabla de multiplicar de dicho número"
        )

        Ln_tabla = int(input("número>>"))
        for i in range(1, 11):
            print(f"{Ln_tabla} x {i} = {Ln_tabla*i}")

        time.sleep(2)
    elif Ln_option == 5:
        print("escriba un número, se presentará su factorial")
        Ln_numero = int(input("número>>"))
        Ln_factorial = 1
        for i in range(1, Ln_numero + 1):
            Ln_factorial *= i
        print(f"El factorial de {Ln_numero} es: {Ln_factorial}")

        time.sleep(2)
    else:
        print("La opción ingresada no es valida")
        clearConsole()
    # si devuelve true no regresa al menú principal, si devuelve false regresa al menú principal
    return True


def menuImport():
    Ln_continue = True
    print("-------------Ejercicios con import---------------")
    print("por hacer")
    Ln_option = int(input(">>"))
    if Ln_option == 1:
        pass
    elif Ln_option == 2:
        pass
    elif Ln_option == 3:
        pass
    elif Ln_option == 4:
        pass
    elif Ln_option == 5:
        pass
    elif Ln_option == 0:
        pass
    else:
        print("La opción ingresada no es valida")
        time.sleep(3)
