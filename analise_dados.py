import pandas as pd
import matplotlib.pyplot as plt

# Em aula, aprendemos introdução à análise de dados.
# Criamos uma estrutura com funções dentro de funções para retornar análises ao usuário.
# Usamos Pandas, Matplotlib e lambda para processar e visualizar os dados.
# Os dados são fictícios, utilizados para demonstrar o conhecimento adquirido em aula.

# Carregar os dados do CSV
df = pd.read_csv('formula_e_data.csv')

# Função principal que chama outras funções de análise
def analisar_dados(df):
    
    # Função para análise básica
    def analise_basica():
        # Exibe uma análise descritiva básica do DataFrame, incluindo estatísticas como:
        # - Média
        # - Desvio Padrão
        # - Mínimo e Máximo
        # Essa análise ajuda a entender rapidamente a distribuição e a amplitude dos valores nas diferentes colunas.
        print("\nAnálise Descritiva Básica Geral:")
        print(df.describe())  # Exibe estatísticas descritivas de todas as colunas numéricas.
    
    # Função para análise por equipe
    def analise_por_equipe():
        # Agrupa os dados por equipe e realiza uma análise de:
        # - Pontuação média
        # - Pontuação máxima
        # - Pontuação mínima
        # O objetivo aqui é entender o desempenho das diferentes equipes ao longo das corridas.
        
        # Usando lambda para encontrar o maior e menor valor de pontuação por equipe
        df['Pontos Máximos'] = df.groupby('Equipe')['Pontos'].transform(lambda x: x.max())
        df['Pontos Mínimos'] = df.groupby('Equipe')['Pontos'].transform(lambda x: x.min())
        
        # Agrupamento e resumo
        resumo_equipes = df.groupby('Equipe').agg({
            'Pontos': ['mean', 'sum'],          # Média e soma dos pontos por equipe
            'Pontos Máximos': ['max'],          # Pontuação máxima por equipe
            'Pontos Mínimos': ['min']           # Pontuação mínima por equipe
        })
        
        # Exibindo os dados
        print("\nAnálise por Equipe (Média, Máximo e Mínimo dos Pontos):")
        print(resumo_equipes)  # Exibe a tabela resumida das estatísticas por equipe.
    
    # Função para gerar gráfico de desempenho das equipes
    def gerar_grafico():
        # Gera um gráfico de barras mostrando o desempenho das equipes, baseado nos pontos médios.
        # Esse gráfico permite uma visualização rápida para comparar as performances das equipes.
        
        # Usando lambda para calcular a média de pontos por equipe
        df['Pontos Médios'] = df.groupby('Equipe')['Pontos'].transform(lambda x: x.mean())
        
        # Criar gráfico de barras
        plt.figure(figsize=(10, 6))
        df.groupby('Equipe')['Pontos Médios'].mean().sort_values().plot(kind='bar', color='blue')
        plt.title('Desempenho das Equipes (Pontos Médios)')
        plt.xlabel('Equipe')
        plt.ylabel('Pontos Médios')
        plt.xticks(rotation=45)

        # Adicionar rótulos aos valores no gráfico
        for index, value in enumerate(df.groupby('Equipe')['Pontos Médios'].mean().sort_values()):
            plt.text(index, value, round(value, 2), ha='center', va='bottom')

        plt.show()

    # Função para lidar com escolha do usuário e garantir input válido
    def escolha_usuario():
        # Solicita ao usuário que escolha o tipo de análise:
        # - 'basica': Para análise descritiva geral
        # - 'equipe': Para análise detalhada por equipe
        # - 'grafico': Para visualizar o gráfico de desempenho das equipes
        while True:
            tipo_analise = input("\nEscolha o tipo de análise: 'basica', 'equipe', ou 'grafico': ").lower()
            if tipo_analise in ['basica', 'equipe', 'grafico']:
                return tipo_analise
            else:
                print("Escolha inválida. Tente novamente com: 'basica', 'equipe', ou 'grafico'.")

    # Chamar função correta com base no input
    tipo_analise = escolha_usuario()
    
    if tipo_analise == 'basica':
        analise_basica()
    elif tipo_analise == 'equipe':
        analise_por_equipe()
    elif tipo_analise == 'grafico':
        gerar_grafico()

# Chamar a função principal para análise
analisar_dados(df)


