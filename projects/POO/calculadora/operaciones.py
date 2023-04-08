class Operadores:
    def __init__(self, a, b):
        self.num1 = a
        self.num2 = b

    def suma(self):
        return self.num1 + self.num2

    def resta(self):
        return self.num1 - self.num2

    def multiplicar(self):
        return self.num1 * self.num2

    def dividir(self):
        return self.num1 / self.num2

def menu():
        print('Menú de Opciones')
        print('Por favor digite el número de la operación que desea realizar')
        print('[1] Sumar')
        print('[2] Restar')
        print('[3] Multiplicar')
        print('[4] Dividir')
        print('[5] Salir') 

def pedir_numero(mensaje):
        num = int(input(mensaje))
        return num
