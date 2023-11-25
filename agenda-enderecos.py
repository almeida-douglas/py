bd = []


def menu():
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
    esc = int(input("Escolha uma opção de 1 a 7: "))
    if esc == 1:
        cadastrar(bd)
    elif esc ==2:
        consultar(bd)
    elif esc == 3:
        excluir(bd)
    elif esc == 4:
        listar(bd)
    elif esc ==5:
        zerar(bd)
    elif esc ==6:
        devs()
    elif esc ==7:
        exit()

def cadastrar(bd):
 
    dados = [[],[],[]]
    dados[0] = input("# Nome:  #  ")
    dados[1] = input("# Endereço:  #  ")
    dados[2] = input("# Telefone:  #  ")

    bd.append(dados)
    print(bd)
    print("# Adicionado com sucesso!\t#")
    esc = int(input("# 1 - Voltar ao início\t\t#"))
    if esc == 1:
        menu()
    else:
        return esc

def consultar(bd):
    print(bd)
    nome = str(input("# Digite o nome a ser consultado: \t \t #"))
    if nome in bd:
        print("# \tNome: ", bd.index(nome)[0], "\t#")
        print("# \tEndereço: ", bd.index(nome)[1], "\t#")
        print("#\t Telefone: ", bd.index(nome)[2], "\t#")
        esc = input("consultar novo nome? (S/N)")
        if esc =='S' or esc =="s":
            return nome
        elif esc =='N' or esc =='N':
           menu()
    else:
        print("não existe")
        esc = input("consultar novo nome? (S/N)")
        if esc =='S' or esc =="s":
            return nome
        elif esc =='N' or esc =='N':
            return menu()
        
def excluir(bd):
    nome = input("Digite o nome a ser excluído:")
    if bd.index(nome) == True:
        esc = input("Tem certeza? (S/N)")
        if esc == 'S' or esc =='s':
           bd.remove(bd.index(nome))
           print("# \tRemovido! \t#")
        elif esc == 'N' or esc =='n':
            return menu()

def listar(bd):
    for i in range (0, bd.len):
        print("# ", bd[i].index, "- ", bd[i][0])










menu()