#ejercicio 1
#Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
#deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

edad= int(input("Ingrese su edad"))
if edad > 18:
    print ("Usted es mayor")

#2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
#mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
#mensaje “Desaprobado”.

#Defino nota y convierto a numero
nota = int(input("Ingrese su nota"))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

#3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
#número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
#contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
#operador de módulo (%) en Python para evaluar si un número es par o impar.
n1 = int(input("Ingrese un numero par"))
if n1 % 2 == 0:
    print ("Ha ingresado un numero par")
else: 
    print("Por favor, ingrese un numero par")

#4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
#siguientes categorías pertenece:
#● Niño/a: menor de 12 años.
#● Adolescente: mayor o igual que 12 años y menor que 18 años.
#● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
#● Adulto/a: mayor o igual que 30 años.
edad= int(input("Ingrese su edad"))

if edad < 12 :
    print ("usted es un niño")
elif( edad >=12)and (edad< 18): 
    print ("Usted es un adolescente")
elif (edad >=18)and (edad < 30):
    print ("Usted es un adulto joven")
else:
    print ("Usted es un adulto ")


#5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
#(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
#pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
#pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
#de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
#como una lista o un string.
contraseña= len(input("Ingrese una contraseña entre 8 y 14 caracteres"))
if (contraseña >= 8 ) and (contraseña <=14):
    print ("Contraseña correcta")
else:
    print ("Ingrese una contraseña entre 8 y 14 caracteres")

#escribir un programa que tome la liste numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
#hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla. Definir la lista numeros_aleatorios de la siguiente forma:

import random
import statistics as stats
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
media = stats.mean(numeros_aleatorios)
mediana = stats.median (numeros_aleatorios)
moda = stats.mode(numeros_aleatorios)

print (numeros_aleatorios)
print (media)
print (mediana)
print (moda)
if moda < mediana < media:
    print ("Sesgo positivo")
elif media<mediana<moda:
    print ("Sesgo negativo")
else:
 print ("Sin sesgo")
 
 #7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
#pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.
frase =  input(print("Escriba una frase o palabra"))
ultimo = frase [-1]
if ultimo == "a" or ultimo == "e" or ultimo == "i" or ultimo == "o" or ultimo == "u":
    print (frase + "!")
else:
    print (frase)

    #8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee:
#1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
#2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
#3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.}
nombre = input("ingrese su nombre")
print ("Elija una opcion")
print ("1. Si quiere su nombre en mayúsculas")
print ("2. Si quiere su nombre en minúsculas")
print ("3. Si quiere su nombre con la primera letra mayúscula.")

opciones= input ("Elija una opcion (1-3)")
if opciones == "1":
    print (nombre.upper())
elif opciones == "2":
    print(nombre.lower())
elif opciones == "3":
    print (nombre.title())
else:
    print("opcion no valida")

#) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
#agnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado porpantalla:
# Menor que 3: "Muy leve" (imperceptible).
#ayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
# Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero eneralmente no causa daños).
# Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructurasdébiles).
# Mayor o igual que 6 y menor que 7: "Fuerte" (puede causar daños en estructurasdébiles).
# mayor  igualque 7: "Extremo" (puede causar graves daños a gran escala).

magnitud = float(input("Ingrese la magnitud del terremoto"))  
if (magnitud < 3) :
    print ("Muy leve (inperceptible)")   
elif  3<= magnitud < 4:
    print ("Leve (ligeramente perceptible)")
elif  4<= magnitud < 5:
    print ("Moderado (sentido por personas, pero generalmente no causa daño)")
elif  5<= magnitud < 6:
    print ("Fuerte (puede causar daños en estructuras débiles)")
elif 6<= magnitud <7:
    print ("Puede causar daños significativos).")
elif magnitud >=7:
    print ("Extremo (puede causar graves daños a gran escala)")

 #Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
#del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
#si el usuario se encuentra en otoño, invierno, primavera o verano.
# Solicitar datos al usuario

hemisferio = input("¿En qué hemisferio estás? (N/S): ").strip().upper()
mes = int(input("¿Qué mes es? (1-12): "))
dia = int(input("¿Qué día es? (1-31): "))

if hemisferio not in ['N', 'S'] or not (1 <= mes <= 12) or not (1 <= dia <= 31):
    print("Datos inválidos. Verifica el hemisferio, mes y día.")
else:
    if hemisferio == 'N':
        if (mes == 12 and dia >= 21) or mes in [1, 2] or (mes == 3 and dia < 20):
            estacion = "invierno"
        elif (mes == 3 and dia >= 20) or mes in [4, 5] or (mes == 6 and dia < 21):
            estacion = "primavera"
        elif (mes == 6 and dia >= 21) or mes in [7, 8] or (mes == 9 and dia < 22):
            estacion = "verano"
        else:
            estacion = "otoño"
    else:  
        if (mes == 6 and dia >= 21) or mes in [7, 8] or (mes == 9 and dia < 22):
            estacion = "invierno"
        elif (mes == 9 and dia >= 22) or mes in [10, 11] or (mes == 12 and dia < 21):
            estacion = "primavera"
        elif (mes == 12 and dia >= 21) or mes in [1, 2] or (mes == 3 and dia < 20):
            estacion = "verano"
        else:
            estacion = "otoño"

    print(f"Estás en el hemisferio {hemisferio} y la estación es {estacion}.")   