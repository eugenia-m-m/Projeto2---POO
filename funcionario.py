import json

class Funcionario:
    arquivo = "funcionarios.json"
    lista_funcionario = []

    def __init__(self, id, nome, cpf, email, telefone, cargo, departamento, salario):
        self.id = id
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.telefone = telefone
        self.cargo = cargo
        self.departamento = departamento
        self.salario = float(salario)


    @classmethod
    def carregar(cls):
        try:
            with open(cls.arquivo, "r", encoding="utf-8") as arquivo:
                cls.lista_funcionario = json.load(arquivo)
        except FileNotFoundError:
            cls.lista_funcionario = []
        return cls.lista_funcionario

    @classmethod
    def salvar(cls):
        with open(cls.arquivo, "w", encoding="utf-8") as arquivo:
            json.dump(cls.lista_funcionario, arquivo, indent=4, ensure_ascii=False)


    @classmethod
    def cadastrar_funcionario(cls, id, nome, cpf, email, telefone, cargo, departamento, salario):
        cls.carregar()
        for func in cls.lista_funcionario:
            if func["ID"] == id:
                return "⚠️ ID do funcionário já cadastrado."

        novo_func = {
            "ID": id,
            "Nome": nome,
            "CPF": cpf,
            "Email": email,
            "Telefone": telefone,
            "Cargo": cargo,
            "Departamento": departamento,
            "Salario": float(salario)
        }

        cls.lista_funcionario.append(novo_func)
        cls.salvar()
        return "✅ Funcionário cadastrado com sucesso."
    
    @classmethod
    def listar_funcionario(cls):
        cls.carregar()  # Carrega a lista de funcionários do arquivo JSON
        if not cls.lista_funcionario:  # Verifica se a lista está vazia
            print("Nenhum funcionário cadastrado.")
            return []

        print("\n------ Funcionários Cadastrados -----\n")
        for f in cls.lista_funcionario:  # Percorre cada funcionário (dicionário)
            print(f"{f['ID']} - {f['Nome']} ({f['Cargo']}) - R${f['Salario']:.2f}")
        
        return cls.lista_funcionario

    @classmethod
    def editar_funcionario(cls, id_funcionario, novo_nome, novo_cpf, novo_email, novo_telefone, novo_cargo, novo_salario):
        cls.carregar()
        for func in cls.lista_funcionario:
            if func["ID"] == id_funcionario:
                func["Nome"] = novo_nome
                func["CPF"] = novo_cpf
                func["Email"] = novo_email
                func["Telefone"] = novo_telefone
                func["Cargo"] = novo_cargo
                func["Salario"] = float(novo_salario)
                cls.salvar()
                return "✅ Funcionário atualizado com sucesso."
        return "⚠️ Funcionário não encontrado."
    
    @classmethod
    def excluir_funcionario(cls, id_funcionario):
        cls.carregar()
        for func in cls.lista_funcionario:
            if func["ID"] == id_funcionario:
                cls.lista_funcionario.remove(func)
                cls.salvar()
                return "✅ Funcionário excluído com sucesso."
        return "⚠️ Funcionário não encontrado."

    @classmethod
    def pesquisar_funcionario(cls, termo):
        cls.carregar()
        resultados = []
        termo = termo.lower()

        for func in cls.lista_funcionario:
            if (termo in func["ID"] or termo in func["Nome"].lower() or termo in func["CPF"]):
                resultados.append(func)

        if not resultados:
            return "⚠️ Nenhum funcionário encontrado."

        texto = "\n------ RESULTADOS DA PESQUISA ------\n"
        for f in resultados:
            texto += (
                f"ID: {f['ID']}\n"
                f"Nome: {f['Nome']}\n"
                f"CPF: {f['CPF']}\n"
                f"Email: {f['Email']}\n"
                f"Telefone: {f['Telefone']}\n"
                f"Cargo: {f['Cargo']}\n"
                f"Salário: R${f['Salario']:.2f}\n"
                f"{'-'*30}\n"
            )
        return texto


    def aumentar_salario():
        print('Oi')