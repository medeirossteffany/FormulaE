import cv2
import time
import os
import mysql.connector
from mysql.connector import Error

# Função para conectar ao banco de dados
def conectar_banco():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456789",
        database="db_formulae"
    )

# Função para autenticar o usuário a partir do banco de dados MySQL
def autenticar_usuario(email, senha):
    try:
        conexao = conectar_banco()
        cursor = conexao.cursor(dictionary=True)
        cursor.execute("SELECT * FROM usuarios WHERE email = %s AND senha = %s", (email, senha))
        usuario = cursor.fetchone()
        cursor.close()
        conexao.close()
        return (usuario is not None, usuario)
    except Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return False, None

# Função para atualizar o saldo do usuário no banco de dados MySQL
def atualizar_saldo(email, pontos):
    try:
        conexao = conectar_banco()
        cursor = conexao.cursor()
        cursor.execute("SELECT saldo FROM transacoes WHERE email = %s", (email,))
        saldo_atual = cursor.fetchone()
        
        if saldo_atual:
            saldo_atual = saldo_atual[0]
            novo_saldo = saldo_atual + pontos
            cursor.execute("UPDATE transacoes SET saldo = %s WHERE email = %s", (novo_saldo, email))
        else:
            cursor.execute("INSERT INTO transacoes (email, saldo) VALUES (%s, %s)", (email, pontos))
        
        conexao.commit()
        cursor.close()
        conexao.close()
    except Error as e:
        print(f"Erro ao atualizar saldo: {e}")

# Função principal que executa a lógica de reprodução de vídeo e cálculo de pontos
def main(video_path, total_time_video):
    if not os.path.exists(video_path):
        print(f"O arquivo de vídeo '{video_path}' não existe.")
        return

    print(f"Tentando abrir o vídeo: {video_path}")
    cap = cv2.VideoCapture(video_path)
    
    if not cap.isOpened():
        print(f"Erro ao abrir o vídeo: {video_path}")
        return
    else:
        print(f"Vídeo '{video_path}' aberto com sucesso.")

    # Obtém o FPS real do vídeo
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_time = 1 / fps

    # Registra o tempo inicial
    start_time = time.time()
    paused = False

    while True:
        if not paused:
            ret, frame = cap.read()
            if not ret:
                print("Fim do vídeo ou erro ao ler o frame. Aguardando o usuário fechar.")
                paused = True

        if paused:
            # Exibe o último frame até que o usuário pressione 'q'
            if frame is not None:
                cv2.imshow('Video', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            cv2.imshow('Video', frame)
            # Saia se a tecla 'q' for pressionada
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # Remove o delay de tempo entre frames
        #time.sleep(frame_time)

    # Registra o tempo final
    end_time = time.time()
    
    # Calcula o tempo total que o vídeo ficou aberto
    total_time_opened = end_time - start_time
    
    # Calcula a porcentagem do tempo que o vídeo ficou aberto
    percentage_opened = (total_time_opened / total_time_video) * 100
    
    # Libera o objeto de captura e fecha todas as janelas OpenCV
    cap.release()
    cv2.destroyAllWindows()

    # Exibe o tempo total e a porcentagem que o vídeo ficou aberto
    print(f"O vídeo ficou aberto {percentage_opened:.2f}% do tempo total do vídeo.")

    pontos = 0
    if percentage_opened >= 50 and percentage_opened < 90:
        pontos += 30
    elif percentage_opened >= 90: 
        pontos += 50 
    else:
        print("Tempo assistido não suficiente para ganhar pontos.")

    if pontos > 0:
        print(f"Você ganhou {pontos} pontos!")
        atualizar_saldo(email, pontos)

if __name__ == "__main__":
    while True:
        email = input("Digite seu email: ")
        senha = input("Digite sua senha: ")
        
        autenticado, dados_usuario = autenticar_usuario(email, senha)
        
        if autenticado:
            print("Autenticação bem-sucedida!")
            break
        else:
            print("Email ou senha incorretos. Tente novamente.")

    # Lista de vídeos disponíveis e seus tempos totais em segundos
    # Faça download da pasta de vídeos pelo link (https://drive.google.com/drive/folders/1oPdIkWW8FHsU-LJ1FJja9chVKgqg60WS?usp=sharing) e altere o caminho de acordo com o da sua máquina.
    videos = {
        "1": ("videos/vídeo01.mp4", 222),
        "2": ("videos/vídeo02.mp4", 431),
        "3": ("videos/vídeo03.mp4", 130)
    }
    
    # Mostra as opções para o usuário
    print("Escolha um vídeo para abrir:")
    for key, value in videos.items():
        print(f"{key}: {value[0]} (duração: {value[1]} segundos)")

    # Recebe a escolha do usuário
    choice = input("Digite o número do vídeo que você deseja abrir: ")
    
    # Obtém o caminho e o tempo total do vídeo escolhido
    video_info = videos.get(choice)
    
    if video_info:
        video_path, total_time_video = video_info
        main(video_path, total_time_video)
    else:
        print("Escolha inválida.")
