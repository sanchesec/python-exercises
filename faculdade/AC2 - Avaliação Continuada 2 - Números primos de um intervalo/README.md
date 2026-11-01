# AC2 — Números Primos em um Intervalo

Atividade da **Avaliação Continuada 2 (AC2)** de programação em Python.

## Objetivo

Desenvolver um programa que receba o início e o fim de um intervalo e apresente os **números primos** encontrados, incluindo os limites informados quando forem primos.

Um número primo é um número inteiro maior que 1 que possui exatamente dois divisores positivos: **1 e ele mesmo**.

## Arquivos

- **`numeros_primos.py`** — código do exercício.
- **Arquivos `.txt`** — registro do meu raciocínio durante o exercício e uma versão explicativa elaborada com auxílio de IA.

## Como executar

Com Python 3 instalado, abra o terminal nesta pasta e execute:

```bash
python3 numeros_primos.py
```

### Exemplo esperado

Para o intervalo de **1 a 20**, os números primos são:

```text
2, 3, 5, 7, 11, 13, 17, 19
```

## Raciocínio e aprendizado

Uma forma de verificar se um número é primo é testar divisões por todos os inteiros entre `2` e `n - 1`. Porém, é possível reduzir essas verificações até a **raiz quadrada de `n`**.

Isso funciona porque, se `n` for composto, poderá ser escrito como a multiplicação de dois fatores. Pelo menos um desses fatores será menor ou igual à raiz quadrada de `n`. Assim, se nenhum inteiro de `2` até essa raiz dividir `n` sem deixar resto, `n` é primo (desde que `n > 1`).

O exercício trabalha conceitos como **funções, laços de repetição, condicionais, intervalos e o operador módulo (`%`)**.

## Autor

Gustavo Soares Sanches
