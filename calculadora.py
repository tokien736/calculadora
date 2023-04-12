class Calculadora:
    def __init__(self, num1, num2,  ):
        self.num1 = num1
        self.num2 = num2

    def __str__(self):
        return f"{self.num1} {self.num2} {self.result}"
        
    def suma(self ):
        self.result = self.num1 + self.num2
        print('La suma es: ', self.result)
        return 
suma = Calculadora(1,2)
suma.suma()
