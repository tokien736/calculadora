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
prueba = Calculadora(4,2)
prueba.suma()
prueba.resta()
prueba.multiplicacion()
prueba.division()

