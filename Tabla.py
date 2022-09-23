def funcion():
    
    while True:
        try:
            a = int(input("valor"))
            b =int(input("valor"))
            
            print("hola")
            break
        except :
            print("Error")
    if a >=1 and 9>=a and b >=1 and 9>=b:
        for i in range (a):
            for j in range (b):
                print("*",end = "" )

funcion()