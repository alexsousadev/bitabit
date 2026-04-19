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

Agora, vamos entender cada um deles de forma mais detalhada...


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



### Referências
- https://x.com/icons_8/status/2044743892201808041/photo/1
- https://www.scandit.com/products/barcode-scanning/symbologies/qr-code/
- https://qrcrazy.blogspot.com/2012/05/what-are-qr-codes.html
- https://free-barcode.com/barcode/barcode-types/qr-code-decoding.asp
- https://jbirnick.net/posts/qr-codes/
- https://softwareengineeringhub.medium.com/how-do-qr-code-scanner-work-in-a-nutshell-a531973a4a
- https://www.researchgate.net/figure/The-Finder-and-Timing-Pattern-of-QR-Barcode_fig7_267828104