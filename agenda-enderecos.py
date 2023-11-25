bd = {}

def adicionar(nome, telefone, endereco):
    bd[nome] = {'Telefone': telefone, 'Endereco': endereco}
    print(f'{nome} adicionado com sucesso!')


def consultar(nome):
    if nome in bd:
        contato = bd[nome]
        print(f'Nome: {nome}\nTelefone: {contato["Telefone"]}\nEndereco: {contato["Endereco"]}')
    else:
        print(f'{nome} não encontrado.')


def deletar():
    menu()

def listar():
    print('Lista de Contatos:')
    for nome, contato in bd.items():
        print(f'Nome: {nome}\nTelefone: {contato["Telefone"]}\nEndereco: {contato["Endereco"]}\n---')


def zerar():
    menu()

def desenvolvedores():
        print("#-------------------------------------------------------#")
        print("#\t\t      Desenvolvedores\t\t\t#")
        print("#-------------------------------------------------------#")
        print("# Diogo de Almeida da Silva - 202310745 \t \t#")
        print("# Douglas De Almeida da Silva - 202310744 \t \t#")
        print("# Roberto Júnior de Carvalho Botelho - 202311417\t#")
        repetir =  input("Repetir? S/N ")
        if repetir == 's' or repetir == 'S':
            desenvolvedores()


def menu():
    while True:
        print("#-------------------------------#")
        print("#\t Agenda de endereços\t#")
        print("#-------------------------------#")
        print("#  opções \t\t\t#")
        print("# 1 - CADASTRAR NOME \t \t#")
        print("# 2 - CONSULTAR NOME \t \t#")
        print("# 3 - EXCLUIR NOME\t \t#")
        print("# 4 - LISTAR NOMES\t \t#")
        print("# 5 - ZERAR A AGENDA\t \t#")
        print("# 6 - DESENVOLVEDORES\t \t#")
        print("# 7 - SAIR\t\t\t#")
        print("#-------------------------------#")
        escolha = input("Escolha uma opção de 1 a 7: ")

        if escolha == '1':
            nome = input("Digite o nome: ")
            telefone = input("Digite o número: ")
            endereco = input("Digite o endereço: ")
            adicionar(nome, telefone, endereco)

        elif escolha == '2':
            nome = input("Digite o nome do contato a ser buscado: ")
            consultar(nome)
        
        elif escolha == '3':
            deletar()

        elif escolha == '4':
            listar()

        elif escolha == '5':
            zerar()

        elif escolha == '6':
            desenvolvedores()

        elif escolha == '7':
            print("Encerrando!")
            break

        else:
            print("Opção inválida. Tente novamente.")
menu()