from funcionario import Funcionario
import json

class Gerente(Funcionario):
    arquivo = "gerente.json"
    cadastro_gerente = []
    
    def __init__(self, nome, cargo, salario, senha, departamento):
        super().__init__(nome, cargo, salario)
        self.senha = senha
        self.departamento = departamento

    def autenticar(self, senha):
        return self.senha == senha

    def exibir_dados(self):
        super().exibir_dados()
        print(f"Departamento: {self.departamento}")

    def exibir_dados_gerente(self):
        super().exibir_dados_gerente()
        print(f"Departamento: {self.departamento}")

    def exibir_dados_funcionario_gerente(self):
        super().exibir_dados_funcionario_gerente()
        print(f"Departamento: {self.departamento}")

    def exibir_dados_gerente_gerente(self):
        super().exibir_dados_gerente_gerente()
        print(f"Departamento: {self.departamento}")