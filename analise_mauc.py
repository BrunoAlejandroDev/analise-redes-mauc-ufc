
#* Importacao das bibliotecas
import pandas as pd #? biblioteca para manipulacao e leitura dos dados
import seaborn as sns #? biblioteca para visualizacao estatistica
import matplotlib.pyplot as plt

#* ====== CARREGAR PLANILHA PARA DF E FORMATAR COLUNAS

#* Teste de carregamento da planilha
caminho_planilha = 'C:\\ciencia-de-dados\\projetos\\analise-redes-mauc-ufc\\dados-mauc.csv'
df_dados = pd.read_csv(caminho_planilha)

#* Transformar os valores da coluna data 
df_dados['Data'] = pd.to_datetime(df_dados['Data'], format='%d/%m/%Y')

#* Definir a coluna de data como index dos dados
df_dados.set_index('Data', inplace=True)

#* Mudar nome das ultimas 3 colunas
df_dados = df_dados.rename(columns={'Qtd_Post_Institucional' : 'Post Institucional', 'Quant_Post_Divulgacao': 'Post Divulgacao', 'Quant_Post_Cultural' : 'Post Cultural'})

#* ====== CALCULAR FREQUENCIA E MEDIA DE POSTS E MEDIAS ======

#* Soma total de posts feitos no periodo de coleta
total_posts_feed = df_dados['Qtd_Postagens_Dia'].sum()
# print(f'Quantidade total de posts (Feed): {total_posts_feed}')

#* Media de posts no periodo de coleta
media_posts_feed = df_dados['Qtd_Postagens_Dia'].mean()
# print(f'Media de post/dia (Feed): {media_posts_feed}')

#* Total de posts do tipo carrossel feitos no periodo
total_posts_carrossel = df_dados['Qtd_Post_Carrosel'].sum()

#* Media de posts do tipo carrossel feitos no periodo
total_posts_carrossel = df_dados['Qtd_Post_Carrosel'].mean()

#* Total de posts do tipo foto feitos no periodo
total_posts_foto = df_dados['Qtd_Post_Foto'].sum()

#* Media de posts do tipo foto feitos no periodo
media_posts_foto = df_dados['Qtd_Post_Foto'].mean()

#* Soma total de stories publicados no periodo observado
total_stories_publicados = df_dados['Qtd_Post_Stories'].sum()

#* Media de stories publicados no periodo observado
media_stories_publicados = df_dados['Qtd_Post_Stories'].mean()

#* Soma total de reels publicados no periodo observado
total_reels_publicados = df_dados['Qtd_Post_Reels'].sum()

#* Media total de reels publicados no periodo observado
media_reels_publicados = df_dados['Qtd_Post_Reels'].mean()


#* ====== CALCULAR ENGAJAMENTO TOTAL ======

total_likes = df_dados['Total_Likes_Dia'].sum()
# print(f'\nTotal de likes no periodo observado: {total_likes}')

total_comentarios = df_dados['Total_Comentario_Dia'].sum()
# print(f'\nTotal de comentarios no periodo observado: {total_comentarios}')

total_visualizacoes = df_dados['Total_Visualizacoes_Dia'].sum()
# print(f'\nTotal de visualizaoes no periodo observado: {total_visualizacoes}')

#* ====== VERIFICAR VOZ DA MARCA ======

soma_tipo_conteudo = df_dados[['Post Institucional', 'Post Divulgacao', 'Post Cultural']].sum()
# print(f'\nQuantidade p/ cada tipo de conteudo no periodo observado:\n{soma_tipo_conteudo}')

media_tipo_conteudo = df_dados[['Post Institucional', 'Post Divulgacao', 'Post Cultural']].mean()
# print(f'\nMedia de cada tipo de conteudo no periodo observado:\n{media_tipo_conteudo}')

#* ====== VERIFICAR TAXA DE ATIVIDADE ======

interacao_marca_dias = df_dados['Interacao_Marca'].sum()
conteudo_proprio = df_dados['Conteudo_Proprio'].sum()
conteudo_participativo = df_dados['Conteudo_Participativo'].sum()
dias_ativos = len(df_dados)
# print(f'\nDias com interacao ativa: {interacao_marca_dias} de {dias_ativos}')
# print(f'\nDias com criacao de conteudo proprio: {conteudo_proprio} de {dias_ativos}')
# print(f'\nDias com conteudo participativo: {conteudo_participativo} de {dias_ativos}')

#* ====== CRIACAO DOS GRAFICOS E VISUALIZACOES ======

#* ===== GRAFICO DE PIZZA PARA VOZ DA MARCA =====

#* Configuracao do estilo dos graficos
sns.set_style('whitegrid') 

#* Configuracao das cores a serem usadas
sns.set_palette('pastel')

#* Grafico de pizza: soma_tipo_conteudo (voz da marca)
plt.figure(figsize=(8,8))

plt.pie(
    soma_tipo_conteudo.values, #? define os numeros a serem usados como parametros do grafico
    labels=soma_tipo_conteudo.index, #? define a legenda para cada tipo de conteudo
    autopct='%1.1f%%', #? formata o percentual a ser mostrado no grafico
    startangle=90, #? define como sera mostrado as fatias do grafico 
    wedgeprops={'edgecolor' : 'black'} #? adiciona uma borda para separar cada fatia e define um cor para a borda
)

plt.title('\nVoz da Marca: Distribuição do Tipo de Conteúdo Publicado no Feed')
plt.show()

#* ===== GRAFICO DE BARRAS PARA VISUALIZACAO DE FREQUENCIA DE MIDIA =====

formatos_total = pd.Series({
    'Foto (Feed)' : total_posts_foto,
    'Reels (Feed)' : df_dados['Qtd_Post_Reels'].sum(),
    'Carrossel (Feed)' : df_dados['Qtd_Post_Carrosel'].sum(),
    'Stories' : df_dados['Qtd_Post_Stories'].sum()
})

plt.figure(figsize=(10,6))

formatos_total.plot(
    kind='bar',
    color=['skyblue', 'salmon', 'lightgreen', 'gold']
)

plt.title('Frequencia de Publicação por Formato de Mídia (8 Dias)')
plt.ylabel('Quantidade Total de Posts')
plt.xlabel('Formato de Mídia')
plt.xticks(rotation=0)
plt.show()

#* ===== GRAFICO DE LINHA PARA VISUALIZACAO DA QUANTIDADE DE SEGUIDORES =====

#* Definir o tamanho do grafico
plt.figure(figsize=(10,6))

#* Plotar a figura 'Qtd_Seguidores' 
df_dados['Qtd_Seguidores'].plot(
    kind='line',
    marker='o', #? adiciona um circulo para cada ponto de dado
    color='darkviolet' #? cor escolhida para a linha no grafico
)

plt.title('Evolução Diária do Número de Seguidores (MAUC)')
plt.ylabel('Quantidade de Seguidores')
plt.xlabel('Data da Observação')
plt.grid(True) #? adiciona linhas de grade
plt.show()