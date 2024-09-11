import mysql.connector
import random
import string

# Configurações de conexão com o banco de dados
def conectar_banco():
    return mysql.connector.connect(
        host="localhost",       # Host onde o MySQL está rodando
        user="root",            # Usuário do MySQL
        password="123456789",   # Substitua com a sua senha do MySQL
        database="db_formulae"  # Nome do banco de dados
    )

# Função para gerar código de 3 letras e 3 números
def gerar_codigo():
    letras = string.ascii_uppercase
    numeros = ''.join(random.choice(string.digits) for _ in range(3))
    return ''.join(random.choice(letras) for _ in range(3)) + numeros

# Função para verificar se o email já está cadastrado
def verificar_email(email):
    conexao = conectar_banco()
    cursor = conexao.cursor(dictionary=True)
    cursor.execute("SELECT * FROM usuarios WHERE email = %s", (email,))
    resultado = cursor.fetchone()
    cursor.close()
    conexao.close()
    return resultado is not None

# Função para verificar se o código é único na tabela de usuários
def verificar_codigo_unico(codigo):
    conexao = conectar_banco()
    cursor = conexao.cursor(dictionary=True)
    cursor.execute("SELECT * FROM usuarios WHERE codigo = %s", (codigo,))
    resultado = cursor.fetchone()
    cursor.close()
    conexao.close()
    return resultado is None

# Função para verificar se o código de divulgação é válido e retornar o email do usuário que o possui
def verificar_codigo_divulgacao(codigo_utilizado):
    conexao = conectar_banco()
    cursor = conexao.cursor(dictionary=True)
    cursor.execute("SELECT email FROM usuarios WHERE codigo = %s", (codigo_utilizado,))
    resultado = cursor.fetchone()
    cursor.close()
    conexao.close()
    return resultado

# Função para atualizar o saldo do usuário no banco de dados
def atualizar_saldo(email, saldo_adicional):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute("UPDATE transacoes SET saldo = saldo + %s WHERE email = %s", (saldo_adicional, email))
    conexao.commit()
    cursor.close()
    conexao.close()

# Função para cadastrar um novo usuário
def cadastrar_usuario():
    email = input("Digite seu email: ")
    while verificar_email(email):
        print("Email já cadastrado, digite um email diferente.")
        email = input("Digite seu email: ")
    
    confirmar_email = input("Digite seu email novamente para confirmar: ")
    while email != confirmar_email:
        print("Os emails não coincidem. Por favor, tente novamente.")
        email = input("Digite seu email: ")
        confirmar_email = input("Digite seu email novamente para confirmar: ")
    
    senha = input("Digite sua senha: ")
    confirmar_senha = input("Digite sua senha novamente para confirmar: ")
    while senha != confirmar_senha:
        print("As senhas não coincidem. Por favor, tente novamente.")
        senha = input("Digite sua senha: ")
        confirmar_senha = input("Digite sua senha novamente para confirmar: ")

    # Gerar código único
    codigo = gerar_codigo()
    while not verificar_codigo_unico(codigo):
        codigo = gerar_codigo()

    # Verificar código de divulgação
    codigo_utilizado = input("Digite o código de divulgação indicado (ou deixe em branco se não tiver): ")
    saldo = 0
    if codigo_utilizado:
        divulgador = verificar_codigo_divulgacao(codigo_utilizado)
        if divulgador:
            # O novo usuário e o usuário que indicou recebem 100 pontos
            saldo = 100  # Novo usuário ganha 100 pontos
            atualizar_saldo(divulgador['email'], 100)  # Indicador ganha 100 pontos
            print(f"O usuário {divulgador['email']} recebeu 100 pontos pela sua indicação.")
        else:
            print("Código de divulgação inválido. Nenhum saldo adicional será adicionado.")

    # Salvar dados do novo usuário no banco de dados
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute("""
        INSERT INTO usuarios (email, senha, codigo_utilizado, codigo)
        VALUES (%s, %s, %s, %s)
    """, (email, senha, codigo_utilizado, codigo))
    
    # Salvar transação no banco de dados com o saldo inicial
    cursor.execute("""
        INSERT INTO transacoes (email, saldo)
        VALUES (%s, %s)
    """, (email, saldo))
    
    conexao.commit()
    cursor.close()
    conexao.close()

    print("Usuário cadastrado com sucesso!")
    print(f"Seu código único de divulgação é: {codigo}")
    if saldo > 0:
        print(f"Seu saldo inicial é de {saldo} pontos.")

# Função principal para executar o programa
def principal():
    cadastrar_usuario()

if __name__ == "__main__":
    principal()

