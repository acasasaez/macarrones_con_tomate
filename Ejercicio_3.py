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