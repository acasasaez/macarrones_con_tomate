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
