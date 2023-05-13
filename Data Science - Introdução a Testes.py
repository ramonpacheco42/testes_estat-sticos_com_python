# %%
import pandas as pd
import seaborn as sns
# %%
tmdb = pd.read_csv('Data/tmdb_5000_movies.csv')
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
notas = pd.read_csv('Data/ratings.csv')
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
# Movielens: média dos filmes com pelo menos 10 votos
nota_media_dos_filmes_com_pelo_menos_10_votos.mean()
# %%
nota_media_dos_filmes_com_pelo_menos_10_votos[0:5].mean()
# %%
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(75243)
temp = nota_media_dos_filmes_com_pelo_menos_10_votos.sample(frac=1)

medias = [temp[0:i].mean() for i in range(1, len(temp))]
    
plt.plot(medias)
# %%
# Achando o intervalo de confiança
from statsmodels.stats.weightstats import zconfint, DescrStatsW
# %%
# ztest para amostra maior que 30 elementos
zconfint(nota_media_dos_filmes_com_pelo_menos_10_votos)
# %%
# ttest para amostra com mais de 30 elementos
desc_todos_com_10_votos = DescrStatsW(nota_media_dos_filmes_com_pelo_menos_10_votos)
desc_todos_com_10_votos.tconfint_mean()
# %%
# Olhando apenas para um filme e comparando com o total
filmes = pd.read_csv('Data/movies.csv')
filmes.query("movieId==1")
# %%
notas1 = notas.query("movieId == 1")
notas1.head()
# %%
ax = sns.distplot(notas1.rating)
ax.set(xlabel="Nota", ylabel="Densidade")
ax.set_title("Distribuição das notas para o Toy Story")
# %%
ax = sns.boxplot(notas1.rating, orient='h')
ax.set(xlabel="Nota")
ax.set_title("Distribuição das notas para o Toy Story")
# %%
notas1.rating.mean()
# %%
notas1.rating.count()
# %%
zconfint(notas1.rating)
# %%
from statsmodels.stats.weightstats import ztest
ztest(notas1.rating, value= 3.4320503405352594)
# Conclusão é que a média do filme Toy Story é diferente das médias de todos os filmes.
# %%
# Entendo porque se usa o zteste apenas para amostras > 30
np.random.seed(75241)
temp = notas1.sample(frac=1).rating

def calcula_teste(i):
    media = temp[0:i].mean()
    stat, p = ztest(temp[0:i], value = 3.4320503405352594)
    return (i, media, p)

valores = np.array([calcula_teste(i) for i in range(2, len(temp))])
plt.plot(valores[:,0],valores[:,1])
plt.plot(valores[:,0], valores[:,2], color='green')
plt.hlines(y=0.05, xmin = 2, xmax= len(temp), color='red')
# %%
# Verificando quanto a média de notas1.rating é maior que de notas.rating
print(ztest(notas1.rating, notas.rating))
zconfint(notas1.rating, notas.rating)
# %%
# Aplicando diretamente o T-Teste
from scipy.stats import ttest_ind
ttest_ind(notas.rating, notas1.rating)
# %%
from statsmodels.stats.weightstats import CompareMeans
descr_todas_as_notas = DescrStatsW(notas.rating)
descr_toystory = DescrStatsW(notas1.rating)
comparacao = descr_todas_as_notas.get_compare(descr_toystory)
# %%
# P-Test
comparacao.summary()
# %%
# T-Test
comparacao.summary()
# %%
import matplotlib.pyplot as plt

plt.boxplot([notas.rating,notas1.rating], labels=['Todas as Notas','Toy Story'],vert=False)
plt.title('Distribuição dos dados')
# %%
descr_todas_as_notas = DescrStatsW(notas.rating)
descr_toystory = DescrStatsW(notas1[3:12].rating)
comparacao = descr_todas_as_notas.get_compare(descr_toystory)
comparacao.summary(use_t=True)
# %%
# Comparando a média de dois filmes
filmes.query("movieId in [1,593,72226]")
# %%
# Plotando o Boxsplot
sns.boxplot(x='movieId', y='rating', data = notas.query('movieId in (1,593,72226)'))
# %%
notas1 = notas.query('movieId == 1')
notas593 = notas.query('movieId == 593')
notas72226 = notas.query('movieId == 72226')

# Realizando o teste estátistico P-Value entre as médias das variáveis notas1 e notas 593
descr_1 = DescrStatsW(notas1.rating)
descr_593 = DescrStatsW(notas593.rating)
comparacao = descr_1.get_compare(descr_593)
comparacao.summary()
# Conlusão:  O teste aceita a hipotese que existe uma diferença estatística entre as duas variáveis
# %%
# Realizando o teste estátistico P-Value entre as médias das variáveis notas 72226 e notas 593
descr_72226 = DescrStatsW(notas72226.rating)
descr_593 = DescrStatsW(notas593.rating)
comparacao = descr_72226.get_compare(descr_593)
comparacao.summary()
# Conclusão: O teste rejeita a hipotese que existe uma diferença estatísticamente comprovada entre as duas variáveis
# %%
comparacao = descr_1.get_compare(descr_72226)
comparacao.summary()
# Conclusão: O teste rejeita a hipotese que existe uma diferença estatísticamente comprovada entre as duas variáveis
# %%
notas.query('movieId in (1, 593, 72226)').groupby('movieId').count()
# %%
descr_1 = DescrStatsW(notas1.rating)
descr_593 = DescrStatsW(notas593.rating)
comparacao = descr_1.get_compare(descr_593)
comparacao.summary(use_t=True)
# %%
descr_72226 = DescrStatsW(notas72226.rating)
descr_593 = DescrStatsW(notas593.rating)
comparacao = descr_72226.get_compare(descr_593)
comparacao.summary(use_t=True)
# %%
comparacao = descr_1.get_compare(descr_72226)
comparacao.summary(use_t=True)
# %%
x = np.array([245, 255, 280, 290, 900,
     190, 230, 140, 874, 899,
     300, 255, 176, 188, 190,
     300, 600, 1200, 1300, 1000,
     800, 130, 120, 140, 150,190,
     1200, 640, 550, 820, 310, 330,
     1020, 210, 198, 188, 132, 155,
     151, 130, 1200, 1201, 113, 140,
     120, 230, 410, 130, 140, 140,
     130, 250, 240, 512, 1240, 1155])
y = np.array([444,551,235,350,413,415,135,
     560,213,350,353,123,556,123,1300,4111,
     140,311,562,143,521,1235,135,256,266,
     343,435,123,1235,331,315,451,12323,31231,313123,31231])
# %%
descr_72226 = DescrStatsW(x)
descr_593 = DescrStatsW(y)
comparacao = descr_72226.get_compare(descr_593)
comparacao.summary()
# %%
from scipy.stats import normaltest
_, p = normaltest(notas1.rating)
p
# %%
# Testes Não parametricos que não exige distribuição normal.
from scipy.stats import ranksums
_, p = ranksums(notas1.rating, notas593.rating)
p
# %%
_, p = ranksums(x,y)
p
# %%
