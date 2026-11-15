def dividir(a,b):

    try:

        resultado = a/b

    except ZeroDivisionError:

       resultado = print("Não é possível dividir por zero")


    except TypeError:
        
        try:

            a = int(a)

        except ValueError:

            a = None

        try:

            b = int(b)

        except ValueError:

            b = None

        if a == None and b == None:

            resultado = print("Os dois valores precisam ser números.")

        else:

            resultado = print("Não é possível dividir um texto por número.")


    return resultado

print(dividir(43284,482384))

print("----------- OPERAÇÃO ENCERRADA ------------")