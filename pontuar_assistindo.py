import cv2
import time
import os
import csv

# Necessário clicar 'q' para fechar o video escolhido 
# Necessário cadastrar email e senha existentes no arquivo usuarios.csv para conseguir prosseguir o programa


# Código feito com o intuito de reter usuarios a assistir as corridas de formulaE 
# Código responsável pelo ganho de pontos por assistir corridas de formulaE

# Função para autenticar o usuário a partir de um arquivo CSV
def autenticar_usuario(email, senha):
    with open('usuarios.csv', 'r', newline='') as arquivo:
        leitor_csv = csv.DictReader(arquivo)
        for linha in leitor_csv:
            if linha['EMAIL'] == email and linha['SENHA'] == senha:
                return True, linha
    return False, None

# Função para atualizar o saldo do usuário no arquivo CSV
def atualizar_saldo(email, pontos):
    with open('transacoes.csv', 'r', newline='') as arquivo:
        leitor_csv = csv.DictReader(arquivo)
        transacoes = list(leitor_csv)

    for transacao in transacoes:
        if transacao['EMAIL'] == email:
            saldo_atual = int(transacao['SALDO'])
            saldo_atual += pontos
            transacao['SALDO'] = str(saldo_atual)
            break

# Abre o arquivo 'transacoes.csv' no modo de escrita para salvar as alterações
    with open('transacoes.csv', 'w', newline='') as arquivo:
        escritor_csv = csv.DictWriter(arquivo, fieldnames=['EMAIL', 'SALDO'])
        escritor_csv.writeheader()
        escritor_csv.writerows(transacoes)

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

    # Define o FPS desejado
    desired_fps = 30

    # Define o tempo entre frames com base no FPS desejado
    frame_time = 1 / desired_fps

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

            # Aguarda o tempo entre frames
            time.sleep(frame_time)

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
    print(f"o video ficou aberto {percentage_opened:.2f}% do tempo total do vídeo.")

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
    videos = {
        "1": ("C:/Users/AngeloFerreira/Desktop/Formula_E_application/Formula_E_Application/videos/vídeo03.mp4", 222),
        "2": ("C:/Users/AngeloFerreira/Desktop/Formula_E_application/Formula_E_Application/videos/vídeo02.mp4", 431),
        "3": ("C:/Users/AngeloFerreira/Desktop/Formula_E_application/Formula_E_Application/videos/vídeo03.mp4", 130)
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



