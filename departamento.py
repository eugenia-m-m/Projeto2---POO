from funcionario import Funcionario
from gerente import Gerente
import json 

class Departamento: 
    arquivo = "Departamento.json"
    lista_depart = ['a', 'b']

    @classmethod
    def carregar(cls):
        try:
            with open(cls.arquivo, "r", encoding="utf-8") as arquivo:
                cls.lista_depart = json.load(arquivo)
        except FileNotFoundError:
            cls.lista_depart = ['a', 'b']
        return cls.lista_depart

    @classmethod
    def salvar(cls):
        with open(cls.arquivo, "w", encoding="utf-8") as arquivo:
            json.dump(cls.lista_depart, arquivo, indent=4, ensure_ascii=False)

    @classmethod
    def relatorio (cls, departa, gerente_id, gerente_senha):
        gasto = 0
        cls.carregar()

        

        for depart in cls.lista_depart:
            if depart[0] == departa:
                for func in cls.carregar():   
                    func["Salário"] += gasto
                    print(gasto)
                    cls.salvar()
                
                
                
                return "🔑 Senha alterada com sucesso!"
        return "⚠️ Gerente não encontrado."
    