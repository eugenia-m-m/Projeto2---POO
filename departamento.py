from funcionario import Funcionario
from gerente import Gerente
import json 

class Departamento: 
    def __init__(self, setor):
        self.setor = setor

    @classmethod
    def relatorio (cls, departa, gerente_id, gerente_senha):
        gasto = 0
        cls.carregar()

        gerente_valido = False
        for gerente in Gerente.lista_gerente:
            if gerente["ID"] == gerente_id and gerente["Senha"] == gerente_senha:
                gerente_valido = True #Marca que o gerente foi encontrado e a senha é válida
                break
        if not gerente_valido:
            return "❌ Apenas gerentes podem aumentar salários."

        for depart in cls.lista_funcionario:
            if depart["Departamento"] == departa:
                depart["Salário"] += gasto 
                print(gasto)
                cls.salvar()
                return "🔑 Senha alterada com sucesso!"
        return "⚠️ Gerente não encontrado."
    