import pandas as pd

# Negación
def negacion(p):
    return not p

# Conjunción
def conjuncion(p, q):
    return p and q

# Disyunción
def disyuncion(p, q):
    return p or q

# Bicondicional
def bicondicional(p, q):
    return p == q

# Condicional
def condicional(p, q):
    return not p or q

class PropositionalLogicCalculator:
    def truth_table(self, expression):
        
        variables = sorted(set(filter(str.isalpha, expression)))

        
        results = pd.DataFrame(columns=variables + ['Resultado'])

        
        num_vars = len(variables)
        for i in range(2 ** num_vars):
            
            combination = [(i >> j) & 1 for j in range(num_vars)]
            values = dict(zip(variables, [bool(1 - val) for val in combination]))  

            
            result = eval(expression.replace('and', 'conjuncion').replace('or', 'disyuncion').replace('not', 'negacion').replace('implies', 'condicional'), {}, values)
            results = results.append({**values, 'Resultado': 0 if result else 1}, ignore_index=True)

        return results

def main():
    calculator = PropositionalLogicCalculator()

    while True:
        expression = input("Ingrese la expresión lógica (o 'salir' para terminar): ")
        if expression.lower() == 'salir':
            print("Saliendo...")
            break

        
        df = calculator.truth_table(expression)
        print("\nTabla de verdad:")
        print(df.replace({True: 0, False: 1})) 

if __name__ == "__main__":
    main()
