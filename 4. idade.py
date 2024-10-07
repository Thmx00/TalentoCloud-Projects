"""
Desenvolva um programa que recebe do usuário nome completo e ano de nascimento que seja entre 1922 e 2021.
A partir dessas informações, o sistema mostrará o nome do usuário e a idade que completou, ou completará, 
no ano atual (2022).

Caso o usuário não digite um número ou apareça um inválido no campo do ano, o sistema informará o erro e 
continuará perguntando até que um valor correto seja preenchido.
"""
continuar = True
while(continuar == True):
    print("Qual é o seu nome?")  
    nome = input()
    print()
    print("Qual é o seu ano de nascimento?  (entre 1922 e 2021)")
    try:
        ano = int(input())
        print()
        if ((ano < 1922) or (ano > 2021)):
            print("Por favor informe o ano de nascimento entre 1922 e 2021")
        else:
            continuar = False
            print(nome, " tem ", 2022 - ano, " anos de idade")
    except:
        print("ERRO: valor inválido. Por favor informe o ano de nascimento entre 1922 e 2021")