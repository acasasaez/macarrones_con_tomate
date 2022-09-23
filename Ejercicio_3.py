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

