from funcionario import Funcionario
from gerente import Gerente
import json 

class Departamento: 
    arquivo = "Departamento.json"
    lista_depart = []

    @classmethod 
    def carregar(cls): 
        try: 
            with open(cls.arquivo, "r", encoding="utf-8") as arquivo: 
                cls.lista_depart = json.load(arquivo)
        except FileNotFoundError: cls.lista_depart = ['a', 'b'] 
        return cls.lista_depart 
    
    @classmethod
    def relatorio(cls, departa):
        cls.carregar()
        funcionarios = Funcionario.carregar()
        gerentes = Gerente.carregar()

        existe = False
        for d in cls.lista_depart:
            if d.upper() == departa:
                existe = True
                break

        if not existe:
            print(f"⚠️ O departamento '{departa}' não existe.")
            return

        gerente_dep = "Não há gerente cadastrado"
        for g in gerentes:
            if g["Departamento"].upper() == departa:
                gerente_dep = g["Nome"]
                break

        funcionarios_depart = []
        gasto_total = 0

        for f in funcionarios:
            if f["Departamento"].upper() == departa:
                funcionarios_depart.append(f)
                gasto_total += f["Salario"]

        print("\n------ RELATÓRIO DE GASTOS ------") # saida do código 
        print("Departamento:", departa)
        print("Gerente:", gerente_dep)
        print("---------------------------------")
        print("Funcionários:")

        if len(funcionarios_depart) == 0:
            print("Nenhum funcionário neste departamento.")
        else:
            for f in funcionarios_depart:
                print(f"{f['Nome']} - R${f['Salario']}")
            print("---------------------------------")
            print(f"💵 Total gasto com salários: R${gasto_total}")
