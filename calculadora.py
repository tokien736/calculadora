class Calculadora:
    def __init__(self, num1, num2, resultado ):
        self.num1 = num1
        self.num2 = num2
        self.result = resultado
    def __str__(self):
        return f"{self.num1} {self.num2} {self.result}"

suma = Calculadora(1, 1 ,2)
print(suma)