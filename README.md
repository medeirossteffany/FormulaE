# FormulaE 

## Introdução

Este projeto inclui quatro scripts que engajam os usuários com a FórmulaE. O primeiro módulo é para cadastro de usuários, com criação de contas e códigos de divulgação para ganhar saldo. O segundo módulo simula um jogo de palpites, permitindo que os usuários ganhem pontos com base nas suas previsões sobre os corredores. O terceiro módulo atribui pontos por assistir vídeos das corridas. O quarto módulo realiza a análise de dados das corridas da Fórmula E utilizando um arquivo CSV. Os pontos ganhos nos jogos são armazenados em um banco de dados MYSQL e poderão ser usados para resgatar itens em uma loja virtual desenvolvida em uma aplicação React.

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

## Código 4: `analise_dados.py`

### Funcionalidade
- Análise de dados de corridas de Fórmula E com base em um arquivo CSV com dados ficticios para simularmos.
- Realiza análises descritivas gerais e por equipe.
- Gera gráficos de desempenho das equipes com base na média de pontos.
- Utiliza funções aninhadas e lambdas para modularizar e simplificar o código.

### Dependências
- `pandas`: Para manipulação e análise de dados do arquivo CSV.
- `matplotlib`: Para gerar gráficos de desempenho.
- `csv`: Para manipulação de arquivos CSV.

### Como Executar
1. Execute o script `analise_dados.py`.
2. Escolha o tipo de análise:
   - 'basica': Mostra uma análise descritiva geral dos dados.
   - 'equipe': Mostra uma análise detalhada de pontuação por equipe.
   - 'grafico': Gera um gráfico de barras mostrando o desempenho das equipes com base nos pontos médios.

---

## Integrantes
- Arthur Abonizio, RM: 555506
- Steffany Medeiros, RM: 556262
- Milena Garcia, RM: 555111
- Enzo Dias, RM: 558225

