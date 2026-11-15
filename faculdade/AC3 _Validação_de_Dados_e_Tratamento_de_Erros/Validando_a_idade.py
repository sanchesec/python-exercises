while True:

    idade = input("\nInsira sua idade: ").strip()

    if not idade.isdigit():

        print("\n Valor invalido: digite apenas numeros inteiros positivos")
        continue

    idade = int(idade)

    if idade > 120 or idade < 1:

        print("\nIdade fora da faixa (1 a 120)")    
        continue

    print("Idade registrada com sucesso!")
    break