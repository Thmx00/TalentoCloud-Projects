"""
    Faça uma função calculadora de dois números com três parâmetros: os dois primeiros serão os números da operação e o terceiro será a entrada que definirá a operação a ser executada. Considera a seguinte definição:
1. Soma
2. Subtração
3. Multiplicação
4. Divisão

Caso seja inserido um número de operação que não exista, o resultado deverá ser 0.
"""

def calculadora (num1, operacao, num2):
    if (operacao == 1):
        return num1 + num2
    elif(operacao == 2):
        return num1 - num2
    elif(operacao == 3):
        return num1 * num2
    elif(operacao == 4):
        return num1 / num2
    else:
        return "0"
    
print("CALCULADORA SIMPLES")
print("Sinais de Operação disponíveis")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

num1 = 18
num2 = 2
operacao = 3
 
resultado = calculadora(num1, operacao, num2)
print("")
print(f"O resultado é {resultado}")