import sqlite3
from sqlite3 import Error


# classe do Banco de Dados
class Banco:

    def __init__(self):
        self.banco = 'condominio_banco.db'
        self.conn = None
        self.conn = sqlite3.connect(self.banco)
        self.c_pos = self.conn.cursor()
        self.select_especial = {
			"condominios": "SELECT * FROM condominios ORDER BY RazaoSocial DESC",
			"funcionarios": "SELECT Nome, CPF, Funcao, Salario,idCondominio FROM funcionarios ORDER BY Nome ASC",
			"esfuncionarios": "SELECT funcionarios.Nome, esfuncionarios.EntradaSaida, esfuncionarios.Horario, esfuncionarios.Motivo FROM esfuncionarios INNER JOIN funcionarios ON funcionarios.id = esfuncionarios.id ORDER BY funcionarios.Nome DESC",
			"proprietarios": "SELECT Nome, Acesso, CPFCNPJ FROM proprietarios ORDER BY Nome DESC",
		    "propriedades": "SELECT propriedades.id, proprietarios.Nome, propriedades.idCondominio FROM propriedades INNER JOIN proprietarios ON proprietarios.id = propriedades.IdProprietario ORDER BY proprietarios.Nome",
			"visitantes": "SELECT Nome, CPF, Motivo, IdPropriedade FROM visitantes ORDER BY Nome DESC",
			"espessoas": "SELECT CASE Funcao WHEN 'V' THEN visitantes.Nome ELSE proprietarios.Nome END Name, espessoas.Horario, espessoas.EntradaSaida, espessoas.Motivo FROM espessoas INNER JOIN visitantes ON visitantes.id = espessoas.idPessoa INNER JOIN proprietarios ON visitantes.id = proprietarios.id"
		}

    def createDataBase(self):
        # criando a tabela condominios
        try:
            self.c_pos.execute("CREATE TABLE condominios("
							"id INTEGER PRIMARY KEY AUTOINCREMENT,"
							"RazaoSocial VARCHAR(60) NOT NULL,"
							"Fantasia VARCHAR(60) NOT NULL"
							")")

			# criando a tabela funcionarios
            self.c_pos.execute("CREATE TABLE funcionarios("
							"id INTEGER PRIMARY KEY AUTOINCREMENT,"
							"Nome VARCHAR(45) NOT NULL,"
							"CPF INT(11) NOT NULL,"
							"Endereco VARCHAR(45) NOT NULL,"
							"Salario FLOAT NOT NULL,"
							"Funcao VARCHAR(45) NOT NULL,"
							"Acesso VARCHAR(20) NOT NULL,"
							"idCondominio INT NOT NULL,"
							"FOREIGN KEY (idCondominio) REFERENCES condominios (id)"
							")")

			# criando a tabela esfuncionarios
            self.c_pos.execute("CREATE TABLE esfuncionarios("
							"id INTEGER PRIMARY KEY AUTOINCREMENT,"
                            "EntradaSaida VARCHAR(1) NOT NULL,"
							"Horario SMALLDATETIME NOT NULL,"
							"Motivo VARCHAR(30) NOT NULL,"
							"idFuncionarios INT NOT NULL,"
                            "FOREIGN KEY (idFuncionarios) REFERENCES funcionarios (id)"
							")")

			# criando a tabela proprietarios
            self.c_pos.execute("CREATE TABLE proprietarios("
							"id INTEGER PRIMARY KEY AUTOINCREMENT,"
							"Nome VARCHAR(45) NOT NULL,"
							"Acesso VARCHAR(10) NOT NULL,"
							"CPFCNPJ VARCHAR(20) NOT NULL"
							")")

			# criando a tabela propriedades
            self.c_pos.execute("CREATE TABLE propriedades("
							"id INTEGER PRIMARY KEY AUTOINCREMENT,"
							"CodInterno VARCHAR(10) NOT NULL,"
							"IdCondominio INT NOT NULL,"
							"IdProprietario INT NOT NULL,"
							"FOREIGN KEY (IdCondominio) REFERENCES condominios (id),"
							"FOREIGN KEY (IdProprietario) REFERENCES proprietarios (id)"
							")")

			# criando a tabela visitantes
            self.c_pos.execute("CREATE TABLE visitantes("
							"id INTEGER PRIMARY KEY AUTOINCREMENT,"
							"Nome VARCHAR(45) NOT NULL,"
							"CPF INT(11) NOT NULL,"
							"Motivo VARCHAR(1) NOT NULL,"
							"IdPropriedade INT NOT NULL,"
							"FOREIGN KEY (IdPropriedade) REFERENCES propriedades(id)"
							")")

			# criando a tabela espessoas
            self.c_pos.execute("CREATE TABLE espessoas("
							"id INTEGER PRIMARY KEY AUTOINCREMENT,"
							"EntradaSaida VARCHAR(1) NOT NULL,"
							"Horario SMALLDATETIME NOT NULL,"
							"Motivo VARCHAR(20) NOT NULL,"
							"idPessoa INT NOT NULL,"
							"Funcao VARCHAR(1) NOT NULL"
							")")
							
            self.conn.commit()
        except Error:
            pass

	# salvando e fechando conexão
    def saveClose(self):
        print("\nSalvando dados...")
        self.conn.commit()
        print("Fechando conexão...")
        self.conn.close()

	# inserindo os dados no banco
    def insertDefault(self, tabela, columns, atributos):	
        self.c_pos.execute(f"INSERT INTO {tabela} ({columns}) VALUES ({atributos}) ")
        self.conn.commit()

	# selecionando os dados do banco
    def selectDefault(self, tabela):
		# seleciona os dados da tabela
        self.c_pos.execute(f"SELECT * FROM {tabela}")
        resultado = self.c_pos.fetchall()
        title = f"\nExibindo valores da tabela: {tabela}"
		# caso a tabela esteja vazia retorna false
        if len(resultado) == 0:
            print("\nVazio!")
            return False
        else:
            print(title)
            print("-" * len(title))
		# exibe os resultados na tela
        for i in resultado:
            print(i)
        
        return True

	# atualizando os dados do banco
    def updateDefault(self, table, updates, id):
        self.c_pos.execute(f"UPDATE {table} SET {updates} WHERE id = {id}")
        self.conn.commit()

	# atualizando os dados do banco
    def deleteDefault(self, table, id):
        self.c_pos.execute(f"DELETE FROM {table} WHERE id = {id}")
        self.conn.commit()

    def selectEspecial(self, table):
        self.c_pos.execute(self.select_especial[table])
        resultado = self.c_pos.fetchall()

        title = f"\nExibindo a seleção: {table}"
		# caso a tabela esteja vazia retorna false
        if len(resultado) == 0:
            print("\nVazio!")
            return False
        else:
            print(title)
            print("-" * len(title))
		# exibe os resultados na tela
        for i in resultado:
            print(i)
	
	# retornando as colunas que o banco possui
    def getColumns(self, tabela):
		# retorna as colunas que o banco possui
        self.c_pos.execute(f'PRAGMA table_info({tabela})')
        resultado = self.c_pos.fetchall()
        colunas = []
        aux = 0
		# insere as colunas em uma lista
        for i in resultado:
            if not aux == 0:
                colunas.append(i[1])
            aux += 1

        return colunas
