
from usuario import Usuario
from db_manager import DBManager


def main():
    opcao = input("Para cadastrar um usuário na Agenda aperte 1;\n"
                  "Para pesquisar um usuário da Agenda aperte 2;\n"
                  "Para atualizar um usuário da Agenda aperte 3;\n"
                  "Para remover um usuário da Agenda aperte 4.\n")
    manager = DBManager()

    if int(opcao) == 1:
        nome = input("Insira o nome: ")
        telefone = input("Insira o telefone: ")
        email = input("Insira o email: ")
        blog = input("Insira o blog: ")
        novo_usuario = Usuario(nome=nome,
                               telefone=telefone,
                               email=email,
                               blog=blog)

        manager.cadastra_usuario(novo_usuario)

    elif int(opcao) == 2:
        busca = input("Digite o e-mail que irá identificar o usuário que quer encontrar dentro da Agenda: ")
        manager.busca_usuario(busca)

    elif int(opcao) == 3:
        busca = input("Digite o e-mail que irá identificar o usuário que quer encontrar dentro da Agenda: ")
        usuario_encontrado = manager.existe_usuario(busca)
        if usuario_encontrado:
            novo_email = input("Digite o novo e-mail para esse usuário: ")
            novo_nome = input("Digite o novo nome para esse usuário: ")
            novo_telefone = input("Digite o novo telefone para esse usuário: ")
            novo_blog = input("Digite o novo blog para esse usuário: ")
            dados = dict()
            dados['email'] = novo_email
            dados['nome'] = novo_nome
            dados['telefone'] = novo_telefone
            dados['blog'] = novo_blog
            manager.atualiza_usuario(busca, dados=dados)
        else:
            print("Usuário não existe na Agenda.")

    elif int(opcao) == 4:
        busca = input("Digite o e-mail que irá identificar o usuário que quer remover da Agenda: ")
        manager.remove_usuario(busca)
    else:
        print("Opção inválida!")


main()
