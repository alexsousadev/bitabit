# Outros Padrões de Código de Barras (EAN-13, Code 39 e mais)

Embora o UPC tenha sido o pioneiro nas prateleiras dos supermercados, a necessidade de automatizar diferentes indústrias fez com que o mundo da tecnologia criasse dezenas de outros formatos. 

**Cada modelo de código de barras que existe hoje nasceu para resolver uma limitação geográfica, de espaço físico ou de tipo de informação que o padrão original da IBM não conseguia tratar sozinho.**

<figure markdown="span">
  ![](../img/typesbarcode.jpeg){ align=center, width="500"}
</figure>

---

## 1) EAN-13: O padrão mundial

Quando a tecnologia do código de barras cruzou o oceano em 1977, a Europa e o resto do mundo quiseram adotá-la. Havia, porém, um problema geográfico: o UPC tinha sido feito sob medida para os Estados Unidos e Canadá. O resto do mundo precisava de um sistema que identificasse o país de origem de cada produto no comércio internacional.

Para resolver isso, nasceu o **EAN-13**. Os engenheiros pegaram a exata mesma estrutura matemática do UPC que vimos lá atrás, mas adicionaram um décimo terceiro ($13^{\circ}$) dígito na frente do código para indicar o país.

Mas aí surgiu um problemão: se os computadores do mundo todo passassem a usar 13 dígitos, como eles leriam os bilhões de produtos americanos que já estavam impressos com o UPC de 12 dígitos?

A solução da GS1 (a organização global de padrões) foi de uma elegância matemática genial: eles transformaram o número zero ($0$) no código oficial dos Estados Unidos e do Canadá.

Funciona assim: na tabela global de países da GS1, a faixa que vai de `000` a `139` ficou reservada exclusivamente para os EUA e Canadá. Então, para o sistema internacional ler um código UPC americano de 12 dígitos, o software do caixa coloca um zero invisível automaticamente na frente dele.

*Se pegarmos o nosso código de exemplo lá de trás, o UPC-A `036000291452` (12 dígitos) é lido pelo sistema global como `0036000291452` (13 dígitos).*

Pronto! O mistério foi desfeito de forma unificada. É por isso que, hoje, qualquer computador do planeta lê os dois formatos sem travar:

- Se o código tem 13 dígitos e começa entre `000` e `139`, o sistema sabe que é um código nativo americano (UPC) adaptado com o zero na frente.
- Se começa com `789` ou `790`, o sistema sabe que a empresa registrou o produto no Brasil.
- Se começa com `560`, foi registrado em Portugal.

> **O "Mito" da Origem:** Um detalhe importante para não cair em pegadinhas é que esse prefixo indica apenas o país onde a empresa registrou a sua marca, e não onde a mercadoria foi fabricada de fato. Uma marca americana pode fabricar suas camisetas na China, mas o código de barras continuará iniciando com o zero dos EUA.

Seguindo a mesma lógica de portabilidade, os europeus também criaram o **EAN-8**, uma versão reduzida para 8 dígitos usada exclusivamente para etiquetar embalagens muito pequenas onde o código de 13 dígitos não caberia.

> Você pode consultar uma tabela completa com os principais prefixos de países em [GS1 Company Prefix](https://www.gs1.org/standards/id-keys/company-prefix). A Wikipedia também organizou essa lista de uma forma um pouco mais amigável em [List of GS1 country codes](https://en.wikipedia.org/wiki/List_of_GS1_country_codes).

---

## 2) Code 39

Fora do varejo tradicional, as necessidades eram outras, pois indústrias e transportadoras precisavam registrar letras e não apenas números. Para resolver isso, surgiu o **Code 39**, o primeiro modelo alfanumérico da história, muito adotado pelo setor automotivo e pelo Departamento de Defesa dos EUA devido à sua alta segurança contra falhas, ideal para inventários de grande porte e peças de metal.

---

## 3) Code 128

Pouco depois, buscando mais eficiência de espaço, foi desenvolvido o **Code 128**, um código de altíssima densidade que consegue armazenar letras, números e símbolos de forma muito mais compacta, tornando-se o padrão absoluto para o rastreio de encomendas na logística global e em crachás corporativos.

---

## 4) Interleaved 2 of 5 (Intercalado 2 de 5)

Para lidar com impressões de qualidade inferior, como caixas de papelão ásperas de armazéns, foi criado o **Interleaved 2 of 5**, que armazena números em pares e possui alta tolerância a falhas de tinta — uma característica que o tornou perfeito para ser adotado, até os dias de hoje, na leitura de boletos bancários.

---

## 5) Codabar

Já o **Codabar** nasceu em 1972 com foco em impressoras térmicas antigas, utilizando letras especiais para marcar o início e o fim da leitura, o que garantiu seu uso histórico em tubos de ensaio de bancos de sangue e etiquetas de livros em bibliotecas.

---

## 6) PostNet

Por fim, até os serviços postais ganharam soluções exclusivas, como o **PostNet**, um código peculiar composto por barras de alturas variadas (curtas e longas) desenhado sob medida pelo correio americano para decifrar os CEPs nos envelopes e acelerar a triagem de cartas em altíssima velocidade.

<style>
  .next-step-card-wrapper {
    margin-top: 2rem;
    border-top: 1px solid rgba(255, 255, 255, 0.1);
    padding-top: 1.5rem;
  }
  .next-step-card-wrapper a {
    display: flex !important;
    align-items: center;
    justify-content: space-between;
    padding: 1rem 1.5rem;
    background-color: rgba(255, 255, 255, 0.03);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 8px;
    text-decoration: none !important;
    transition: all 0.3s ease;
    color: inherit !important;
  }
  .next-step-card-wrapper a:hover {
    background-color: rgba(255, 255, 255, 0.08) !important;
    border-color: var(--md-typeset-a-color, #009688) !important;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
  }
  .next-step-card-wrapper a .nav-arrow {
    font-size: 1.5rem;
    transition: transform 0.3s ease;
    display: inline-block;
  }
  .next-step-card-wrapper a:hover .nav-arrow {
    transform: translateX(6px);
  }
  .next-step-card-wrapper a .nav-title {
    font-size: 1.1rem;
    font-weight: 700;
    color: var(--md-typeset-a-color, #009688);
  }
</style>

<div class="next-step-card-wrapper" markdown="1">

[<span class="nav-title">5) Desafios e Ceticismo de Implementação</span> <span class="nav-arrow">➔</span>](./desafios-e-ceticismo.md)

</div>
