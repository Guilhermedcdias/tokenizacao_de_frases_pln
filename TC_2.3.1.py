import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize

texto = "O cachorro grande corre rápido."
tokens_palavras = word_tokenize(texto)

print(tokens_palavras)
