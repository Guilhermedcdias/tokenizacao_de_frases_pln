
# TC 2.3
Execução do exercicio PP 2.6 do capitulo 2 do livro do professor Fabricio da aula de PLN.

Para exemplificar o funcionamento de uma tokenização por palavras utilizando expressões regulares, foi utilizado o Regular Expression (re).

> Veja o arquivo ```PP_2.6.py``` para saber em detalhes o codigo...


No exemplo foi tokenizado uma frase de duas formas diferentes, a primeira: dividindo-a em palavras, mas ignorando números e caracteres especiais.


Foi utilizado o seguinte regex: ```'\b\w+\b'```, que captura qualquer sequência de caracteres alfanuméricos que esteja delimitada por espaços ou pontuações.

- \b: Representa uma borda de palavra.
- \w+: Representa uma ou mais letras ou números.`

Dessa forma obtemos o seguinte resultado:

``` bash
['O', 'preço', 'do', 'produto', 'é', 'R', '100', '00', 'Disponível', 'a', 'partir', 'de', '10', '10', '2023']
```

E se quisessemos modificar o comportamento do tokenizador, por exemplo, para ignorar números, podemos ajustar a expressão regular da seguinte forma: ```'\b[a-zA-Z]+\b'```. dessa forma fariamos com que sejam capturadas palavras compostas exclusivamente por letras do alfabeto (tanto maiúsculas quanto minúsculas) e que estejam delimitadas por bordas de palavras (como espaços, pontuações ou início/fim da linha).

- \b: Representa uma borda de palavra.
- [a-zA-Z]+: Representa uma ou mais letras do alfabeto.

Dessa forma obtemos o seguinte resultado:

``` bash
['O', 'do', 'produto', 'R', 'a', 'partir', 'de']
```

## Outros Possiveis Regex

- \b\w+\b
Descrição: Captura palavras formadas por letras, números ou sublinhados.
Exemplo: "palavra_exemplo", "123", "texto".

- \b[a-zA-Z]+\b
Descrição: Captura apenas palavras formadas por letras, ignorando números e símbolos.
Exemplo: "cachorro", "palavra".

- \b\d+\b
Descrição: Captura números inteiros no texto.
Exemplo: "123", "2024".

- \b\d{4}\b
Descrição: Captura exatamente quatro dígitos, útil para anos ou códigos de 4 dígitos.
Exemplo: "2024", "1990".

- \d{1,3}(?:,\d{3})*
Descrição: Captura números grandes formatados com vírgulas.
Exemplo: "1,000", "100,000".

- [A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}
Descrição: Captura endereços de e-mail válidos.
Exemplo: "email@exemplo.com".

- \b[0-9A-Fa-f]{6}\b
Descrição: Captura códigos hexadecimais de 6 dígitos.
Exemplo: "#FFAABB", "00FF00".

- \b\d{1,2}/\d{1,2}/\d{4}\b
Descrição: Captura datas no formato dia/mês/ano.
Exemplo: "12/10/2024", "1/1/1990".

- \b(?:http|https):\/\/[^\s]+
Descrição: Captura URLs que começam com http ou https.
Exemplo: "https://example.com".

- <[^>]+>
Descrição: Captura tags HTML.
Exemplo: <div>, <p>.