def suma(a, b):
    """Retorna la suma de dos números."""
    return a + b

def resta(a, b):
    """Retorna la resta de dos números."""
    return a - b

def multiplicacion(a, b):
    """Retorna la multiplicación de dos números."""
    return a * b

def division(a, b):
    """Retorna la división de dos números.
    
    Lanza un error si el divisor es cero.
    """
    if b == 0:
        raise ValueError("No se puede dividir entre cero.")
    return a / b

def potencia(base, exponente):
    """Retorna la base elevada al exponente."""
    return base ** exponente

def raiz_cuadrada(valor):
    """Retorna la raíz cuadrada de un número.
    
    Lanza un error si el número es negativo.
    """
    if valor < 0:
        raise ValueError("No se puede calcular la raíz cuadrada de un número negativo.")
    return valor ** 0.5

def calculadora():
    """Función principal que gestiona el menú y la ejecución de operaciones matemáticas."""
    while True:
        print("\nOpciones de la Calculadora:")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Potencia")
        print("6. Raíz Cuadrada")
        print("7. Salir")

        opcion = input("Seleccione una opción (1-7): ")

        if opcion == '7':
            print("Gracias por usar la calculadora.")
            break

        if opcion in {'1', '2', '3', '4', '5', '6'}:
            if opcion in {'1', '2', '3', '4', '5'}:
                num1 = float(input("Ingrese el primer número: "))
                num2 = float(input("Ingrese el segundo número: "))

            if opcion == '1':
                print(f"Resultado: {suma(num1, num2)}")
            elif opcion == '2':
                print(f"Resultado: {resta(num1, num2)}")
            elif opcion == '3':
                print(f"Resultado: {multiplicacion(num1, num2)}")
            elif opcion == '4':
                try:
                    print(f"Resultado: {division(num1, num2)}")
                except ValueError as e:
                    print(e)
            elif opcion == '5':
                print(f"Resultado: {potencia(num1, num2)}")
            elif opcion == '6':
                valor = float(input("Ingrese el valor: "))
                try:
                    print(f"Resultado: {raiz_cuadrada(valor)}")
                except ValueError as e:
                    print(e)
        else:
            print("Opción no válida. Por favor, seleccione una opción entre 1 y 7.")

# Ejecutar la calculadora
calculadora()
