import mysql.connector

# Função para conectar ao banco de dados
def conectar_banco():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456789",
        database="db_formulae"
    )

# Calcula os pontos baseados na colocação
def ganho_colocacao(posicao):
    if posicao == 1:
        return 25
    elif posicao == 2:
        return 18
    elif posicao == 3:
        return 15
    elif 4 <= posicao <= 10:
        return [12, 10, 8, 6, 4, 2, 1][posicao - 4]
    else:
        return 0

# Calcula os pontos baseados nas atividades realizadas
def acoes_realizadas(atividades):
    pontuacoes = {
        "Pit stop": 5,
        "Ultrapassagem": 10,
        "Volta rápida": 15,
        "Colisão leve": -5
    }
    pontuacao_total = sum(pontuacoes.get(atividade, 0) for atividade in atividades)
    return pontuacao_total

# Autentica o usuário com base no email e senha fornecidos
def autenticar_usuario(email, senha):
    conexao = conectar_banco()
    cursor = conexao.cursor(dictionary=True)
    cursor.execute("SELECT * FROM usuarios WHERE email = %s AND senha = %s", (email, senha))
    usuario = cursor.fetchone()
    cursor.close()
    conexao.close()
    return (usuario is not None, usuario)

# Obtém o saldo do usuário com base no email
def obter_saldo(email):
    conexao = conectar_banco()
    cursor = conexao.cursor(dictionary=True)
    cursor.execute("SELECT saldo FROM transacoes WHERE email = %s", (email,))
    saldo = cursor.fetchone()
    cursor.close()
    conexao.close()
    return saldo['saldo'] if saldo else 0

# Atualiza o saldo do usuário com base na pontuação obtida
def atualizar_saldo(email, pontos):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute("SELECT saldo FROM transacoes WHERE email = %s", (email,))
    saldo_atual = cursor.fetchone()
    
    if saldo_atual:
        saldo_atual = saldo_atual[0]  # Ajustado para acessar o primeiro item da tupla
        novo_saldo = saldo_atual + pontos
        cursor.execute("UPDATE transacoes SET saldo = %s WHERE email = %s", (novo_saldo, email))
    else:
        cursor.execute("INSERT INTO transacoes (email, saldo) VALUES (%s, %s)", (email, pontos))
    
    conexao.commit()
    cursor.close()
    conexao.close()

# Desconta o saldo do usuário com base no valor fornecido
def descontar_saldo(email, valor):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute("SELECT saldo FROM transacoes WHERE email = %s", (email,))
    saldo_atual = cursor.fetchone()
    
    if saldo_atual:
        saldo_atual = saldo_atual[0]  # Ajustado para acessar o primeiro item da tupla
        novo_saldo = saldo_atual - valor
        cursor.execute("UPDATE transacoes SET saldo = %s WHERE email = %s", (novo_saldo, email))
    
    conexao.commit()
    cursor.close()
    conexao.close()

# Atualiza a pontuação dos corredores da corrida passada na corrida atual
def atualizar_pontuacao(corrida):
    for posicao, info in corrida.items():
        info["pontuacao"] = ganho_colocacao(posicao) + acoes_realizadas(info["atividades"])

# Dados simulando uma corrida passada
corrida_passada = {
    1: {"nome": "Pascal Wehrlein - TAG Heuer Porsche", "atividades": ["Ultrapassagem", "Volta rápida"], "classificacao": "caro"},
    2: {"nome": "Mitch Evans - Jaguar TCS Racing", "atividades": ["Pit stop", "Ultrapassagem", "Colisão leve"], "classificacao": "caro"},
    3: {"nome": "Antonio Felix da Costa - TAG Heuer Porsche", "atividades": ["Volta rápida", "Pit stop"], "classificacao": "caro"},
    4: {"nome": "Nick Cassidy - Jaguar TCS Racing", "atividades": ["Pit stop", "Volta rápida"], "classificacao": "caro"},
    5: {"nome": "Jean-Éric Vergne - DS Penske", "atividades": ["Pit stop", "Volta rápida"], "classificacao": "caro"},
    6: {"nome": "Jake Dennis - Avalanche Andretti Formula E", "atividades": ["Ultrapassagem", "Pit stop"], "classificacao": "caro"},
    7: {"nome": "Stoffel Vandoorne - DS Penske", "atividades": ["Ultrapassagem", "Pit stop"], "classificacao": "caro"},
    8: {"nome": "Norman Nato - Avalanche Andretti Formula E", "atividades": ["Pit stop", "Colisão leve"], "classificacao": "medio"},
    9: {"nome": "Robin Frijns - ABT CUPRA Formula E Team", "atividades": ["Pit stop"], "classificacao": "medio"},
    10: {"nome": "Sam Bird - NEOM McLaren Formula E Team", "atividades": ["Ultrapassagem", "Pit stop"], "classificacao": "medio"},
    11: {"nome": "Jake Hughes - NEOM McLaren Formula E Team", "atividades": ["Volta rápida", "Colisão leve"], "classificacao": "medio"},
    12: {"nome": "Sacha Fenestraz - Nissan Formula E Team", "atividades": ["Pit stop"], "classificacao": "medio"},
    13: {"nome": "Edoardo Mortara - Maserati MSG Racing", "atividades": ["Ultrapassagem", "Pit stop"], "classificacao": "medio"},
    14: {"nome": "Maximilian Günther - Maserati MSG Racing", "atividades": ["Volta rápida", "Colisão leve"], "classificacao": "medio"},
    15: {"nome": "Lucas di Grassi - Mahindra Racing", "atividades": ["Pit stop"], "classificacao": "medio"},
    16: {"nome": "Nyck de Vries - Mahindra Racing", "atividades": ["Ultrapassagem"], "classificacao": "medio"},
    17: {"nome": "Daniel Abt - NIO 333 Racing", "atividades": ["Volta rápida", "Ultrapassagem"], "classificacao": "medio"},
    18: {"nome": "André Lotterer - Andretti Formula E Team", "atividades": ["Pit stop", "Volta rápida"], "classificacao": "medio"},
    19: {"nome": "Nico Müller - ABT CUPRA Formula E Team", "atividades": ["Colisão leve"], "classificacao": "barato"},
    20: {"nome": "Oliver Rowland - Nissan Formula E Team", "atividades": ["Colisão leve"], "classificacao": "barato"},
    21: {"nome": "Sérgio Sette Câmara - NIO 333 Racing", "atividades": ["Pit stop", "Colisão leve"], "classificacao": "barato"}
}

# Define o custo do contrato para cada colocação
custo_contrato = {
    "Colocação": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21],
    "Custo": [50, 47, 44, 41, 38, 35, 32, 29, 26, 23, 20, 17, 14, 11, 8, 5, 2, 1, 1, 1, 1]
}

# Atualiza a pontuação dos corredores na corrida passada
atualizar_pontuacao(corrida_passada)

# Atualiza o custo do contrato dos corredores na corrida passada
for i, (numero, info) in enumerate(corrida_passada.items()):
    info["custo_contrato"] = custo_contrato["Custo"][i]

# Dados simulando uma corrida atual
corrida_atual = {
    1: {"nome": "Nick Cassidy - Jaguar TCS Racing", "atividades": ["Ultrapassagem", "Volta rápida"], "classificacao": "caro"},
    2: {"nome": "Jake Dennis - Avalanche Andretti Formula E", "atividades": ["Ultrapassagem", "Pit stop"], "classificacao": "caro"},
    3: {"nome": "Jean-Éric Vergne - DS Penske", "atividades": ["Volta rápida"], "classificacao": "caro"},
    4: {"nome": "Stoffel Vandoorne - DS Penske", "atividades": ["Pit stop", "Ultrapassagem"], "classificacao": "caro"},
    5: {"nome": "Pascal Wehrlein - TAG Heuer Porsche", "atividades": ["Pit stop"], "classificacao": "caro"},
    6: {"nome": "Mitch Evans - Jaguar TCS Racing", "atividades": ["Pit stop"], "classificacao": "caro"},
    7: {"nome": "Antonio Felix da Costa - TAG Heuer Porsche", "atividades": ["Volta rápida"], "classificacao": "caro"},
    8: {"nome": "Norman Nato - Avalanche Andretti Formula E", "atividades": ["Pit stop"], "classificacao": "medio"},
    9: {"nome": "Robin Frijns - ABT CUPRA Formula E Team", "atividades": ["Pit stop"], "classificacao": "medio"},
    10: {"nome": "Jake Hughes - NEOM McLaren Formula E Team", "atividades": ["Colisão leve"], "classificacao": "medio"},
    11: {"nome": "Sam Bird - NEOM McLaren Formula E Team", "atividades": ["Colisão leve"], "classificacao": "medio"},
    12: {"nome": "Sacha Fenestraz - Nissan Formula E Team", "atividades": ["Ultrapassagem"], "classificacao": "medio"},
    13: {"nome": "Edoardo Mortara - Maserati MSG Racing", "atividades": ["Pit stop"], "classificacao": "medio"},
    14: {"nome": "Maximilian Günther - Maserati MSG Racing", "atividades": ["Colisão leve"], "classificacao": "medio"},
    15: {"nome": "Lucas di Grassi - Mahindra Racing", "atividades": ["Ultrapassagem"], "classificacao": "medio"},
    16: {"nome": "Nyck de Vries - Mahindra Racing", "atividades": ["Volta rápida"], "classificacao": "medio"},
    17: {"nome": "Daniel Abt - NIO 333 Racing", "atividades": ["Pit stop"], "classificacao": "medio"},
    18: {"nome": "André Lotterer - Andretti Formula E Team", "atividades": ["Volta rápida"], "classificacao": "medio"},
    19: {"nome": "Nico Müller - ABT CUPRA Formula E Team", "atividades": ["Colisão leve"], "classificacao": "barato"},
    20: {"nome": "Oliver Rowland - Nissan Formula E Team", "atividades": ["Colisão leve"], "classificacao": "barato"},
    21: {"nome": "Sérgio Sette Câmara - NIO 333 Racing", "atividades": ["Pit stop"], "classificacao": "barato"}
}

# Atualiza a pontuação dos corredores na corrida atual
atualizar_pontuacao(corrida_atual)

print("Bem-vindo ao E-GAME")
acesso = False

for tentativa in range(1, 4):
    email = input("Digite seu email: ")
    senha = input("Digite sua senha: ")
    
    autenticado, usuario = autenticar_usuario(email, senha)
    if not autenticado:
        print(f"Email e senha errados, você tem mais {3 - tentativa} tentativa(s)")
    else:
        acesso = True  
        break

if acesso:
    saldo_usuario = obter_saldo(email)
    print(f"Seu saldo atual é: {saldo_usuario}")
    print("Abaixo os dados da última corrida")
    for numero, corredor in corrida_passada.items():
        print(f'{numero}: {corredor}')

    escolha_usuario = []
    custo_total = 0

    while len(escolha_usuario) < 3:
        escolha = int(input("Digite o número do corredor a ser contratado (um corredor por vez): "))
        if 1 <= escolha <= len(corrida_passada) and escolha not in escolha_usuario:
            custo_total += corrida_passada[escolha]["custo_contrato"]
            if custo_total <= saldo_usuario:
                escolha_usuario.append(escolha)
            else:
                print("Saldo insuficiente para contratar este corredor. Tente outro corredor.")
                custo_total -= corrida_passada[escolha]["custo_contrato"]
        else:
            print("Número inválido ou já escolhido, tente novamente.")

    # Descontar o custo total do saldo do usuário
    descontar_saldo(email, custo_total)

    # Imprimir a quantidade de pontos descontados
    print(f"Foram descontados {custo_total} ponto(s). Seu saldo atual agora é {saldo_usuario - custo_total}")

    print("Resultados dos corredores escolhidos na corrida atual:")

    # Exibir os dados atualizados da corrida atual para os corredores escolhidos
    for escolha in escolha_usuario:
        print(corrida_atual[escolha])

    # Calcular a soma das pontuações dos corredores escolhidos na corrida atual
    soma_pontuacoes = sum(corrida_atual[escolha]["pontuacao"] for escolha in escolha_usuario)

    # Atualizar o saldo do usuário com a pontuação obtida
    atualizar_saldo(email, soma_pontuacoes)
    
    print(f"Sua soma de pontuações na corrida atual é: {soma_pontuacoes}")
    print(f"{soma_pontuacoes} ponto(s) foram adicionados ao seu saldo. Seu saldo atual agora é {saldo_usuario - custo_total + soma_pontuacoes}")
else:
    print("Acesso negado após 3 tentativas.")
