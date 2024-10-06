
# TC 2.3
Execução do exercicio TC 2.3 do capitulo 2 do livro do professor Fabricio da aula de PLN.

Utilizar da Tokenização nos ajuda a dividir o texto em partes menores, e dependendo da forma como fazemos isso, podemos obter diferentes resultados a partir disso diferentes estatisticas...

Para a execução deste exercicio utilizaremos a frase: "O cachorro grande corre rapido".

Utilizaremos 3 tipos de Tokenização para resolução deste exercicio:

- Tokenização por Palavras;
- Tokenização por Caracteres;
- Tokenização por SubPalavras;


Abaixo as resoluções nos 3 tipos de Tokenização:
## Tokenização por palavras


``` bash
["O", "cachorro", "grande", "corre", "rápido."]

```

> Para ver a execução do exercicio veja o arquivo nomeado de `TC_2.3.1.py`

- Essa forma de Tokenização gerou 5 tokens;
- Nesta forma de Tokenização cada palavra ocorre uma vez


## Tokenização por caracteres


``` bash
["O", " ", "c", "a", "c", "h", "o", "r", "r", "o", " ", "g", "r", "a", "n", "d", "e", " ", "c", "o", "r", "r", "e", " ", "r", "á", "p", "i", "d", "o", "."]


```

> Para ver a execução do exercicio veja o arquivo nomeado de `TC_2.3.2.py`

- Essa forma de Tokenização gerou 32 tokens;
- Nesta forma de Tokenização, o caractere "r" aparece 5 vezes, e o espaço (" ") aparece 4 vezes.

## Tokenização por subpalavras


``` bash
["O", "ca", "ch", "orro", " grande", " co", "rre", " rá", "pido", "."]


```

- Essa forma de Tokenização gerou 10 tokens;
- Nesta forma de Tokenização cada subpalavra ocorre uma vez

> Para ver a execução do exercicio veja o arquivo nomeado de `TC_2.3.3.py`, no caso deste exercicio o resultado esperado é diferente do que é gerado pela execução em codigo pois a tokenização por subpalavras, como a usada pelo SentencePiece, divide palavras em pedaços menores chamados subpalavras, para lidar com palavras raras ou desconhecidas e reduzir o tamanho do vocabulário. Essa abordagem identifica fragmentos frequentes no texto e os reutiliza para formar palavras, permitindo maior flexibilidade. O símbolo "▁" indica o início de uma nova palavra ou sequência, resultando em tokens menores e mais eficientes do que palavras inteiras, o que é útil em modelos com vocabulário limitado.



## Finalização

- Palavras: 5 tokens, cada palavra aparece 1 vez.
- Caracteres: 32 tokens, "r" aparece 5 vezes.
- Subpalavras: 10 tokens, cada parte aparece 1 vez.

Diferentes tokenizações resultam em quantidades e frequências diferentes de elementos, o que pode impactar como analisamos e processamos textos.

Ao tokenizar por palavras, as palavras inteiras são os elementos mais importantes. No caso dos caracteres, há mais tokens e a frequência de letras individuais pode ser mais relevante. Com subpalavras, você captura padrões internos das palavras, o que pode ser útil para lidar com palavras desconhecidas ou morfologia complexa.