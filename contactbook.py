#!/usr/bin/env/ python3
"""Agenda para adicionar, visualizar, editar, favoritar e deletar contatos.

- A aplicação deve iniciar mostrando uma lista de opções do que é possível fazer 
com o app e permitir que o usuário digite uma escolha para iniciar a aplicação.
- Deve ser possível adicionar um contato
    - O contato pode ter os dados:
        - Nome
        - Telefone
        - Email
        - Favorito (está opção é para poder marcar um contato como favorito)
"""
__version__ = "0.1.0"
__author__ = "Bruno Rocha"

def adicionar_contato(contatos, nome_contatos, numero_telefone, email):
    contato = {
        "nome": nome_contatos,
        "numero": numero_telefone,
        "email": email, 
        "favoritar": False
    }
    contatos.append(contato)
    print(f"Contato '{nome_contatos}' adicionado com sucesso!")
    print()
    return

def visualizar_contato(contatos):
    print("{:#^30}".format(" LISTA DE CONTATOS "))
    for indice, contato in enumerate(contatos, start=1):
        status = "★" if contato["favoritar"] else " "
        nome_contatos = contato["nome"]
        print(f"{indice}. [{status}] {nome_contatos}")
    print("-" * 30)
    return

def editar_contato(contatos, indice_contato, novo_nome_contato):
    indice_contato_ajustado = int(indice_contato) - 1
    if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
        contatos[indice_contato_ajustado]["nome"] = novo_nome_contato
        print(f"O contato '{indice_contato}' foi atualizado para '{novo_nome_contato}'")
        print("-" * 30)
        visualizar_contato(contatos)
        print("-" * 30)
    else:
        print("Opção inválida!")
    print()    
    return

def marcar_favorito(contatos, indice_contato):
    indice_contato_ajustado = int(indice_contato) - 1
    contatos[indice_contato_ajustado]["favoritar"] = True
    print(f"O contato {indice_contato} marcada como favorito !")
    print("-" * 30)
    visualizar_contato(contatos)
    print("-" * 30)
    return

def ver_favoritos(contatos):
    print("{:*^30}".format(" LISTA DE FAVORITOS "))
    favoritos_encontrados = False
    for indice, contato in enumerate(contatos, start=1):
        if contato["favoritar"]:
            nome_contato = contato["nome"]
            telefone_contato = contato["numero"]
            email_contato = contato["email"]
            print(f"\nContato {indice} \nNome: {nome_contato} \nTelefone: {telefone_contato} \nEmail: {email_contato}")
            favoritos_encontrados = True
    if not favoritos_encontrados:
        print("Nenhum favorito encontrado!")
    print("-" * 30)
    return

def apagar_contato(contatos, indice_contato):
        visualizar_contato(contatos)
        print("Digite a opção que deseja remover: ")
        if indice_contato.isdigit() and 0 < int(indice_contato) <= len(contatos):
            indice_contato_ajustado = int(indice_contato) - 1
            contato_removido = contatos.pop(indice_contato_ajustado)
            print("Contato removido com sucesso!")
            print("-" * 30)
            print(f"Nome: {contato_removido['nome']}")
            print(f"Telefone: {contato_removido['numero']}")
            print(f"E-mail: {contato_removido['email']}")
            print("-" * 30)
            visualizar_contato(contatos)
            print()
        else:
            print("Índice de contato inválido")
        print()
        return

contatos = []

while True:
    print("{:-^30}".format("AGENDA DE CONTATOS"))
    print("1 -> Adicionar")
    print("2 -> Visualizar")
    print("3 -> Editar")
    print("4 -> Marcar como favorito")
    print("5 -> Ver os favoritos")
    print("6 -> Apagar contato")
    print("7 -> Sair")
    print()

    usuario = input("Digite a opção que deseja: ")

    if usuario == "1":
        nome_contatos = input("Digite o nome: ")
        numero_telefone = input("Digite o número de telefone: ")
        email = input("Digite o E-mail: ")
        adicionar_contato(contatos, nome_contatos, numero_telefone, email)
    elif usuario == "2":
        visualizar_contato(contatos)
    elif usuario == "3":
        visualizar_contato(contatos)
        indice_contato = input("Digite a opção que deseja editar: ")
        novo_nome_contato = input("Digite o novo nome do contato: ")
        editar_contato(contatos, indice_contato, novo_nome_contato)
    elif usuario == "4":
        visualizar_contato(contatos)
        indice_contato = input("Digite opção que deseja marcar como favorito: ")
        marcar_favorito(contatos, indice_contato)
    elif usuario == "5":
        ver_favoritos(contatos)
    elif usuario == "6":
        visualizar_contato(contatos)
        indice_contato_a_remover = input("Digite a opção que deseja remover: ")
        apagar_contato(contatos, indice_contato_a_remover)
    elif usuario == "7":
        break
    else:
        print("Opção inválida !")
        print()