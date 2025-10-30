import json
from funcionario import Funcionario

class Gerente(Funcionario):
    arquivo = "gerentes.json"
    lista_gerente = []

    def __init__(self, id, nome, cpf, email, telefone, cargo, salario, senha, departamento):
        super().__init__(id, nome, cpf, email, telefone, cargo, salario)
        self.senha = senha
        self.departamento = departamento

    def autenticar(self, senha):
        return self.senha == senha

    @classmethod
    def carregar(cls):
        try:
            with open(cls.arquivo, "r", encoding="utf-8") as arquivo:
                cls.lista_gerente = json.load(arquivo)
        except FileNotFoundError:  #é criado uma lista vazia, se o arquivo não for encontrado
            cls.lista_gerente = []
        return cls.lista_gerente

    @classmethod
    def salvar(cls):
        with open(cls.arquivo, "w", encoding="utf-8") as arquivo:
            json.dump(cls.lista_gerente, arquivo, indent=4, ensure_ascii=False)


    @classmethod
    def cadastrar_gerente(cls, id, nome, cpf, email, telefone, cargo, salario, senha, departamento):
        cls.carregar()
        for gerente in cls.lista_gerente:
            if gerente["ID"] == id:
                return "⚠️ ID de gerente já cadastrado."

        novo_gerente = {
            "ID": id,
            "Nome": nome,
            "CPF": cpf,
            "Email": email,
            "Telefone": telefone,
            "Cargo": cargo,
            "Salario": float(salario),
            "Senha": senha,
            "Departamento": departamento
        }

        cls.lista_gerente.append(novo_gerente)
        cls.salvar()
        return "✅ Gerente cadastrado com sucesso."

    @classmethod
    def alterar_senha(cls, id_gerente, senha_antiga, nova_senha):
        cls.carregar()
        for gerente in cls.lista_gerente:
            if gerente["ID"] == id_gerente:
                if gerente["Senha"] != senha_antiga:
                    return "❌ Senha atual incorreta."
                if nova_senha == senha_antiga:
                    return "⚠️ A nova senha não pode ser igual à antiga."
                
                gerente["Senha"] = nova_senha
                cls.salvar()
                return "🔑 Senha alterada com sucesso!"
        return "⚠️ Gerente não encontrado."
    
    @classmethod
    def aumentar_salario(cls, gerente_id, gerente_senha):
        cls.carregar() #Carrega os dados do arquivo JSON dos funcionários
        Funcionario.carregar() #Carrega os dados do arquivo JSON dos funcionários

        gerente_valido = False
        for gerente in Gerente.lista_gerente:
            if gerente["ID"] == gerente_id and gerente["Senha"] == gerente_senha:
                gerente_valido = True #Marca que o gerente foi encontrado e a senha é válida
                break
        if not gerente_valido:
            return "❌ Apenas gerentes podem aumentar salários."

        id_funcionario = input("Digite o ID do funcionário: ")  #Pergunta qual funcionário terá o aumento

        if not cls.lista_funcionario:  #Verifica se a lista de funcionários está vazia
            return "⚠️ Nenhum funcionário cadastrado."

        percentual = float(input("Digite o percentual de aumento (%): "))

        for func in cls.lista_funcionario: #Procura o funcionário e aumenta o salário
            if func["ID"] == id_funcionario:
                aumento = func["Salario"] * (percentual / 100)
                func["Salario"] += aumento
                Funcionario.salvar() #Salva no novo salário do fun. no arquivo Json de funcionário
                return f"💰 Salário de {func['Nome']} aumentado em {percentual}% (Novo: R${func['Salario']:.2f})"
        return "⚠️ Funcionário não encontrado."


    @classmethod
    def excluir_gerente(cls, id_gerente):
        cls.carregar()
        for gerente in cls.lista_gerente:
            if gerente["ID"] == id_gerente:
                cls.lista_gerente.remove(gerente)
                cls.salvar()
                return "✅ Gerente excluído com sucesso."
        return "⚠️ Gerente não encontrado."