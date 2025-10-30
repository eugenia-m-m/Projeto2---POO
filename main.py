from funcionario import Funcionario
from gerente import Gerente

def menu():
    while True:
        print("""
        ------------- MENU -------------
        1 - Cadastrar Funcionário 📃
        2 - Cadastrar Gerente 📃
        3 - Listar Funcionários ✍
        4 - Pesquisar Funcionário 🔍
        5 - Editar Funcionário 📝
        6 - Excluir Funcionário 📌
        7 - Excluir Gerente 📌
        8 - Aumentar Salário 💰
        9 - Alterar Senha de Gerente 🔐
        0 - Sair ❌
        """)

        op = int(input("Escolha uma opção: "))

        if op == 1:
            id = input("ID: ")
            nome = input("Nome completo: ").title()
            cpf = input("CPF: ")
            email = input("Email: ")
            telefone = input("Telefone: ")
            cargo = input("Cargo: ")
            salario = float(input("Salário: "))

            msg = Funcionario.cadastrar_funcionario(id, nome, cpf, email, telefone, cargo, salario)
            print(msg)

        elif op == 2:
            id = input("ID: ")
            nome = input("Nome completo: ").title()
            cpf = input("CPF: ")
            email = input("Email: ")
            telefone = input("Telefone: ")
            cargo = input("Cargo: ")
            salario = float(input("Salário: "))
            senha = input("Senha: ")
            departamento = input("Departamento: ")

            msg = Gerente.cadastrar_gerente(id, nome, cpf, email, telefone, cargo, salario, senha, departamento)
            print(msg)

        elif op == 3:
            Funcionario.listar_funcionario()


        elif op == 4:
            termo = input("Digite o nome, CPF ou ID do funcionário: ")
            print(Funcionario.pesquisar_funcionario(termo))

        elif op == 5:
            id = input("ID do funcionário: ")
            novo_nome = input("Novo nome: ")
            novo_cpf = input("Novo CPF: ")
            novo_email = input("Novo email: ")
            novo_telefone = input("Novo telefone: ")
            novo_cargo = input("Novo cargo: ")
            novo_salario = float(input("Novo salário: "))
            print(Funcionario.editar_funcionario(id, novo_nome, novo_cpf, novo_email, novo_telefone, novo_cargo, novo_salario))

        elif op == 6:
            id = input("ID do funcionário: ")
            print(Funcionario.excluir_funcionario(id))

        elif op == 7:
            id = input("ID do gerente: ")
            print(Gerente.excluir_gerente(id))

        elif op == 8:
            gerente_id = input("Digite seu ID de gerente: ")
            gerente_senha = input("Digite sua senha: ")
            print(Gerente.aumentar_salario(gerente_id, gerente_senha))


        elif op == 9:
            id = input("ID do gerente: ")
            senha_atual = input("Senha atual: ")
            nova_senha = input("Nova senha: ")
            print(Gerente.alterar_senha(id, senha_atual, nova_senha))

        elif op == 0:
            print("Volte sempre! 🤝")
            break

        else:
            print("❌ Opção inválida. Tente novamente!")


if __name__ == "__main__":
    menu()
