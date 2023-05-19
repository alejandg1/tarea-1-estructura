print("-------------Ejercicios con input---------------")

print("\n ###### primer ejemplo #####")
print(
    "a continuación ingrese dos números, se mostrará la multiplicación y suma de estos"
)
Ln_val = int(input("primer número>>"))
Ln_val2 = int(input("segundo número>>"))
print(
    f"la suma de los números ingresados es: {Ln_val+Ln_val2}, y la multiplicación de estos es: {Ln_val2*Ln_val}"
)
print("\n ###### segundo ejemplo #####")

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

print("\n ###### tercer ejemplo #####")

print("ingrese dos cadenas de texto, se devolverán las dos cadenas como una sola")

Lv_cad1 = input("cadena 1 >>")
Lv_cad2 = input("cadena 2 >>")
Lv_combinación = Lv_cad1 + Lv_cad2
print(f"la combinación de las cadenas es: {Lv_combinación}")


print("\n ###### cuarto ejemplo #####")


print("ahora escriba un número, se mostrará la tabla de multiplicar de dicho número")

Ln_tabla = int(input("número>>"))
for i in range(1, 11):
    print(f"{Ln_tabla} x {i} = {Ln_tabla*i}")

print("\n ###### quinto ejemplo #####")
print("escriba un número, se presentará su factorial")
Ln_numero = int(input("número>>"))
Ln_factorial = 1
for i in range(1, Ln_numero + 1):
    Ln_factorial *= i
print(f"El factorial de {Ln_numero} es: {Ln_factorial}")
