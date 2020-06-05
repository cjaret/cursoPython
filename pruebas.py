import turtle

def main(): #Esta será la función principal
    window = turtle.Screen() #Abrimos la ventana
    tortuga = turtle.Turtle() #Generar una tortuga

    mksquare(tortuga) #Haz un cuadrado
    turtle.mainloop() #Mantener la ventana abierta

def mksquare(tortuga):
    length = int(input("Qué tan grande quieres tu cuadrado: "))
    
    for i in range(4):
        mklineAndTurn(tortuga, length)

def mklineAndTurn(tortuga, length):
    tortuga.forward(length)
    tortuga.left(90)
    


""" 

Es importante definir dónde tienen que empezar los programas en python, pues son una secuencia de comandos y tienen que iniciar en algún lugar. Python le llama main a los archivos que corre.

"""

if __name__ == "__main__": #Si el nombre de este archivo es igual al main que estás corriendo, ejecuta la función main
    main()