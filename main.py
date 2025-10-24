from funcionario import Funcionario
from gerente import Gerente


def menu():
    while True:
        print(""" 
        ------------- MENU -------------
            
            1 - CADASTRAR FUNCIONÁRIO 📃
            2 - CADASTRAR GERENTE 📃
            3 - LISTAR FUNCIONÁRIOS ✍
            4 - PESQUISAR FUNCIONÁRIO 🔍
            5 - ALTERAR SALÁRIO DE FUNCIONÁRIO 💰
            6 - ALTERAR SENHA DE GERENTE 💰
            7 - EDITAR DADOS DE FUNCIONÁRIO 📝
            8 - EDITAR DADOS DE GERENTE 📝
            9 - REMOVER FUNCIONÁRIO 📌
            10 - REMOVER GERENTE 📌
            0 - SAIR ❌
    """)
        
        op = input()
        if op == '1':
            nome = input('Informe o seu nome completo: ').title()
            cpf = input('Informe seu CPF: ')
            rg = input('Informe seu RG: ')
            id = input('Informe seu ID:')
            data_nasc = input('Informe seu data de nascimento: ')
            salario = input('Informe seu salário: ')
            novo_funcionario = Funcionario(nome, cpf, rg, id, data_nasc, salario)
            Funcionario.cadastro_funcionario.append(novo_funcionario)
            print('Funcionário cadastrado com sucesso! Seja Bem vindo!')

    
        elif op == '2':
            nome = input('Informe o seu nome completo: ').title()
            cpf = input('Informe seu CPF: ')
            rg = input('Informe seu RG: ')
            id = input('Informe seu ID: ')
            data_nasc = input('Informe seu data de nascimento: ')
            salario = input('Informe seu salário: ')
            novo_gerente = Gerente(nome, cpf, rg, id, data_nasc, salario)
            Gerente.cadastro_gerente.append(novo_gerente)

        elif op == '3':
            print(Funcionario.cadastro_funcionario)

        elif op == '4':
            pass

        elif op == '5':
            percentual = float(input('Digite o percentual de aumento do funcionário: '))
            print("")

        elif op == '6':
            pass

        elif op == '7':
            pass

        elif op == '8': 
            pass

        elif op == '9':
            pass

        elif op == '10':
            pass                                                                                   

        elif op == '11':                                                                            
            pass        

        elif op == '0':
            print('Sair')
            break

        else:
            print('Opção inválida. Tente novamente!')



if __name__ == "__main__":
    menu()