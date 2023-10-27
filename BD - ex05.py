import sqlite3

banco_empresa = sqlite3.connect('Empresa.db')
cursor = banco_empresa.cursor()

#criando a tabela funcionários
cursor.execute("CREATE TABLE IF NOT EXISTS funcionarios(\
               ID INTEGER PRIMARY KEY AUTOINCREMENT,\
               NOME VARCHAR (50) NOT NULL,\
               CPF VARCHAR (11) NOT NULL,\
               EMAIL VARCHAR(30) NOT NULL,\
               TELEFONE VARCHAR(11) NOT NULL,\
               RUA VARCHAR(50) NOT NULL,\
               NUMER0 VARCHAR(5) NOT NULL,\
               CIDADE TEXT NOT NULL,\
               UF VARCHAR(2) NOT NULL,\
               CEP VARCHAR(8),\
               PAIS TEXT)")

#criando a tabela dadosCorporativos
cursor.execute("CREATE TABLE IF NOT EXISTS dadosCorporativos(\
               ID INTEGER PRIMARY KEY AUTOINCREMENT,\
               SETOR VARCHAR(50) NOT NULL,\
               CARGO VARCHAR(20) NOT NULL,\
               SALARIO FLOAT)")

#criando a tabela diversidade
cursor.execute("CREATE TABLE IF NOT EXISTS diversidade(\
               ID INTEGER PRIMARY KEY AUTOINCREMENT,\
               GENERO VARCHAR(50) NOT NULL,\
               IDADE VARCHAR(2) NOT NULL,\
               ORIENTACAO SEXUAL VARCHAR(50) NOT NULL)")


#Inserindo dados na tabela funcionarios
add_funcionarios = "INSERT INT funcionarios(NOME, CPF, EMAIL, TELEFONE, RUA, NUMERO, CIDADE, UF, CEP, PAIS) VALUES(?,?,?,?,?,?,?,?,?,?)"

add_funcionarios.execute('INSERT TO funcionarios(NOME, CPF, EMAIL, TELEFONE, RUA, NUMERO, CIDADE, UF, CEP, PAIS) VALUES("Soraia Ramos", 48858695411, "soraia.ramos@gmail.com", 55487598, "Rua Moraes", 20, "Santo André", "SP", 00123-450, "Brasil")')
add_funcionarios.execute('INSERT TO funcionarios(NOME, CPF, EMAIL, TELEFONE, RUA, NUMERO, CIDADE, UF, CEP, PAIS) VALUES("Fernanda Eduardos", 12345678911, "fend.dos@gmail.com", 48487598, Avenida Campos, 450, "Bolotas", "SP", 04523-450, "Brasil")')
add_funcionarios.execute('INSERT TO funcionarios(NOME, CPF, EMAIL, TELEFONE, RUA, NUMERO, CIDADE, UF, CEP, PAIS) VALUES("Eudes Gouveia", 78945612378, "gouveia.ed@gmail.com", 45617895, Rua 9 de agostinho, 213, "Minas Gerais", "MG", 78945-120, "Brasil")')
add_funcionarios.execute('INSERT TO funcionarios(NOME, CPF, EMAIL, TELEFONE, RUA, NUMERO, CIDADE, UF, CEP, PAIS) VALUES("Geovanna Mendes", 45678912300, "geovanna.mds@gmail.com", 55487789, Avenida JJ, 98, "Cidade verde", "PI", 45678-125, "Brasil")')
add_funcionarios.execute('INSERT TO funcionarios(NOME, CPF, EMAIL, TELEFONE, RUA, NUMERO, CIDADE, UF, CEP, PAIS) VALUES("Osvaldo Dunker", 78851495411, "osvaldinho09@gmail.com", 12487546, Rua Leitão, 12, "Rio de Janeiro", "RJ", 58123-450, "Brasil")')
add_funcionarios.execute('INSERT TO funcionarios(NOME, CPF, EMAIL, TELEFONE, RUA, NUMERO, CIDADE, UF, CEP, PAIS) VALUES("Ana Rainee", 78461254631, "rainee.ana@gmail.com", 78948569, Rua Cascalho, 90, "São Paulo", "SP", 00894-450, "Brasil")')
add_funcionarios.execute('INSERT TO funcionarios(NOME, CPF, EMAIL, TELEFONE, RUA, NUMERO, CIDADE, UF, CEP, PAIS) VALUES("Danilo Souza", 70258695411, "danilo.souza@gmail.com", 78451236, Rua Leonarod, 208, "Santo Estevão", "BH", 78945-789, "Brasil")')

#Inserindo dados na tabela dadosCorporativos
add_dadosCorporativos = "INSERT INT dadosCorporativos(SETOR, CARGO, SALARIO) VALUES(?,?,?)"

add_dadosCorporativos.execute('INSERT TO dadosCorporativos(SETOR, CARGO, SALARIO) VALUES("Financeiro", "Auxilar Administrativa", 2000)')
add_dadosCorporativos.execute('INSERT TO dadosCorporativos(SETOR, CARGO, SALARIO) VALUES("Recursos Humano", "Gerente de RH", 8000)')
add_dadosCorporativos.execute('INSERT TO dadosCorporativos(SETOR, CARGO, SALARIO) VALUES("Financiero", "Estagiário", 1200)')
add_dadosCorporativos.execute('INSERT TO dadosCorporativos(SETOR, CARGO, SALARIO) VALUES("Suporte", "Coordernador de TI", 7000)')
add_dadosCorporativos.execute('INSERT TO dadosCorporativos(SETOR, CARGO, SALARIO) VALUES("Suporte", "Analista de Suporte", 3000)')
add_dadosCorporativos.execute('INSERT TO dadosCorporativos(SETOR, CARGO, SALARIO) VALUES("Marketing", "Analista de Comunicação", 3000)')
add_dadosCorporativos.execute('INSERT TO dadosCorporativos(SETOR, CARGO, SALARIO) VALUES("TI", "Programador FullStack", 8000)')

#Inserindo dados na tabela diversidade
add_diversidade = "INSERT INT diversidade(GENERO, IDADE, ORIENTACAO SEXUAL) VALUES(?,?,?)"

add_diversidade.execute('INSERT TO diversidade(GENERO, IDADE, ORIENTACAO SEXUAL) VALUES("F", 25, "Bissexual")')
add_diversidade.execute('INSERT TO diversidade(GENERO, IDADE, ORIENTACAO SEXUAL) VALUES("F", 46, "Heterossexual")')
add_diversidade.execute('INSERT TO diversidade(GENERO, IDADE, ORIENTACAO SEXUAL) VALUES("M", 50, "Não-Binário")')
add_diversidade.execute('INSERT TO diversidade(GENERO, IDADE, ORIENTACAO SEXUAL) VALUES("F", 45, "Heterossexual")')
add_diversidade.execute('INSERT TO diversidade(GENERO, IDADE, ORIENTACAO SEXUAL) VALUES("M", 30, "Bissexual")')
add_diversidade.execute('INSERT TO diversidade(GENERO, IDADE, ORIENTACAO SEXUAL) VALUES("F", 27, "N/A")')
add_diversidade.execute('INSERT TO diversidade(GENERO, IDADE, ORIENTACAO SEXUAL) VALUES("M", 36, "Heterossexual")')

#define a consulta SQL para selecionar todos os registros da tabela
selecionar_tudo = "SELECT * FROM funcionarios"
selecionar_tudo = "SELECT * FROM dadosCorporativos"
selecionar_tudo = "SELECT * FROM diversidade"

#Comandos Joins para realizar consultas nas tabelas


#executa a consulta SQL para obter todas as entradas da tabela .
entradas = cursor.execute(selecionar_tudo).fetchall
banco.commit();
banco.close();