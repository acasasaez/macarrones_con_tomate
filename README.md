# macarrones_con_tomate
El enlace a nuestro repositorio es el siguiente: https://github.com/acasasaez/macarrones_con_tomate_1.git


    Ejercicio 1:

```
Matriz =[[1,1,1,3],
[2,2,2,7],
[3,3,3,9],
[4,4,4,13]]
def a(m):
    for i in Matriz:
        ia =i[3]
        i.pop()
        b =sum (i)
        i.append(ia)
        if b == ia:
            
            print ("la fila", i, "cumple")
        else:
             print ("la fila", i, "no cumple")
             i.pop()
             i.append(b)
             print( "La fila correcta es", i)


a (Matriz)

```
    Ejercicio 2:

```
def fuct (b = str(input("Introducir cadena"))):
    a = 0
    for i in b:
        a+=1
    if a>= 3 and 10>a:
            print ("La cadena tiene una longitud mayor o igual que 3 y menor que 10 ")
    else:
            print ("La cadena no tiene una longitud mayor o igual que 3 y menor que 10 ")
 
fuct()

```
    Ejercicio 3
    
```
from calendar import c



def funcion(Lista =[]):
    Lista =[]
    while True:
        try:
            a = int(input("Valor de inicio de lista"))
            b =int(input("Valor de fin lista"))
            c =int(input("Valor de diferencia entre valores consecutivos de lista"))
            c!=0
            for i in range (a,b+1,c):
                Lista.append(i)
            print(Lista) 
            break
        except :
            print("Error")

funcion()
funcion()
#Para que se impriman las listas requeridas basta con introducir los parámetros a,b,c correctos
#1ºNúmeros del 0 al 10: a = 0 b= 10 c=1
#2ºNúmeros del -10 al 0: a = -10 b= 0 c=1
#3ºNúmeros pares del 0 al 20  a = 0 b= 20 c=2
#4ºNúmeros impares del -20 al 0 a = -19 b= 0 c=2
#5ºMúltiplos de 5 del 0 al 50 a = 0 b= 50 c=5

```
    Ejercicio 4
```
def funcion():
    while True:
        while True:
            try:
                a = int(input("valor1"))
                b =int(input("valor2"))
            
            
                break
            except :
                print("Error")
           
        if a >=1 and 9>=a and b >=1 and 9>=b:
                for i in range (a):
                    for j in range (b):
                        print("*",end = "" )
                break
        
        else:
                print("Introduzca un número del 1 al 9")

funcion()
