notas = [8.5, 7.0, 9.5]
aluno = {"nome": "Ana", "curso": "ADS"}

nota = int(input("Posição da nota: ").strip())
campo_aluno = input("Campo do aluno: ").strip().lower()

try:

    resultado1 = print(notas[nota])

except IndexError:

    resulado1 = print(f"Não existe nota na posição {nota}")

try:

    resultado2 = print(aluno[f"{campo_aluno}"])

except KeyError:

    resultado2 = print(f"O campo {campo_aluno} não existe no cadastro.")