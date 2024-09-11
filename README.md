# Formula E Application

## Introdução

Este projeto inclui três scripts que engajam os usuários com corridas de Fórmula E. O primeiro módulo é para cadastro de usuários, com criação de contas e códigos de divulgação para saldo inicial. O segundo módulo simula um jogo de palpites, permitindo que os usuários ganhem pontos com base nas suas previsões sobre os corredores. O terceiro módulo atribui pontos por assistir vídeos das corridas. Os pontos são armazenados em um banco de dados e poderão ser usados para resgatar itens em uma loja virtual desenvolvida em uma aplicação React.

---

## Código 1: `cadastro_usuario.py`

### Funcionalidade
- Criação de cadastro de usuários.
- Geração de códigos únicos de divulgação para cada usuário.
- Verificação de códigos de divulgação para saldo inicial.

### Dependências
- `csv`: Para manipulação de arquivos CSV.
- `random`: Para gerar códigos aleatórios.
- `string`: Para manipulação de strings.
- `os`: Para verificação de existência de arquivos.
- `mysql.connector`: Para integração com o banco de dados MySQL.

### Como Executar
1. Execute o script `cadastro_usuario.py`.
2. Digite o email e senha para criar um novo usuário.
3. Confirme o email e a senha.
4. (Opcional) Insira um código de divulgação para ganhar saldo inicial. Caso possua um código de divulgação, seu saldo será atualizado no banco de dados MySQL.
5. O usuário será cadastrado e as informações serão salvas no banco de dados MySQL.

---

## Código 2: `e-game.py`

### Funcionalidade
- Simulação de ganho de pontos por palpites em corredores de Fórmula E.
- Cálculo de pontos baseados na colocação e atividades dos corredores.
- Autenticação de usuários.
- Atualização do saldo do usuário com base nos palpites.

### Dependências
- `csv`: Para manipulação de arquivos CSV.
- `mysql.connector`: Para integração com o banco de dados MySQL.

### Como Executar
1. Execute o script `e-game.py`.
2. Digite seu email e senha para autenticar.
3. Se autenticado, visualize seu saldo atual.
4. Faça seus palpites selecionando três corredores.
5. O saldo será atualizado com base nos resultados dos palpites no banco de dados MySQL.

---

## Código 3: `pontuar_assistindo.py`

### Funcionalidade
- Sistema de pontos por assistir vídeos de corridas de Fórmula E.
- Autenticação de usuários.
- Reprodução de vídeos e cálculo de pontos baseados no tempo assistido.

### Dependências
- `cv2` (OpenCV): Para reprodução de vídeos.
- `time`: Para medir o tempo de reprodução.
- `os`: Para verificação de existência de arquivos.
- `csv`: Para manipulação de arquivos CSV.
- `mysql.connector`: Para integração com o banco de dados MySQL.

### Como Executar
1. Faça download da pasta de vídeos no diretório pelo [link](https://drive.google.com/drive/folders/1oPdIkWW8FHsU-LJ1FJja9chVKgqg60WS?usp=sharing) e altere o caminho de acordo com o da sua máquina.
2. Execute o script `pontuar_assistindo.py`.
3. Digite seu email e senha para autenticar.
4. Escolha um vídeo para assistir.
5. Assista ao vídeo. Feche o vídeo pressionando 'q'.
6. O tempo assistido será calculado e os pontos serão atualizados no saldo do usuário no banco de dados MySQL.

---

## Integrantes
- Arthur Abonizio, RM: 555506
- Steffany Medeiros, RM: 556262
- Milena Garcia, RM: 555111
- Enzo Dias, RM: 558225
- Gustavo Henrique, RM: 556712

