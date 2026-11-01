def eh_primo(n):

    eh_primo = True

    raiz_n = n ** 0.5
    raiz_n = int(raiz_n)
  

    if n < 2:
        eh_primo = False
    
    for numero in range(2, (raiz_n + 1) ):

        if n % numero == 0:

            eh_primo = False


    return eh_primo

primos = []

print("\nNúmeros primos de um intervalo.....\n")

ninicio = int(input("Digite o número inicial do intervalo: ").strip())

nfim = int(input("Digite o número final do intervalo: ").strip())

for numero in range(ninicio, nfim):

    if eh_primo(numero):

        primos.append(numero)

print(f"\nOs numeros primos entre {ninicio} e {nfim} são: {primos}\n")
print(f"Há {len(primos)} numeros primos entre esses dois números")