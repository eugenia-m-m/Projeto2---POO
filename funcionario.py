import json

class Funcionario:
    arquivo = "funcionario.json"
    lista_funcionario = []

    def __init__(self, nome, cpf, email, telefone, cargo, salario):
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.telefone = telefone
        self.cargo = cargo
        self.salario = salario

    @classmethod
    def carregar(cls): 
        with open(cls.arquivo, "r", encoding="UTF-8") as arquivo:
            dado = json.load(arquivo)
            return dado
        return False

    @classmethod
    def salvar(cls, dados): 
        with open(cls.arquivo, "w", encoding="UTF-8") as arquivo:
            json.dump(dados, arquivo, indent=4, ensure_ascii=False)
            return True
        return False
    

    @classmethod
    def cadastrar_funcionario(cls, id, nome, cpf, email, telefone, cargo, salario):
        for funcio in cls.lista_funcionario:
            if funcio["ID"] == id:
                return "⚠️ ID do funcionário já cadastrado."
        
        funcio = {
            "ID": id, 
            "Nome": nome, 
            "CPF": cpf,
            "Email": email,
            "Telefone": telefone,
            "Cargo": cargo,
            "Salario": salario
        }
        cls.list_funcionario.append(funcio)
        cls.salvar(cls.list_funcionario)
        return "✅ Funcionário cadastrado com sucesso."
    
    @classmethod
    def editar_funcionario(cls, id_funcionario, novo_nome):
        for funcio in cls.list_funcionario:
            if funcio["ID"] == id_funcionario:  
                funcio["Nome"] = novo_nome  
                cls.salvar(cls.lista_funcionario)
                return "✅ Funcionário atualizado com sucesso."
        return "⚠️ Funcionário não encontrado."

   

