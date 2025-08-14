# 1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.
print ("Hola mundo!")

#Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
#el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
#por pantalla “Hola Marcos!”.

nombre = input ("Ingrese su nombre")
print (f"Hola!", nombre)
# Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
#imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
#“Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
#años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
#la impresión por pantalla.
nombre= input ("Ingrese su nombre")
apellido = input ("Ingrese su apellido")
edad = input ("Ingrese su edad")
lugarderesidencia= input("Ingrese su lugar de residencia")
print(f"soy {nombre} {apellido} tengo {edad} y vivo en {lugarderesidencia}")

#4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
#su perímetro.
import math

radio= float (input("ingrese el radio del circulo"))
perimetro= round (2* math.pi * radio, 2)
area = round(math.pi * radio**2, 2)
print (f"El perimetro es {perimetro} y el area es {area}")

#5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
#cuántas horas equivale.
segundos= float (input ("ingrese los segundos"))
horas = round (segundos / 3600,2)
print (f"{segundos}segundos , equivalen a {horas}horas")

#Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
#multiplicar de dicho número.
num= int(input("ingrese un numero entero"))
print (f""" {num} x o = {num * 0} 
{num} x 1 = {num * 1}
{num} x 2 = {num * 2}
{num} x 3 = {num * 3}
{num} x 4 = {num * 4}
{num} x 5 = {num * 5}
{num} x 6 = {num * 6}
{num} x 7 = {num * 7}
{num} x 8 = {num * 8}
{num} x 9 = {num * 9}""")

#Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
#pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.
num1= int(input("Ingrese un numero entero"))
num2 = int(input("Ingrese otro numero entero"))
suma = num1 + num2
resta = num1 - num2
multi = num1 * num2
division = num1 / num2
print(f""" 
      La suma es {suma}
      la resta es {resta}
      la multiplicacion es {multi}
      la division es {division}""")

#8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
#de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente
#modo:𝐼𝑀𝐶 = 𝑝𝑒𝑠𝑜 𝑒𝑛 𝑘𝑔 /(𝑎𝑙𝑡𝑢𝑟𝑎 𝑒𝑛 𝑚)**2
peso = float(input("Ingrese su Peso"))
altura = float(input("Ingrese su altura"))
IMC = round (peso / altura **2,2)
print ("Su IMC es de", IMC)

#9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
#pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:
#𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐹𝑎ℎ𝑟𝑒𝑛ℎ𝑒𝑖𝑡 = 9/5 * 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐶𝑒𝑙𝑠𝑖𝑢𝑠 + 32
temp_celcius = float(input("Ingrese la temperatura en grados celcius"))
temp_fahren= 9/5 * temp_celcius + 32
print (f"{temp_celcius} grados celcius equivalen a {temp_fahren} grados fahrenheit")

#10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de dichos números.
num1 = float(input ("Ingrese un numeros enteros"))
num2= float(input ("Ingrese otro numeros enteros"))
num3 = float(input ("Ingrese otro numeros enteros"))
promedio = round ((num1 + num2 + num3 )/ 3, 2)
print ("El promedio es ", promedio)