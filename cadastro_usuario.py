import csv
import random
import string
import os


# Proximo semestre colocar dandos csv em um banco de dados 

# Codigo responsável pela criação de cadastros


# Função para gerar código de 3 letras e 3 números
def gerar_codigo():
    letras = string.ascii_uppercase
    numeros = ''.join(random.choice(string.digits) for _ in range(3))
    return ''.join(random.choice(letras) for _ in range(3)) + numeros

# Função para criar a tabela de usuários
def criar_tabela_usuarios():
    if not os.path.exists('usuarios.csv'):
        with open('usuarios.csv', mode='w', newline='') as file:
            escritor = csv.writer(file)
            escritor.writerow(['EMAIL', 'SENHA', 'CODIGO_UTILIZADO', 'CODIGO'])

# Função para criar a tabela de transações
def criar_tabela_transacoes():
    if not os.path.exists('transacoes.csv'):
        with open('transacoes.csv', mode='w', newline='') as file:
            escritor = csv.writer(file)
            escritor.writerow(['EMAIL', 'SALDO'])

# Função para verificar se o email já está cadastrado
def verificar_email(email):
    with open('usuarios.csv', mode='r', newline='') as file:
        leitor = csv.DictReader(file)
        for linha in leitor:
            if linha['EMAIL'] == email:
                return True
        return False

# Função para verificar se o código é único na tabela de usuários
def verificar_codigo_unico(codigo):
    with open('usuarios.csv', mode='r', newline='') as file:
        leitor = csv.DictReader(file)
        for linha in leitor:
            if linha['CODIGO'] == codigo:
                return False
        return True

# Função para verificar se o código de divulgação é válido
def verificar_codigo_divulgacao(codigo_utilizado):
    with open('usuarios.csv', mode='r', newline='') as file:
        leitor = csv.DictReader(file)
        for linha in leitor:
            if linha['CODIGO'] == codigo_utilizado:
                return True
        return False

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
    if codigo_utilizado and verificar_codigo_divulgacao(codigo_utilizado):
        saldo = 100

    # Salvar dados do usuário em um arquivo CSV
    with open('usuarios.csv', mode='a', newline='') as file:
        escritor = csv.writer(file)
        escritor.writerow([email, senha, codigo_utilizado, codigo])

    # Salvar transação em um arquivo CSV
    with open('transacoes.csv', mode='a', newline='') as file:
        escritor = csv.writer(file)
        escritor.writerow([email, saldo])

    print("Usuário cadastrado com sucesso!")
    print(f"Seu código único de divulgação é: {codigo}")
    if saldo > 0:
        print(f"Seu saldo inicial é de {saldo} pontos.")

# Função principal para executar o programa
def principal():
    criar_tabela_usuarios()
    criar_tabela_transacoes()
    cadastrar_usuario()

if __name__ == "__main__":
    principal()
