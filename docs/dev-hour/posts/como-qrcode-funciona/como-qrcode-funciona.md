---
date: 2025-01-01
categories:
    - Eletrônica
tags:
    - QR Code
    - Codificação de Dados
    - Leitura Óptica
---

# Como o QR Code funciona?

Você já percebeu como, em poucos segundos, consegue acessar um cardápio, pagar uma conta ou entrar em um site só apontando a câmera do celular? Aqueles quadradinhos pretos e brancos, que antes pareciam estranhos, hoje estão em todo lugar — e têm um nome: QR Code.

Mas afinal, o que é um QR Code?

QR Code é a sigla para Quick Response Code (código de resposta rápida). Ele é um tipo de código de barras bidimensional, capaz de armazenar informações como links, textos, contatos e até dados para pagamento.

Diferente dos códigos de barras tradicionais (aqueles de supermercado), o QR Code consegue guardar muito mais informação — e de forma muito mais rápida de ser lida.

<figure markdown="span">
![](./img/qrcode_vs_barcode.png){ align=center, width="500"}
</figure>

O inventor foi o engenheiro **Masahiro Hara**, que se inspirou no jogo de tabuleiro *Go* ao criar o padrão visual dos quadradinhos.

Ele trabalhava em uma empresa chamada Denso Wave, subsidiária da Toyota, onde surgiu um problema: as fábricas da Toyota lidavam com milhares de peças diferentes (como parafusos, motores e componentes eletrônicos), cada uma com specs detalhadas em kanji, números e alfanuméricos. Os códigos de barras tradicionais (unidimensionais) eram lentos, armazenavam poucos dados (cerca de 20-25 caracteres), exigiam alinhamento preciso e falhavam em ambientes sujos ou movimentados das linhas de montagem.

E é ai que o Hara entra em cena. Ele projetou o QR para rastrear peças em caixas: uma única etiqueta QR substituía várias etiquetas de barcode, codificando dados de múltiplas peças de uma vez, com capacidade para até 7.000 caracteres.

Como foi um projeto industrial proprietário, não existe um "paper original" acadêmico clássico publicado. No entanto, a documentação técnica primária vem das patentes japonesas da Denso Wave e descrições oficiais no site da empresa:

- [Method for displaying information code and method for reading the information code | JP2004054581A](https://ppl-ai-file-upload.s3.amazonaws.com/patents/fallback/JP2004054581A.pdf?response-content-disposition=inline%3B%20filename%3D%22JP2004054581A.pdf%22&response-content-type=application%2Fpdf&AWSAccessKeyId=ASIA2F3EMEYER5RM2VAO&Signature=jhXiVOHCaHJu9eW02XdZbGb4GCE%3D&x-amz-security-token=IQoJb3JpZ2luX2VjECYaCXVzLWVhc3QtMSJGMEQCIDl2Rrg%2FfXiIU3%2BexVwkncOd1%2B8ECah0vUmpe%2FQO%2By3FAiAEcg%2BuwldRBPXtgRM%2BZnE9rYOK6GLejoS4k%2FJYEJYQtyr8BAjv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAEaDDY5OTc1MzMwOTcwNSIM1djh%2BhyZ8wZanVOwKtAEGVQ3un3kZL4KShI%2BcEsb%2FgJeY9ht2mvARrC7utlOpPAGDl5EjJv5rjgntYbb07jj2oFwLZjUGu%2BCQ52TJm5WxiuLIXbes%2B17ICe4xNl61LjIw3UUlRzPJzqaCxxkD5EF8PBgng7k4LqMSMZkt1sutTzxwjA8QzgyZF8zmUQvjhGa9mif3Jo4fLKBGE8BnWg1g7d3m9aFjquan1WO7QUvIlaoGkzbvo%2BRUcAhaxlU59daI3GaMcyWeSvCyty6HyHHW6mHhVQSx8TGx0V6GYdQu%2Fc%2FkRthkr4m6lE9533IfDu5LOo2ZfMZtQrkvfuxqaDV1NLiMp18294vyu6SEZa1VI67idjWGh6ATj%2FbFaPTW85LG2FnnLWJxn9R9%2BPJcRKf8OWJAz0G%2Fi5XJknfPZje6qxf135qTcJIlpyKtNBwjCtzUJupSW8HlUd3F4q1XpijMAyuBwkYym3rsBHqrINEez7UncipRqGyMA%2FNOEccIWDFDaLYHko20tDkMdLmkDDDgt8TKvAd1Jhzi%2FyJ7Hj3sSUB0uL3oh4dMvmYEj0%2BxGILiaxZKmDdyoplWULkKwV0ulPHAnZmTFgXdGWyb94tNh4aTY35a6P6oFSoCIToZHjjpnF%2BCFBQWWY5YUV9ApTAgQ3JfQhI%2BiAm1LkuT1LhwJmExVQ0kfXQU0EquXmtNs1nI%2FZJfsdc1tbPpijNEAPOm7OSnOhTngeBV6TI%2BE9ERTKx%2FZjFXunrKmGcNA4sSwVhyfh60M4fq2Sb5tMhsmSsBQrbn1ugVaQqvPLkBbC09TDTj47PBjqZAdgFlJ3ti7bDwGY0DrsiXlv%2FSZMJF8Fo14A7eAawA1t2bTmiDkFnFJoGB9PJJOir51%2FbqH%2BHILQJqt3BbVJ0gK77ShovC3Q7kWPLhUNbiGsoc68SxZqVOKZO%2Bzvh01KKY8QfAvtQxeOmh9VGaZWxBWrb1NHYJ75DVKMguskaF1Jr3G1PjmCHf4KduEXwiKV91O9ehwxe9J761A%3D%3D&Expires=1776523785)


- [História de desenvolvimento do QR Code| Denso Wave](https://www.denso-wave.com/en/technology/vol1.html)



A Denso Wave optou por [**não exercer os direitos da patente**](https://www.qrcode.com/en/patent.html), o que permitiu sua adoção global gratuita, apesar de ainda haver patentes. Na prática, é uma situação meio "meio livre, meio controlada". 

Mas afinal, como é possível que um amontoado de quadrados pretos e brancos armazene tanta informação e ainda seja legível mesmo com a tela trincada ou suja?

## 1) Anatomia de um QR Code

O QR Code não é apenas uma imagem aleatória; ele é uma grade (grid) estruturada. Para que um leitor (como a câmera do seu celular) entenda o que está ali, ele não olha para a imagem como um todo, mas sim para padrões geométricos específicos.

Antes de entender *como* ele armazena dados, precisamos entender *o que* compõe visualmente um QR Code. Cada elemento tem uma função específica.

Assim, podemos separar o QR Code nas seguintes partes:

<figure markdown="span">
![](./img/partes_qrcode.webp){ align=center, width="500"}
</figure>


- **Padrões de Busca (Finder Patterns):** São aqueles três quadrados grandes nos cantos (geralmente superior esquerdo, superior direito e inferior esquerdo).

    > Eles permitem que o leitor identifique a orientação do código. Graças a eles, você pode escanear um QR Code de cabeça para baixo ou de lado, e o seu celular ainda vai saber exatamente como "girar" a imagem digitalmente para ler os dados.

- **Padrões de Alinhamento (Alignment Patterns):** Aqueles quadradinhos menores espalhados pelo "corpo" do código (em versões maiores, a partir da Versão 2).

    > Se o código for muito grande (com muitos dados), ele pode sofrer distorções se estiver impresso em uma superfície curva ou se a foto estiver com perspectiva. Esses pontos servem para o software "calibrar" e alinhar a grade, corrigindo possíveis deformações na leitura.

- **Padrões de Temporização (Timing Patterns):** São aquelas linhas de módulos alternados (preto, branco, preto, branco) que conectam os padrões de busca.

    > Eles funcionam como uma "régua". Eles informam ao leitor qual é a densidade da matriz (o tamanho do "pixel" do código) para que o sistema saiba contar quantos módulos existem na linha e na coluna.

- **Zona de Silêncio (Quiet Zone):** Muitos ignoram isso, mas é a parte mais importante para o "início" da leitura. É a margem branca ao redor do código.

    > Sem esse espaço em branco, o leitor não consegue separar o código do restante da imagem (como um rótulo ou papel). Se você colocar um QR Code encostado em uma borda colorida, ele falhará porque o sensor não saberá onde a "mensagem" começa.

- **Célula ou Módulo (Cell):** Se você olhar para um QR Code com bastante zoom, verá que ele é composto por uma grade de pequenos quadrados pretos e brancos. Cada um desses quadrados individuais é chamado de célula ou módulo.

Agora, vamos entender cada um deles de forma mais detalhada tentando entender como um scanner de QR Code funciona. Eles seguem um padrão técnico rigoroso:

1. **Localizando a oritentação:** O scanner de QR code começa reconhecendo os 3 marcadores de posição no QR code para saber a orientação correta da leitura.
2. **Obtendo o Indicador de Modo:** O scanner começa no canto inferior direito, onde encontra o indicador de modo. Esses quatro módulos de dados indicam qual é o tipo de dado (numérico, alfanumérico, byte ou kanji) do restante das informações codificadas.
3. **Obtendo a contagem de caracteres:** Em seguida, o scanner encontra o indicador de contagem de caracteres, que são os próximos 8 módulos de dados acima do indicador de modo. Eles indicam quantos caracteres existem no total de dados codificados.


### 1.1) Os Padrões de Posicionamento

Aqueles três quadrados grandes nos cantos (superior-esquerdo, superior-direito e inferior-esquerdo) são chamados de **padrões de posicionamento** (*finder patterns*). Eles existem para que o leitor consiga identificar:

- Onde está o QR Code na imagem
- Qual é a orientação (o código pode ser lido em qualquer ângulo)
- Qual é o tamanho de cada "célula" (os quadradinhos pretos e brancos)

> Você reparou que o quarto canto nunca tem esse quadrado? É proposital! O leitor usa a ausência do padrão no canto inferior-direito para confirmar que orientou a leitura corretamente.

### 2.2) Os Módulos

Cada quadradinho preto ou branco é chamado de **módulo**. Um módulo preto representa `1` e um branco representa `0`. No fundo, um QR Code é uma grade de bits — uma imagem binária que codifica informação.

O tamanho dessa grade depende da **versão** do QR Code. A versão 1 tem uma grade de 21×21 módulos. A versão 40 (a maior) tem 177×177 módulos. Cada versão aumenta em 4 módulos por lado.

<figure markdown="span">
![](./img/versions_qrcode.png){ align=center, width="500"}
</figure>

| Versão | Tamanho da grade | Capacidade (texto) |
|--------|------------------|--------------------|
| 1      | 21 × 21          | até 17 caracteres  |
| 5      | 37 × 37          | até 64 caracteres  |
| 10     | 57 × 57          | até 174 caracteres |
| 40     | 177 × 177        | até 4.296 caracteres |

-  [Informações sobre capacidade e versões do QR Code | QR Code.com](https://www.qrcode.com/en/about/version.html)

## 2) Como os dados são codificados?

Aqui começa a parte interessante. Para transformar um texto (como uma URL) em uma grade de módulos pretos e brancos, o QR Code passa por uma série de etapas.

### 2.1) Escolha do modo de codificação

O primeiro passo é decidir *como* representar os dados. Existem 4 modos principais:

- **Numérico:** apenas dígitos (0–9). Mais eficiente — armazena 3 dígitos em 10 bits.
- **Alfanumérico:** dígitos + letras maiúsculas + alguns símbolos. Armazena 2 caracteres em 11 bits.
- **Byte:** qualquer caractere UTF-8/ISO-8859-1. O mais flexível, mas menos eficiente.
- **Kanji:** caracteres japoneses. Armazena 1 caractere em 13 bits.

> Na prática, quando você gera um QR Code com uma URL como `https://exemplo.com`, o modo **Byte** é o utilizado, pois URLs contêm letras minúsculas, que não existem no modo alfanumérico.

### 2.2) Correção de Erros — O Superpoder do QR Code

Aqui está um dos aspectos mais fascinantes do QR Code: ele **continua funcionando mesmo que parte dele esteja danificada, coberta ou suja**.

Isso é possível graças a um algoritmo chamado **Reed-Solomon**, desenvolvido em 1960 pelos matemáticos Irving Reed e Gustave Solomon. Ele adiciona dados redundantes ao código, permitindo que o leitor reconstrua as informações perdidas.

Existem 4 níveis de correção de erros:

| Nível | Nome     | Recupera até... |
|-------|----------|-----------------|
| L     | Low      | 7% dos dados    |
| M     | Medium   | 15% dos dados   |
| Q     | Quartile | 25% dos dados   |
| H     | High     | 30% dos dados   |

> É por isso que QR Codes com logos no meio ainda funcionam! A logo cobre parte dos módulos, mas o nível de correção **H** permite que até 30% da informação seja reconstruída pelo leitor. O designer que colocou aquele logo estava, na verdade, explorando matematicamente essa capacidade



### 2.3) Como o scanner percorre os dados — o caminho em zigue-zague

Embora para você seja simples apontar a câmera e pronto, por baixo dos panos o scanner está executando uma sequência precisa de passos para extrair cada bit de informação da grade.

#### O caminho de leitura

O scanner **não** lê os módulos de forma aleatória nem linha por linha. Ele percorre a grade em **colunas de 2 módulos**, num movimento de zigue-zague:

1. Começa no **canto inferior direito** da área de dados.
2. Sobe dois módulos de cada vez até encontrar um marcador de posição ou a borda.
3. Desloca-se **dois módulos para a esquerda** e passa a descer.
4. Repete o padrão — **direita→esquerda, sobe→desce** — até cobrir todos os módulos de dados.

Qualquer posição que pertença aos finder patterns, timing patterns ou format information é **ignorada** nesse percurso; o scanner pula essas áreas reservadas e continua.

#### Os 6 passos do processo de leitura

**1. Apontar o celular para o QR Code**

O aplicativo de câmera começa capturando frames de vídeo em busca de um padrão candidato.

**2. Identificar os marcadores de posição**

O scanner reconhece os três **finder patterns** (os quadrados grandes nos cantos). Com a zona de silêncio (quiet zone) em volta, ele delimita com precisão as bordas do código e calcula a perspectiva — mesmo que o código esteja levemente inclinado ou distorcido.

**3. Ler o indicador de modo (Mode Indicator)**

O scanner posiciona-se no canto **inferior direito** e lê os primeiros **4 módulos**. A ordem não é "linha por linha" nem "coluna por coluna" — é o próprio passo inicial do zigue-zague: **pares de colunas, de baixo para cima, coluna direita antes da esquerda**.

Visualizando os 4 módulos do indicador de modo (os dois últimos módulos à direita nas duas últimas linhas disponíveis):

```
        col→  ... [D] [E]   ← colunas do par mais à direita
linha ↓
  ...
  n-1            [ 3 ] [ 4 ]
   n             [ 1 ] [ 2 ]   ← linha mais baixa disponível
```

A leitura ocorre assim:

1. `[1]` — linha mais baixa, coluna direita do par → bit mais significativo (MSB)
2. `[2]` — mesma linha, coluna esquerda do par
3. `[3]` — uma linha acima, coluna direita
4. `[4]` — mesma linha, coluna esquerda → bit menos significativo (LSB)

Então para o modo **Byte** (`0100`), o scanner vê, nessa ordem: `0`, `1`, `0`, `0`.

Esses bits indicam qual tipo de dado foi codificado:

| Bits   | Modo          | Exemplos de conteúdo            |
|--------|---------------|---------------------------------|
| `0001` | Numérico      | `0123456789`                    |
| `0010` | Alfanumérico  | `A–Z`, `0–9`, ` $%*+-./:` |
| `0100` | Byte          | qualquer caractere UTF-8/ASCII  |
| `1000` | Kanji         | caracteres japoneses            |

**4. Ler o indicador de contagem de caracteres (Character Count Indicator)**

Logo acima do indicador de modo estão os próximos **8 módulos** (para versões 1–9). Eles representam um número binário que diz ao scanner **quantos caracteres** existem no payload — para que ele saiba exatamente quantos bits de dados precisa ler a seguir.

**5. Percorrer os módulos de dados no zigue-zague**

Conhecendo o modo e o comprimento, o scanner continua sua trilha em zigue-zague, lendo grupo a grupo de bits (8 bits por vez no modo Byte) e convertendo-os nos caracteres correspondentes. O processo termina quando o scanner lê o **indicador de fim** (`0000`), sinalizando que não há mais dados.

**6. Ler os módulos de correção de erros**

Após o último caractere, o scanner encontra os **codewords de correção de erros** gerados pelo algoritmo Reed-Solomon. Com essas informações redundantes, ele é capaz de detectar e **reconstruir módulos danificados ou ilegíveis** — conforme o nível de correção configurado (L, M, Q ou H).

> Repare que os passos 3, 4 e 5 mapeiam diretamente para a estrutura que vimos em [2.1](#21-escolha-do-modo-de-codificação) e [2.2](#22-correção-de-erros--o-superpoder-do-qr-code): o modo escolhido na geração é o primeiro dado que o leitor encontra; a contagem de caracteres vem em seguida; e a correção de erros fica no final do fluxo de bits, pronta para "consertar" o que o ruído ou o dano físico tiver corrompido.

---

## 3) Como a URL `https://alexsousadev.github.io/bitabit/` virou esse QR Code?

Até agora você entendeu a teoria — modos de codificação, correção de erros, padrões de posicionamento. Agora vamos acompanhar o processo **passo a passo**, usando como exemplo exato o arquivo `qrcode_bitabit.svg`.

### Passo 1 — Análise da entrada e escolha do modo

A URL tem **39 caracteres**:

```
https://alexsousadev.github.io/bitabit/
```

Como ela contém letras minúsculas (`alexsousadev`, `github`, `bitabit`), o modo **Alfanumérico** já é eliminado de cara — ele só aceita maiúsculas. O modo escolhido é o **Byte**, que trata cada caractere como um byte no padrão ISO-8859-1 (compatível com ASCII para todos os caracteres de uma URL).

### Passo 2 — Determinação da versão e do nível de correção de erros

Com 39 bytes em modo Byte, precisamos de uma versão grande o suficiente. O gerador avalia a menor versão que suporte os dados:

| Versão | Grade    | Capacidade Byte (Nível L) |
|--------|----------|---------------------------|
| 2      | 25 × 25  | 32 bytes                  |
| **3**  | **29 × 29** | **55 bytes**           |
| 4      | 33 × 33  | 80 bytes                  |

39 bytes cabe na **Versão 3** com nível de correção **L** (Low). Isso pode ser verificado diretamente no SVG: os módulos ocupam posições de `x=173` até `x=1769`, com espaçamento de 57 unidades, o que dá exatamente **29 posições distintas** → grade 29×29.

### Passo 3 — Conversão para bits

Cada caractere da URL é convertido para seu valor em ASCII e representado em 8 bits (1 byte). Antes dos dados propriamente ditos, o codificador precisa escrever um **cabeçalho de bits**:

- **Indicador de modo** (4 bits): `0100` — representa o modo Byte
- **Contador de caracteres** (8 bits para versão 1–9): `00100111` — representa o número 39 em binário

Em seguida, cada caractere da URL vira 8 bits:

| Char | ASCII (decimal) | Bits     |
|------|-----------------|----------|
| `h`  | 104             | `01101000` |
| `t`  | 116             | `01110100` |
| `t`  | 116             | `01110100` |
| `p`  | 112             | `01110000` |
| `s`  | 115             | `01110011` |
| `:`  | 58              | `00111010` |
| `/`  | 47              | `00101111` |
| `/`  | 47              | `00101111` |
| `a`  | 97              | `01100001` |
| ... (31 caracteres restantes) | | |

A sequência completa de bits fica:

```
0100  00100111  01101000 01110100 01110100 01110000 01110011
      ^ count   ^ h      ^ t      ^ t      ^ p      ^ s
00111010 00101111 00101111 01100001 01101100 ...
^ :      ^ /      ^ /      ^ a      ^ l
```

No total: `4 + 8 + (39 × 8) = 324 bits de dados`.

Ao final da sequência de dados, o codificador acrescenta um **terminador** de `0000` e bits de preenchimento até completar múltiplos de 8. Se ainda sobrarem "slots" de bytes, são adicionados os **bytes de padding** padrão `11101100` e `00010001` alternados.

### Passo 4 — Correção de erros com Reed-Solomon

Os bits de dados são agrupados em **codewords** (palavras de 8 bits). Para a Versão 3, nível L, a estrutura é:

- **19 codewords de dados** (152 bits)
- **7 codewords de correção de erros** gerados pelo algoritmo Reed-Solomon

O Reed-Solomon trata os codewords como polinômios num campo de Galois GF(256). O "polinômio dos dados" é dividido por um "polinômio gerador" de grau 7, e o resto dessa divisão são os 7 codewords de correção. Esses bytes extras permitem que o leitor **reconstrua até 7% dos dados danificados**.

### Passo 5 — Posicionamento na grade

Com os **26 codewords** no total (19 dados + 7 correção), o codificador distribui os bits na grade 29×29.

O preenchimento segue um caminho em **colunas de 2 módulos**, percorrendo a grade de baixo para cima, depois de cima para baixo, alternando. Posições que já estão "reservadas" (os padrões de posicionamento, timing patterns e format information) são puladas automaticamente.

<figure markdown="span">
![](./img/qrcode_bitabit.svg){ align=center, width="250"}
<figcaption>O QR Code do bitabit — versão 3, 29×29 módulos</figcaption>
</figure>

Olhando no SVG, os três **finder patterns** aparecem como blocos de `<svg>` aninhados nas posições `(173,173)`, `(1427,173)` e `(173,1427)` — os três cantos que você reconhece como os "quadrados grandes". O canto inferior-direito fica propositalmente **vazio**, permitindo que o leitor saiba exatamente qual é a orientação correta.

### Passo 6 — Aplicação da máscara

Para evitar grandes regiões de módulos todos pretos ou todos brancos (o que confundiria o leitor), uma das 8 máscaras padrão é aplicada sobre a região de dados. Cada máscara é definida por uma fórmula baseada na posição `(linha i, coluna j)` de cada módulo:

| Máscara | Condição para inverter o módulo  |
|---------|----------------------------------|
| 0       | `(i + j) % 2 == 0`               |
| 1       | `i % 2 == 0`                     |
| 2       | `j % 3 == 0`                     |
| 3       | `(i + j) % 3 == 0`               |
| 4       | `(i/2 + j/3) % 2 == 0`           |
| 5       | `(i*j)%2 + (i*j)%3 == 0`         |
| 6       | `((i*j)%2 + (i*j)%3) % 2 == 0`   |
| 7       | `((i+j)%2 + (i*j)%3) % 2 == 0`   |

O codificador calcula uma **pontuação de penalidade** para cada máscara (avaliando padrões repetitivos, desequilíbrio preto/branco, etc.) e escolhe a máscara com a menor pontuação. Isso garante que o QR Code tenha a melhor legibilidade possível.

### Passo 7 — Informações de formato

Os **15 bits de format information** codificam dois dados cruciais:

- O **nível de correção de erros** (L, M, Q ou H)
- O **número da máscara** aplicada (0–7)

Esses 15 bits são escritos em posições fixas ao lado dos finder patterns (nas linhas e colunas 8 da grade) e recebem XOR com uma sequência fixa `101010000010010` para evitar que sejam confundidos com módulos de dados. Eles são duplicados em dois lugares diferentes do código para garantir que o leitor sempre consiga ler essa informação.

### Passo 8 — Do grid para o SVG

Com todos os módulos definidos (preto = `1`, branco = `0`), o gerador percorre a grade posição por posição e, para cada módulo preto, escreve um elemento no arquivo SVG:

```svg
<rect x="686" y="173" width="57" height="57" fill="#000000"/>
```

- O canvas total é `2000 × 2000` unidades
- Cada módulo ocupa `57 × 57` unidades
- A primeira posição de módulo começa em `x=173, y=173` (zona de silêncio de ~3 módulos)
- Os **finder patterns** são representados como `<svg>` aninhados com `<path>` e `<polygon>` para o quadrado externo e o interno, respectivamente

O resultado final é o arquivo `qrcode_bitabit.svg`: uma coleção de centenas de retângulos pretos precisamente posicionados que, juntos, formam a representação visual da URL.

### Resumo visual do processo

```
URL (texto)
    │
    ▼
Bytes ASCII (modo Byte)
    │
    ▼
Bits: cabeçalho + dados + terminador + padding
    │
    ▼
Reed-Solomon → codewords de correção de erros
    │
    ▼
Posicionamento na grade 29×29
    │
    ▼
Aplicação de máscara (melhor equilíbrio preto/branco)
    │
    ▼
Escrita das format information (15 bits)
    │
    ▼
SVG: um <rect> por módulo preto → qrcode_bitabit.svg
```

### Referências
- https://x.com/icons_8/status/2044743892201808041/photo/1
- https://www.scandit.com/products/barcode-scanning/symbologies/qr-code/
- https://qrcrazy.blogspot.com/2012/05/what-are-qr-codes.html
- https://free-barcode.com/barcode/barcode-types/qr-code-decoding.asp
- https://jbirnick.net/posts/qr-codes/
- https://softwareengineeringhub.medium.com/how-do-qr-code-scanner-work-in-a-nutshell-a531973a4a
- https://www.researchgate.net/figure/The-Finder-and-Timing-Pattern-of-QR-Barcode_fig7_267828104