import sentencepiece as spm

# Treinando o modelo para tokenização de subpalavras
texto_exemplo = "O cachorro grande corre rápido."
with open('texto.txt', 'w', encoding='utf-8') as f:
    f.write(texto_exemplo)

# Treina um modelo de subpalavras
spm.SentencePieceTrainer.train(input='texto.txt', model_prefix='modelo_subpalavras', vocab_size=20)

# Carrega o modelo treinado
sp = spm.SentencePieceProcessor(model_file='modelo_subpalavras.model')

# Tokeniza o texto em subpalavras
tokens_subpalavras = sp.encode_as_pieces(texto_exemplo)

print(tokens_subpalavras)

