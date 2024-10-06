import re

# Frase de exemplo
texto = "O preço do produto é R$ 100,00! Disponível a partir de 10/10/2023."

# Definindo o padrão de expressão regular para capturar apenas palavras
padrao = r'\b\w+\b'

# Tokenização com expressão regular
tokens = re.findall(padrao, texto)

print("Tokens encontrados:", tokens)


# Modificando o padrão para ignorar números
padrao_sem_numeros = r'\b[a-zA-Z]+\b'

# Tokenização ignorando números
tokens_sem_numeros = re.findall(padrao_sem_numeros, texto)

print("Tokens sem números:", tokens_sem_numeros)
