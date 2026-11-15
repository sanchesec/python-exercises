clientes = [
    {"id": 1 , "nome": "Ana Souza", "email": "ana@fecaf.com.br"},
    {"id": 2, "nome": "",             "email": "bruno@fecaf.com.br"},
    {"id": 3, "nome": "Carla Dias",   "email": "carla.fecaf.com.br"},
    {"id": "x", "nome": "Diego Lima", "email": "diego@fecaf.com.br"},
    {"id": 5,                         "email": "erica@fecaf.com.br"},
    {"id": 6, "nome": "Felipe Rocha", "email": ""},
]

validos = []
invalidos = []

for cliente in clientes:


    try:

        if isinstance(cliente["id"], int) != True:

            invalidos.append({"id": cliente["id"],"motivo": "id não é um número inteiro"})

            continue

    except KeyError:

        invalidos.append({"id": None, "motivo": "Campo ausente: 'id' "})

        continue


    try:
    
        if cliente["nome"].strip() == "":

            invalidos.append({"id": cliente["id"],"motivo": "nome vazio"})

            continue

    except KeyError:

        invalidos.append({"id": cliente["id"],"motivo": "Campo ausente: 'nome' "})

        continue


    try:

        if cliente["email"].strip() == "":

            invalidos.append({"id": cliente["id"],"motivo": "e-mail vazio "})

            continue

        elif len(cliente["email"].split("@")) != 2:

            invalidos.append({"id": cliente["id"],"motivo": "e-mail inválido: Falta o sinal '@' "})

            continue
            
        elif len((cliente["email"].split("@")[1]).split(".")) != 3:

            invalidos.append({"id": cliente["id"],"motivo": "e-mail inválido: Falta o sinal '.' "})

            continue


    except KeyError:

        invalidos.append({"id": cliente["id"],"motivo":"Campo ausente: 'e-mail'"})
        
        continue

    
    validos.append({"id": cliente["id"], "nome": cliente["nome"], "email": cliente["email"] })




print(f"\nClientes válidos ({len(validos)})\n")

for cliente in validos:

    print(cliente)


print(f"\nClientes inválidos ({len(invalidos)})\n")

for cliente in invalidos:

    print(cliente)