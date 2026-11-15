def para_inteiro(texto):

    try:

        texto = int(texto)

    except ValueError:

        
        mensagem,texto = print(f"{texto} não é um número inteiro\n"), None

    return texto

lista = ["10", "abc", "7", "", "3.5", "-4"]
soma = 0

for texto in lista:

    if para_inteiro(texto) != None:
        soma += para_inteiro(texto)

print(f"Soma dos valores válidos: {soma}")



