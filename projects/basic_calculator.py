def basic_calculation():
    print("Welcome to the basic calculator")
    print("Please enter the first number")
    num1 = int(input())
    print("Please enter the second number")
    num2 = int(input())
    print("Please enter the operation you would like to perform")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    operation = int(input())
    if operation == 1:
        print("The answer is", num1 + num2)
    elif operation == 2:
        print("The answer is", num1 - num2)
    elif operation == 3:
        print("The answer is", num1 * num2)
    elif operation == 4:
        print("The answer is", num1 / num2)
    else:
        print("Invalid operation")
    print("Thank you for using the basic calculator")

basic_calculation()

def calculadora_basica():
    """
        Función que realiza operaciones básicas
        Argumentos: Ninguno
        Devuelve: Ninguno
    """
    print('Bienvenido a la calculadora básica')
    print('Por favor ingrese el primer número')
    num1 = int(input())
    print('Por favor ingrese el segundo número')
    num2 = int(input())
    print('Por favor ingrese la operación que desea realizar')
    print('1. Suma')
    print('2. Resta')
    print('3. Multiplicación')
    print('4. División')
    operacion = int(input())
    if operacion == 1:
        print('El resultado es: ', num1 + num2)
    elif operacion == 2:
        print('El resultado es: ', num1 - num2)
    elif operacion == 3:
        print('El resultado es: ', num1 * num2)
    elif operacion == 4:
        print('El resultado es: ', num1 / num2)
    else:
        print("Operación invalida")
    print('¡Gracias por usar la calculadora básica!')
    
calculadora_basica()