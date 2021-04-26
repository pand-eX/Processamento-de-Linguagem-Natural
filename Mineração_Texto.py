#biblioteca
import matplotlib.pyplot as plt
import nltk
nltk.download("stopwords")
from nltk.corpus import PlaintextCorpusReader
from nltk.corpus import stopwords
from matplotlib.colors import ListedColormap
from wordcloud import wordcloud
import string

# Criação de um corpus lendo textos do disco
corpus = PlaintextCorpusReader('Arquivos', '.*', encoding = "ISO-8859-1")

# Leitura dos arquivos do disco, percorrer os registros e mostrar o nome dos primeiros 100 arquivos
arquivos = corpus.fileids()
#primeiro arquivo
arquivos[0]

#zero a 10
arquivos[0:10]

#imprime todos os nomes
for a in arquivos:
    print(a)

# Acesso ao texto do primeiro arquivo
texto = corpus.raw('1.txt')
texto

# Acesso a todos as palavras de todos os arquivos do corpus
todo_texto = corpus.raw()
todo_texto

# Obtenção de todas as palavras do corpus e visualização da quantidade
palavras = corpus.words()
#acessando pelo indíce
palavras[170]

#quantidade
len(palavras)

# Usando o NLTK, obtemos as stop word em inglês
stops = stopwords.words('english')
#stops = stopwords.words('portuguese')
stops

# Definição das cores que serão utilizadas na nuvem de palavras
mapa_cores = ListedColormap(['orange', 'green', 'red', 'magenta'])
# Criação da nuvem de palavras, com no máximo 100 palavras e utilizando as stop words
nuvem = WordCloud(background_color = 'white',
                  colormap = mapa_cores,
                  stopwords = stops,
                  max_words = 100)
# Criação e visualização da nuvem de palavras
nuvem.generate(todo_texto)
plt.imshow(nuvem)

# Criação de nova lista de palavras, removendo stop words
palavras_semstop = [p for p in palavras if p not in stops]
len(palavras_semstop)

# Remoção da pontuação, gerando uma lista sem stop words e sem pontuação
palavras_sem_pontuacao = [p for p in palavras_semstop if p not in string.punctuation]
len(palavras_sem_pontuacao)

# Cálculo da frequência das palavras e visualização das mais comuns
frequencia = nltk.FreqDist(palavras_sem_pontuacao)
frequencia

#mais comuns
mais_comuns = frequencia.most_common(100)
mais_comuns