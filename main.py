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
            pass
    
        elif op == '2':
            pass

        elif op == '3':
            pass

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