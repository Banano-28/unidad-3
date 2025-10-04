def a_postfija(expresion):
    pila_operadores = []   
    pila_salida = []      

    for caracter in expresion:
        if caracter.isdigit(): 
            pila_salida.append(caracter)

        elif caracter == "(":
            pila_operadores.append(caracter)

        elif caracter == ")": 
            while pila_operadores and pila_operadores[-1] != "(":
                pila_salida.append(pila_operadores.pop())
            pila_operadores.pop() 

        elif caracter in "+-*/": 
        
            while pila_operadores and pila_operadores[-1] != "(" and prioridad(pila_operadores[-1]) >= prioridad(caracter):
                pila_salida.append(pila_operadores.pop())
            pila_operadores.append(caracter)  

    while pila_operadores:
        pila_salida.append(pila_operadores.pop())

    return pila_salida

def a_prefija(expresion):

    expresion_invertida = []
    for caracter in expresion[::-1]:
        if caracter == "(":
            expresion_invertida.append(")")
        elif caracter == ")":
            expresion_invertida.append("(")
        else:
            expresion_invertida.append(caracter)

    postfija = a_postfija(expresion_invertida)

    prefija = postfija[::-1]

    return prefija

def prioridad(op):
    if op in "+-":
        return 1
    if op in "*/":
        return 2
    return 0


print("=== Conversión de Expresiones ===")
print("Ejemplo de entrada (infija):  4+(3*2)")
print("Resultado esperado postfija:  4 3 2 * +")
print("Resultado esperado prefija:   + 4 * 3 2")
print("=================================\n")

expresion = input("Ingrese una expresión aritmética en forma normal (infija): ")

resultado_postfija = a_postfija(expresion)
resultado_prefija = a_prefija(expresion)

print("\n--- Resultados ---")
print("Expresión original (infija):", expresion)
print("Postfija:", " ".join(resultado_postfija))
print("Prefija: ", " ".join(resultado_prefija))
