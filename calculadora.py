from os import system

class Calculadora:
    def __init__(self, num1, num2  ):
        self.num1 = num1
        self.num2 = num2

    def __str__(self):
        return f"{self.num1} {self.num2} {self.result}"
        
    def suma(self ):
        self.result = self.num1 + self.num2
        print('La suma es: ', self.result)
        return 

    def resta(self ):
        self.result = self.num1 - self.num2
        print('La resta es: ', self.result)
        return 

    def multiplicacion(self ):
        self.result = self.num1 * self.num2
        print('La multiplicaión es: ', self.result)
        return 
    def division(self ):
        self.result = self.num1 / self.num2
        print('La división es: ', self.result)
        return             


while True: 
    try:
        print("===================")
        print("======MENÚ========")
        print("===================")
        print("1. Suma ")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Salir")


        opc = int(input("Ingrese una opcion: "))
        if opc == 1:
            while True:
                try:
                    print("=====SUMA=====")
                    x = int(input("Ingrese el primero numero: "))
                    y = int(input("Ingrese el segundo numero: "))
                    c = Calculadora(x, y) 
                    c.suma()
                    break
                except ValueError:
                    print("Por favor, ingrese solo numeros")
                    respuesta = input("Desea volver a ingresar los datos? [s/n]: ")
                    if respuesta == "n":
                        break
        elif opc == 2:
            while True:
                try:
                    print("=====RESTA=====")
                    x = int(input("Ingrese el primero numero: "))
                    y = int(input("Ingrese el segundo numero: "))
                    c = Calculadora(x, y) 
                    c.resta()
                    break
                except ValueError:
                    print("Por favor, ingrese solo numeros")
                    respuesta = input("Desea volver a ingresar los datos? [s/n]: ")
                    if respuesta == "n":
                        break      
        elif opc == 3:
            while True:
                try:
                    print("=====MULTIPLICACIÓN=====")
                    x = int(input("Ingrese el primero numero: "))
                    y = int(input("Ingrese el segundo numero: "))
                    c = Calculadora(x, y) 
                    c.multiplicacion()
                    break
                except ValueError:
                    print("Por favor, ingrese solo numeros")
                    respuesta = input("Desea volver a ingresar los datos? [s/n]: ")
                    if respuesta == "n":
                        break       
        elif opc == 4:
            while True:
                try:
                    print("=====DIVISION=====")
                    x = int(input("Ingrese el primero numero: "))
                    y = int(input("Ingrese el segundo numero: "))
                    c = Calculadora(x, y) 
                    c.division()
                    break
                except ValueError:
                    print("Por favor, ingrese solo numeros")
                    respuesta = input("Desea volver a ingresar los datos? [s/n]: ")
                    if respuesta == "n":
                        break      
                except ZeroDivisionError:
                    print("ALERTA, ESTA DIVIDIENDO UN NUMERO ENTRE CERO")
                    respuesta = input("Desea volver a ingresar los datos? [s/n]: ")
                    if respuesta == "n":
                        break     
        elif opc == 5:
            system("cls")
            print("Gracias por Ingresar al Programa")
            break                                                                   
    except ValueError:
        print("Por favor, ingrese solo numeros")
        respuesta = input("Desea volver a ingresar los datos? [s/n]: ")
        if respuesta == "n":
            break
     




