# %%
import pandas as pd
import seaborn as sns
# %%
tmdb = pd.read_csv('tmdb_5000_movies.csv')
tmdb.head()
# %%
# Gerando informações descritivas do conjunto de dados
tmdb.describe()
# %%
# Plotando um histograma normalizado da variável vote_average
ax = sns.distplot(tmdb.vote_average)
ax.set(xlabel='Nota Média', ylabel='Densidade')
ax.set_title('Média de votos em filmes do TMDB 5000')
# %%
# O mesmo histograma sem normalização
ax = sns.distplot(tmdb.vote_average, norm_hist=False, kde=False)
ax.set(xlabel='Nota Média', ylabel='Frequência')
ax.set_title('Média de votos em filmes do TMDB 5000')
# %%
# Plotando um boxplot da mesma variável
ax = sns.boxplot(x=tmdb.vote_average)
ax.set(xlabel='Nota média do filme')
ax.set_title('Distribuição de nota média dos filmes do TMDB 5000')
# %%
# Buscando os filmes cuja a média de notas é igual a zero
tmdb.query('vote_average == 0')
# %%
# Criando uma dataset com número de votantes maior ou igual a 10
tmdb_com_mais_de_10_votos = tmdb.query('vote_count >= 10')
tmdb_com_mais_de_10_votos.describe()
# %%
# Plotando o histograma para o novo conjunto de dados
ax = sns.distplot(tmdb_com_mais_de_10_votos.vote_average, norm_hist=False, kde=False)
ax.set(xlabel='Nota Média', ylabel='Frequência')
ax.set_title('Média de votos em filmes do TMDB 5000')
# %%
# Plotando o histograma normalizado
ax = sns.distplot(tmdb_com_mais_de_10_votos.vote_average)
ax.set(xlabel='Nota Média', ylabel='densidade')
ax.set_title('Média de votos em filmes do TMDB 5000')
# %%
# Plotando um boxplot da mesma variável
ax = sns.boxplot(x=tmdb_com_mais_de_10_votos.vote_average)
ax.set(xlabel='Nota média do filme')
ax.set_title('Distribuição de nota média dos filmes do TMDB 5000')
# %%
# Carregando dados do movielens
notas = pd.read_csv('ratings.csv')
notas.head()
# %%
# Fazendo um groupby das média das notas por fime
nota_media_por_filme = notas.groupby("movieId").mean()["rating"]
nota_media_por_filme.head()
# %%
# Plotando o histograma do movielens média de notas
ax = sns.distplot(nota_media_por_filme.values)
ax.set(xlabel='Nota Média', ylabel='densidade')
ax.set_title('Média de votos em filmes do Movielens')
# %%
quantidade_de_votos_por_filmes = notas.groupby("movieId").count()
filmes_com_pelo_menos_10_votos = quantidade_de_votos_por_filmes.query("rating >= 10").index
filmes_com_pelo_menos_10_votos.values
# %%
nota_media_dos_filmes_com_pelo_menos_10_votos = nota_media_por_filme.loc[filmes_com_pelo_menos_10_votos.values]
# %%
ax = sns.distplot(nota_media_dos_filmes_com_pelo_menos_10_votos.values)
ax.set(xlabel='Nota Média', ylabel='densidade')
ax.set_title('Média de votos em filmes do Movielens com pelo menos 10 votos')
# %%
ax = sns.boxplot(x=nota_media_dos_filmes_com_pelo_menos_10_votos.values)
ax.set(xlabel='Nota média do filme')
ax.set_title('Distribuição de nota média dos filmes do movielens com mais de 10 votos')
# %%
# Histograma com a quantidade acumulada de filmes
ax = sns.distplot(nota_media_dos_filmes_com_pelo_menos_10_votos.values,
                  hist_kws={'cumulative':True},
                  kde_kws={'cumulative':True})
ax.set(xlabel='Nota Média', ylabel='% Acumulada de filmes')
ax.set_title('Média de votos em filmes do Movielens com pelo menos 10 votos')
# %%
# Analisando a distribuição dos dados capturados de outros campos do TMDB
tmdb_com_mais_de_10_votos.vote_count

ax = sns.distplot(tmdb_com_mais_de_10_votos.vote_count)
ax.set(xlabel='Número de Votos', ylabel='densidade')
ax.set_title('Número de votos em filmes no TMDB 5000 com 10 ou mais votos')

# %%
# Para variável orçamento
ax = sns.distplot(tmdb.query('budget > 0').budget)
ax.set(xlabel='Budget (Gastos)', ylabel='densidade')
ax.set_title('Gastos em filmes no TMDB 5000 com 10 ou mais votos')
# %%
ax = sns.distplot(tmdb.popularity)
ax.set(xlabel='Popularidade', ylabel='densidade')
ax.set_title('Popularidade de filmes no TMDB 5000 com 10 ou mais votos')
# %%
tmdb.runtime.isnull().sum()
# %%
ax = sns.distplot(tmdb.query('runtime > 0').runtime.dropna())
ax.set(xlabel='Tempo de Duração', ylabel='densidade')
ax.set_title('Tempo de Duração de filmes no TMDB 5000 com 10 ou mais votos')
# %%
ax = sns.distplot(tmdb.query('runtime > 0').runtime.dropna(),
                  hist_kws={'cumulative':True},
                  kde_kws={'cumulative':True})
ax.set(xlabel='Tempo de Duração', ylabel=" '%' de filmes")
ax.set_title('Tempo de Duração de filmes no TMDB 5000 com 10 ou mais votos')
# %%
# Qual o runtime que representa o 20%
tmdb.query('runtime > 0').runtime.dropna().quantile(0.8)
# %%
