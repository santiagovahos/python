from operaciones import Operadores, menu, pedir_numero

if __name__ == "__main__":
    calculadora = Operadores(0, 0)
    opc = 0
    while opc == 0:
        while opc >= 0 and opc <= 5:
            menu()
            opc = pedir_numero('Digite la opción que desea: ')
            if opc == 1:
                calculadora.num1 = pedir_numero('Digite el primer número: ')
                calculadora.num2 = pedir_numero('Digite el segundo número: ')
                print('El resultado de la suma es: ', calculadora.suma())
            elif opc == 2:
                calculadora.num1 = pedir_numero('Digite el primer número: ')
                calculadora.num2 = pedir_numero('Digite el segundo número: ')
                print('El resultado de la resta es: ', calculadora.resta())
            elif opc == 3:
                calculadora.num1 = pedir_numero('Digite el primer número: ')
                calculadora.num2 = pedir_numero('Digite el segundo número: ')
                print('El resultado de la multiplicación es: ', calculadora.multiplicar())
            elif opc == 4:
                calculadora.num1 = pedir_numero('Digite el primer número: ')
                calculadora.num2 = pedir_numero('Digite el segundo número: ')
                print('El resultado de la división es: ', calculadora.dividir())
            elif opc == 5:
                print('Gracias por usar la calculadora')
                break
            else:
                pass
        else:
            print('Opción no válida')
            opc = 0