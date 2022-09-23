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
