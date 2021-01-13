from datetime import datetime

# classe do Menu
class Menu:

    # dicionário de tabelas do banco de dados
    menus = {
        1: "condominios", 
        2: "funcionarios", 
        3: "propriedades", 
        4: "proprietarios",
        5: "visitantes",
        6: "esfuncionarios",
        7: "espessoas"
    }

    # dicionário de campos do banco de dado
    fields = {
        "condominios": [
                ["Razão Social", 
                "Nome Fantasia"],

                ["STRING",
                "STRING"]
            ],

        "funcionarios": [
                ["Nome", 
                "CPF", 
                "Endereço", 
                "Salário", 
                "Função", 
				"Acesso",
                "ID do Condominio"],

                ["STRING",
                "INT",
                "STRING",
                "FLOAT",
                "STRING",
				"STRING",
                "INT"]
            ],

        "propriedades": [
                ["Código Interno",
                "ID do Condomínio",
				"ID do Proprietário"],

                ["STRING",
                 "INT",
				 "INT"]
            ],

        "proprietarios": [
                ["Nome",
                "Acesso",
                "CPF ou CNPJ"],

                ["STRING",
                 "STRING",
                 "STRING"]
            ],
            
        "visitantes": [
                ["Nome",
                "CPF",
                "Motivo",
                "ID da Propriedade"],

                ["STRING",
                 "INT",
                 "STRING",
                 "INT"]
            ],

        "esfuncionarios": [
                ["Entrada ou Saída [E ou S]",
                "Horário [AAAA-MM-DD hh:mm:ss]",
                "Motivo",
                "ID"],

                ["STRING",
                 "DATETIME",
                 "STRING",
                 "INT"]
            ],

        "espessoas": [
                ["Entrada ou Saída [E ou S]",
                "Horário [AAAA-MM-DD hh:mm:ss]",
                "Motivo",
                "ID",
                "Função [V ou P]"],

                ["STRING",
                 "DATETIME",
				 "STRING",
                 "INT",
                 "STRING"]
            ]           
    }

    # mostrando os menus
    def show(self, menu):
        title = ""
        options = ""
        if menu == "tabelas": # menu inicial
            title = "\nSeleção de Tabelas"
            options = "1 - Condominio" \
                      "\n2 - Funcionários" \
                      "\n3 - Propriedade" \
                      "\n4 - Proprietários" \
                      "\n5 - Visitantes" \
                      "\n6 - Entrada|Saída de Funcionários" \
                      "\n7 - Entrada|Saída de Pessoas" \
                      "\n0 - Sair"
        elif menu == 1: # menu dos condomínios
            title = "\nSeleção de Opções - [Condomínios]"
            options = "1 - Cadastrar Condomínio" \
                      "\n2 - Exibir Condomínio" \
                      "\n3 - Atualizar Condomínio" \
					  "\n4 - Deletar Condomínio" \
					  "\n5 - Exibir Condomínios em Ordem Alfabética" \
                      "\n0 - Sair"
        elif menu == 2: # menu dos funcionários
            title = "\nSeleção de Opções - [Funcionários]"
            options = "1 - Cadastrar Funcionários" \
                      "\n2 - Exibir Funcionários" \
                      "\n3 - Atualizar Funcionários" \
					  "\n4 - Deletar Funcionários" \
					  "\n5 - Exibir Dados Pessoais" \
                      "\n0 - Sair"
        elif menu == 3: # menu das propriedades
            title = "\nSeleção de Opções - [Propriedades]"
            options = "1 - Cadastrar Propriedade" \
                      "\n2 - Exibir Propriedade" \
                      "\n3 - Atualizar Propriedade" \
					  "\n4 - Deletar Propriedade" \
					  "\n5 - Exibir Propriedades e seus Proprietários" \
                      "\n0 - Sair"
        elif menu == 4: # menu dos proprietários
            title = "\nSeleção de Opções - [Proprietários]"
            options = "1 - Cadastrar Proprietários" \
                      "\n2 - Exibir Proprietários" \
                      "\n3 - Atualizar Proprietários" \
					  "\n4 - Deletar Proprietários" \
					  "\n5 - Exibir Dados Pessoais" \
                      "\n0 - Sair"
        elif menu == 5: # menu dos Visitantes
            title = "\nSeleção de Opções - [Visitantes]"
            options = "1 - Cadastrar Visitantes" \
                      "\n2 - Exibir Visitantes" \
                      "\n3 - Atualizar Visitantes" \
					  "\n4 - Deletar Visitantes" \
					  "\n5 - Exibir Dados Pessoas" \
                      "\n0 - Sair"
        elif menu == 6: # menu dos proprietários
            title = "\nSeleção de Opções - [Entrada|Saída - Funcionários]"
            options = "1 - Inserir Entrada|Saída de Funcionários" \
                      "\n2 - Exibir Entrada|Saída de Funcionários" \
                      "\n3 - Atualizar Entrada|Saída de Funcionários" \
					  "\n4 - Deletar Entrada|Saída de Funcionários" \
					  "\n5 - Exibir Entrada|Saída de Funcionários e Seus Nomes" \
                      "\n0 - Sair"
        elif menu == 7: # menu dos proprietários
            title = "\nSeleção de Opções - [Entrada|Saída - Pessoas]"
            options = "1 - Inserir Entrada|Saída de Pessoas" \
                      "\n2 - Exibir Entrada|Saída de Pessoas" \
                      "\n3 - Atualizar Entrada|Saída de Pessoas" \
                      "\n4 - Deletar Entrada|Saída de Pessoas" \
					  "\n5 - Exibir Entrada|Saída de Pessoas e Seus Nomes" \
                      "\n0 - Sair"

        print(title)
        print("-" * len(title))
        print(options)
        selected_option = input("Digite o número da opção escolhida: ")
        selected_option = getCorrectInput(selected_option, "INT")

        while not selected_option and not selected_option == 0:
            selected_option = input("Digite o número da opção escolhida: ")
            selected_option = getCorrectInput(selected_option, "INT")
        
        return selected_option

    # menu de entrada de dados
    def getInfos(self, tabela):
        dados = []
        title = "Informe os dados"
        print("\n" + title)
        print("-" * len(title))
        # para cada campo da tabela, exibir uma mensagem
        for i in range(0, len(self.fields[tabela][0])):
            # receber a entrada de dados
            input_type = self.fields[tabela][1]
            dado = getCorrectInput(input(f"{ self.fields[tabela][0][i] }: "), input_type[i])
            while not dado:
                print("Valor inválido!")
                dado = getCorrectInput(input(f"{ self.fields[tabela][0][i] }: "), input_type[i])
            # inserir os dados em uma lista
            dados.append(dado)

        return dados

    # convertendo a lista de colunas e de valores em string 
    def getUpdates(self, column, values):
        updates = []
        # adiciona o sinal '=' entre a coluna e o valor a ser inserido nessa coluna
        for i in range(0, len(values)):
            updates.append(column[i] + " = " + values[i])
        
        return updates

    # retornando as tabelas que o menu possui
    def getTable(self, num):
        return self.menus[num]

# convertendo a lista de atributos para um string
def convertToString(lista):
    string = ""
    # adiciona virgulas entre as itens da lista
    for i in range(0, len(lista)):
        separator = ""
        if not i == len(lista) - 1:
            separator = ", "
        string += str(lista[i]) + separator

    return string

# verificando o tipo da entrada "DATATIME"
def getCorrectInput(input_value, input_type):
    # tenta converter para int
    try:
        int(input_value)
        # caso a entrada seja int mas o tipo necessário não corresponda
        if input_type == "INT" or input_type == "STRING":
            return input_value
        else:
            return False
    except ValueError:
        try:
            # caso a entrada seja float mas o tipo necessário não corresponda
            float(input_value)
            if input_type == "FLOAT" or input_type == "STRING":
                return input_value
            else:
                return False
        except ValueError:
            try:
                # caso a entrada seja datetime mas o tipo necessário não corresponda
                input_value = datetime.strptime(input_value,'%Y-%m-%d %H:%M:%S')
                if input_type == "DATETIME" or input_type == "STRING":
                    return "'" + str(input_value) + "'"
                else:
                    return False
            except ValueError:
                if input_type == "STRING":
                    return "'" + str(input_value) + "'"
                else:
                    return False


def clearTerminal():
    print("\033[2J\033[1;1H")
