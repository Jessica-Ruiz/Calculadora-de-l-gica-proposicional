import pandas as pd

# Definición de funciones lógicas
def negacion(p):
    # Devuelve la negación de un valor booleano (¬p)
    print(f"Negación de {p}: {not p}")
    return not p

def conjuncion(p, q):
    # Devuelve la conjunción lógica (p ∧ q), es verdadera solo si ambas son verdaderas
    resultado = p and q
    print(f"Conjunción de {p} y {q}: {resultado}")
    return resultado

def disyuncion(p, q):
    # Devuelve la disyunción lógica (p ∨ q), es verdadera si al menos una es verdadera
    resultado = p or q
    print(f"Disyunción de {p} y {q}: {resultado}")
    return resultado

def bicondicional(p, q):
    # Devuelve la bicondicional lógica (p ↔ q), es verdadera si ambas son iguales
    resultado = p == q
    print(f"Bicondicional de {p} y {q}: {resultado}")
    return resultado

def condicional(p, q):
    # Devuelve el condicional lógico (p → q), falso solo si p es verdadero y q es falso
    resultado = not p or q
    print(f"Condicional de {p} a {q}: {resultado}")
    return resultado

# Función para evaluar expresiones lógicas ingresadas por el usuario
def evaluar_expresion(expresion, valores):
    # Reemplaza las variables en la expresión con sus valores actuales (True/False)
    for var, val in valores.items():
        expresion = expresion.replace(var, str(val))

    # Sustituye los símbolos lógicos por operadores de Python
    expresion = expresion.replace('¬', 'not ')
    expresion = expresion.replace('∧', ' and ')
    expresion = expresion.replace('∨', ' or ')
    expresion = expresion.replace('→', ' <= ')  # p → q equivale a ¬p ∨ q
    expresion = expresion.replace('↔', ' == ')  # p ↔ q equivale a p == q

    # Intenta evaluar la expresión lógica final
    print(f"\nEvaluando la expresión: {expresion}")
    try:
        resultado = eval(expresion)
        print(f"Resultado de la expresión: {resultado}")
        return resultado
    except Exception as e:
        # Muestra un mensaje de error si la expresión no es válida
        return f"Error al evaluar la expresión: {e}"

# Función para generar la tabla de verdad de una expresión lógica dada
def generar_tabla_verdad(expresion):
    # Encuentra las variables en la expresión (letras mayúsculas)
    variables = sorted(set([c for c in expresion if c.isupper()]))
    n = len(variables)

    # Genera todas las combinaciones posibles de valores para las variables
    resultados = []

    for i in range(2 ** n):
        valores = {}
        for j in range(n):
            # Asigna valores booleanos en función de los bits del número actual
            valores[variables[j]] = bool((i >> (n - 1 - j)) & 1)

        # Evalúa la expresión lógica con los valores actuales
        print(f"\nValores actuales: {valores}")
        resultado = evaluar_expresion(expresion, valores)

        # Guarda la combinación de valores y el resultado en la tabla
        fila = [int(valores[var]) for var in variables] + [int(resultado)]
        resultados.append(fila)

    # Crea un DataFrame para mostrar la tabla de verdad de manera ordenada
    df = pd.DataFrame(resultados, columns=variables + ["Resultado"])
    return df

# Función principal que gestiona el menú y la interacción con el usuario
def main():
    while True:
        print("\nMenú de Opciones:")
        print("1. Ingresar una nueva expresión lógica")
        print("2. Salir")

        opcion = input("Seleccione una opción (1 o 2): ")

        if opcion == '1':
            # Solicita la expresión lógica al usuario y genera su tabla de verdad
            expresion = input("Ingrese la expresión lógica (use P, Q, R, S como variables): ")
            tabla_verdad = generar_tabla_verdad(expresion)
            print("\nTabla de Verdad:")
            print(tabla_verdad)
        elif opcion == '2':
            # Sale del programa
            print("Saliendo del programa...")
            break
        else:
            # Muestra un mensaje de error si la opción no es válida
            print("Opción no válida. Por favor, seleccione 1 o 2.")

# Punto de entrada del programa
if _name_ == "_main_":
    main()
