# Formula E Application

## Introdução

Este projeto consiste em três códigos voltados para o cadastro de usuários, simulação de jogo de ganho de pontos por palpites em corredores e sistema de pontos por assistir vídeos de corridas de Fórmula E. O intuito é engajar os usuários em atividades relacionadas às corridas de Fórmula E, oferecendo um sistema de pontos baseado em suas interações e participação. Em breve, os usuários poderão utilizar os pontos para resgatar itens em uma loja virtual. Além disso, todo o sistema será integrado com um front-end, proporcionando uma visualização intuitiva e aprimorada dos sistemas.

---

## Código 1: `cadastro_usuario.py`

### Funcionalidade
- Criação de cadastro de usuários.
- Geração de códigos únicos para cada usuário.
- Verificação de códigos de divulgação para saldo inicial.

### Dependências
- `csv`: Para manipulação de arquivos CSV.
- `random`: Para gerar códigos aleatórios.
- `string`: Para manipulação de strings.
- `os`: Para verificação de existência de arquivos.

### Como Executar
1. Execute o script `cadastro_usuario.py`.
2. Digite o email e senha para criar um novo usuário.
3. Confirme o email e a senha.
4. (Opcional) Insira um código de divulgação para ganhar saldo inicial, caso possua um código de divulgação seu saldo sera atualizado em `transacoes.csv`.
5. O usuário será cadastrado e as informações serão salvas nos arquivos `usuarios.csv` e `transacoes.csv`.

---

## Código 2: `e-game.py`

### Funcionalidade
- Simulação de ganho de pontos por palpites em corredores de Fórmula E.
- Cálculo de pontos baseados na colocação e atividades dos corredores.
- Autenticação de usuários.
- Atualização do saldo do usuário com base nos palpites.

### Dependências
- `csv`: Para manipulação de arquivos CSV.

### Como Executar
1. Execute o script `e-game.py`.
2. Digite seu email e senha para autenticar.
3. Se autenticado, visualize seu saldo atual.
4. Faça seus palpites selecionando três corredores.
5. O saldo será atualizado com base nos resultados dos palpites em `transacoes.csv`.

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
- Faça download da pasta de vídeos no diretório pelo [link](https://drive.google.com/drive/folders/1oPdIkWW8FHsU-LJ1FJja9chVKgqg60WS?usp=sharing) e altere o caminho de acordo com o da sua máquina. Certifique-se de que as barras estejam voltadas para o lado direito.

### Como Executar
1. Faça download da pasta de vídeos no diretório pelo [link](https://drive.google.com/drive/folders/1oPdIkWW8FHsU-LJ1FJja9chVKgqg60WS?usp=sharing) e altere o caminho de acordo com o da sua máquina.
2. Execute o script `pontuar_assistindo.py`.
3. Digite seu email e senha para autenticar.
4. Escolha um vídeo para assistir.
5. Assista ao vídeo. Feche o vídeo pressionando 'q'.
6. O tempo assistido será calculado e os pontos serão atualizados no saldo do usuário em `transacoes.csv`.


---

## Observações
- **Atualização em Tempo Real**: Futuras melhorias podem incluir análises em tempo real das corridas de Fórmula E e dados de corridas reais.
- **Integração com Banco de Dados**: Potencial migração para banco de dados para eficiência dos dados dos usuários e transações.
- **Melhorias no Front-End**: Integração do sistema com um site e seções necessárias, entre elas a loja virtual para resgatar itens com os pontos ganhos.

---

## Integrantes
- Arthur Abonizio, RM: 555506
- Steffany Medeiros, RM: 556262
- Milena Garcia, RM: 555111
- Enzo Dias, RM: 558225
- Gustavo Henrique, RM: 556712
