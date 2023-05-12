print("el número a adivinar está entre 1 y 100, tienes 8 intentos para adivinarlo")

Nombre = input("Ingrese su nombre ")
from random import randint
Numero_Secreto = randint(1, 100)
contador_Intentos = 1
Intentos_restantes = 8


while contador_Intentos <=8:
    Numero_Ingresado = input(f"{Nombre} Ingresa un numero: ")
    
    if not Numero_Ingresado.isdigit():
       print("el número que ingresa tiene que ser entero")
       continue
    else:
        Numero_Ingresado = int(Numero_Ingresado)
        
        if Numero_Ingresado < Numero_Secreto:
            Intentos_restantes -= 1
            contador_Intentos += 1
            print("El número secreto es mayor que el número ingresado. Te quedan", Intentos_restantes)
        elif Numero_Ingresado > Numero_Secreto:
            Intentos_restantes -= 1
            contador_Intentos += 1
            print("El número secreto es menor que el número ingresado. Te quedan", Intentos_restantes)
    if contador_Intentos >=9:
            print("tenes una crotera, ya no tenes más intentos")
              
              
    if Numero_Ingresado == Numero_Secreto:
               print(f"sos un capo el número era: {Numero_Secreto}, adivinaste en el intento: ",contador_Intentos,)
               break
                 
        
        

 
    

         


        




    
    
    
    
            

    
    
    
    
            
    





     
    
 
    
    
 
    
    



    





