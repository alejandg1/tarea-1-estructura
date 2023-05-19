import modules
import time


def menu():
    Lb_continueMain = True
    print("Bienvenido, seleccione uno de las siguientes funcionalidades")
    Gn_opcion = 1
    while Lb_continueMain:
        print(
            "--------------------------------------------------------------------- \n 1. Sentencias Break / continue \n 2. Sentencia import \n 3. Sentencia input \n 4. Sentencia with \n ######## 0. finalizar ejecución  ########"
        )
        print(
            "----------------------escriba su elección----------------------------------------"
        )
        Gn_opcion = int(input(">>"))

        if Gn_opcion == 1:
            print("--------------------------------------------------------------")
            Lb_conti = modules.menuBreakCont()
            if not Lb_conti:
                continue
            else:
                modules.menuBreakCont()

        elif Gn_opcion == 2:
            print("--------------------------------------------------------------")
            modules.menuImport()
            time.sleep(3)

        elif Gn_opcion == 3:
            print("--------------------------------------------------------------")
            Lb_conti = modules.menuInput()
            if not Lb_conti:
                continue
            else:
                modules.menuInput()

        elif Gn_opcion == 4:
            print("--------------------------------------------------------------")
            Lb_conti = modules.menuWith()
            if not Lb_conti:
                continue
            else:
                modules.menuWith()
            time.sleep(3)
        else:
            print("La opción ingresada no es valida")
            time.sleep(3)
        Lb_continueMain = modules.continu()
        if Lb_continueMain == None:
            while Lb_continueMain == None:
                Lb_continueMain = modules.continu()


menu()
