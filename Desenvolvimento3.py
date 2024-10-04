# numero - variavel que armazena o numero a ser impresso para cada andar

#Imprimir numeros de 1 a 20 excepto 13 usando o for
print("Imprimindo andares usando a estrutura de repetição for")
for numero in range(1, 20 +1):
    if(numero == 13):
        continue
    print("andar - ", numero)
print("")
print("")
#Imprimir numeros de 1 a 20 excepto 13 usando while
print("imprimindo os andares usando a estrutura de repetição while")
numero = 21
while (numero > 1):
    numero = numero - 1
    if(numero == 13):
        continue
    print("andar - ", numero)


#Imprimir numeros de 1 a 20 excepto 13 usando o do .. while
"""
numero = 21;
do {
    numero = numero - 1
    if (numero == 13){
        continue
    }
    print ("andar - ", numero);
} while(numero >= 2);
"""