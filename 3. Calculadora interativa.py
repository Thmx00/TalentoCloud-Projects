"""
Faça uma função calculadora que os números e as operações serão feitas pelo usuário. O código deve ficar 
rodando infinitamente até que o usuário escolha a opção de sair. No início, o programa mostrará a seguinte lista de operações:

1: Soma
2: Subtração
3: Multiplicação
4: Divisão
0: Sair

Digite o número para a operação correspondente e caso o usuário introduza qualquer outro, o sistema deve mostrar
a mensagem “Essa opção não existe” e voltar ao menu de opções.
"""

def calculadora(num1, operacao, num2):
    if(operacao == 1):
        return num1 + num2
    elif(operacao == 2):
        return num1 - num2
    elif(operacao == 3):
        return num1 * num2
    elif(operacao == 4):
        if (num2 == 0):
            return "ERRO: Denomnador não pode ser igual a 0"
        else: 
            return num1/num2
    else:
        return 0
continuar = True
while (continuar == True):
    print("CALCULADORA SIMPLES")
    print("Sinais operacionais dispopníveis")
    print("1: SOMA")
    print("2: SUBTRAÇÃO")
    print("3: MULTIPLICAÇÃO")
    print("4: DIVISÃO")
    print()
    
    print("Digite o sinal operacional: ")
    operacao = int(input())
    if((operacao < 0) or (operacao > 4)):
            print("Essa opção não existe")
    elif(operacao == 0):
            continuar == False
    else:
        print("Digite o primeiro número: ")
        num1 = float(input())
        print("Digite o segundo número: ")
        num2 = float(input())
        print()

        resultado = calculadora(num1, operacao, num2)
        print(f"O resultado é: {resultado}")
