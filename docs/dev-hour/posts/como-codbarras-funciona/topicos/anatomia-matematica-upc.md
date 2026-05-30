# A Anatomia Matemática do UPC (Universal Product Code)

Para entender a estrutura do UPC, primeiro precisamos quebrar o código de barras em suas menores partes. A menor unidade de um código de barras é chamada de "módulo", com uma largura padrão de 0,33 milímetros (basicamente, é a linha mais fina possível). Ele é incrivelmente pequeno. 

> Essa padronização de tamanho é mantida pela GS1 (Global System 1), uma organização internacional, neutra e sem fins lucrativos, responsável por desenvolver e manter os padrões globais de comunicação empresarial.

Isso garante que um código de barras impresso no Brasil seja lido exatamente do mesmo jeito na China, nos Estados Unidos ou em qualquer outro lugar.

> Você pode ver as regras de tamanho em [GS1 - UPC Specifications](https://www.gs1ie.org/standards/data-carriers/barcodes/upc/).

Mas, de forma geral, a GS1 permite que esse tamanho varie um pouco para caber em embalagens diferentes:

- **O tamanho mínimo permitido:** $0,26 \text{ mm}$ (usado em produtos bem pequenos, como chicletes ou esmaltes).
- **O tamanho máximo permitido:** $0,66 \text{ mm}$ (usado em caixas grandes de papelão em estoques, para o operador conseguir ler de longe).

Quando olhamos para um código de barras de longe, vemos linhas pretas de vários tamanhos (umas finas, outras médias, outras bem grossas). Mas essas linhas grossas são apenas vários módulos pretos colocados colados um ao lado do outro. Na prática, isso significa que estamos codificando uma informação de forma binária: 

<figure markdown="span">
  ![](../img/scanner.png){ align=center, width="500"}
</figure>

- **Módulo de cor de fundo (Branco):** É definido normativamente com o valor lógico $0$.
- **Módulo de cor de primeiro plano (Preto):** É definido normativamente com o valor lógico $1$.

Assim, tudo que temos ali são números codificados em binário. No entanto, não temos apenas o código em si do produto, temos também uma série de módulos que servem para orientar o leitor e garantir que a leitura seja feita corretamente. Dessa forma, podemos dividir um código de barras em três grandes grupos: 

1. **Blocos de dados (Data Blocks):** São os módulos que carregam a informação do produto. 

    > No código de barras tradicional (chamado tecnicamente de UPC-A), temos 6 blocos de dados à esquerda e 6 blocos de dados à direita.

2. **Portões (Guards):** São os módulos que servem para orientar o leitor. 

    > 6 módulos formam os portões de segurança (2 na entrada, 2 no meio, 2 na saída).

3. **Zona de silêncio (Quiet Zones):** É a área em branco antes do código de barras. 

    > É obrigatório ter um espaço em branco de pelo menos 9 módulos de largura antes e depois do código. Isso serve para o leitor entender onde o código começa e onde ele termina. 

Por exemplo, um código assim:

<div style="text-align: center; margin: 1.5rem 0;">
  <img src="../../img/upc_a_normal.svg" alt="Código de barras UPC-A normal" style="background-color: #ffffff; padding: 12px; border-radius: 6px; display: inline-block; width: 200px; box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);" />
</div>

pode ser dividido assim:

> A tabela abaixo representa um exemplo de como ele é estruturado e como seria a representação de cada número no código de barras, e não exatamente o mesmo código da imagem acima.

<div class="barcode-table-container" style="overflow-x: auto; margin: 2rem 0; box-shadow: 0 4px 20px rgba(0, 0, 0, 0.15); border-radius: 8px;">
  <table style="text-align: center; border-collapse: collapse; width: 100%; min-width: 800px; font-family: 'Outfit', 'Inter', system-ui, -apple-system, sans-serif; background-color: #80A080; border: none; color: #ffffff; margin: 0;">
    <caption style="padding: 14px; font-weight: 700; font-size: 1.1rem; background-color: #5a755a; color: #ffffff; letter-spacing: 0.5px; border-bottom: 2px solid rgba(255, 255, 255, 0.15);">
      Tabela de codificação para o padrão de código de barras UPC-A
    </caption>
    <thead>
      <tr style="background-color: #698b69; border-bottom: 2px solid rgba(255, 255, 255, 0.1);">
        <th rowspan="2" style="padding: 12px 6px; border: 1px solid rgba(255, 255, 255, 0.1); font-weight: 600; text-transform: uppercase; font-size: 0.85rem; letter-spacing: 0.5px;">Zona de Silêncio</th>
        <th rowspan="2" style="padding: 12px 6px; border: 1px solid rgba(255, 255, 255, 0.1); font-weight: 600; text-transform: uppercase; font-size: 0.85rem; letter-spacing: 0.5px;">PORTÃO</th>
        <th colspan="10" style="padding: 12px 6px; border: 1px solid rgba(255, 255, 255, 0.1); font-weight: 700; font-size: 0.9rem; text-transform: uppercase; letter-spacing: 1px;">Bloco de Dados (Esquerda)</th>
        <th rowspan="2" style="padding: 12px 6px; border: 1px solid rgba(255, 255, 255, 0.1); font-weight: 600; text-transform: uppercase; font-size: 0.85rem; letter-spacing: 0.5px;">PORTÃO</th>
        <th colspan="10" style="padding: 12px 6px; border: 1px solid rgba(255, 255, 255, 0.1); font-weight: 700; font-size: 0.9rem; text-transform: uppercase; letter-spacing: 1px;">Bloco de Dados (Direita)</th>
        <th rowspan="2" style="padding: 12px 6px; border: 1px solid rgba(255, 255, 255, 0.1); font-weight: 600; text-transform: uppercase; font-size: 0.85rem; letter-spacing: 0.5px;">PORTÃO</th>
        <th rowspan="2" style="padding: 12px 6px; border: 1px solid rgba(255, 255, 255, 0.1); font-weight: 600; text-transform: uppercase; font-size: 0.85rem; letter-spacing: 0.5px;">Zona de silêncio</th>
      </tr>
      <tr style="background-color: #698b69;">
        <!-- L 0-9 -->
        <th style="padding: 8px 4px; border: 1px solid rgba(255, 255, 255, 0.1); font-weight: 700;">0</th>
        <th style="padding: 8px 4px; border: 1px solid rgba(255, 255, 255, 0.1); font-weight: 700;">1</th>
        <th style="padding: 8px 4px; border: 1px solid rgba(255, 255, 255, 0.1); font-weight: 700;">2</th>
        <th style="padding: 8px 4px; border: 1px solid rgba(255, 255, 255, 0.1); font-weight: 700;">3</th>
        <th style="padding: 8px 4px; border: 1px solid rgba(255, 255, 255, 0.1); font-weight: 700;">4</th>
        <th style="padding: 8px 4px; border: 1px solid rgba(255, 255, 255, 0.1); font-weight: 700;">5</th>
        <th style="padding: 8px 4px; border: 1px solid rgba(255, 255, 255, 0.1); font-weight: 700;">6</th>
        <th style="padding: 8px 4px; border: 1px solid rgba(255, 255, 255, 0.1); font-weight: 700;">7</th>
        <th style="padding: 8px 4px; border: 1px solid rgba(255, 255, 255, 0.1); font-weight: 700;">8</th>
        <th style="padding: 8px 4px; border: 1px solid rgba(255, 255, 255, 0.1); font-weight: 700;">9</th>
        <!-- R 0-9 -->
        <th style="padding: 8px 4px; border: 1px solid rgba(255, 255, 255, 0.1); font-weight: 700;">0</th>
        <th style="padding: 8px 4px; border: 1px solid rgba(255, 255, 255, 0.1); font-weight: 700;">1</th>
        <th style="padding: 8px 4px; border: 1px solid rgba(255, 255, 255, 0.1); font-weight: 700;">2</th>
        <th style="padding: 8px 4px; border: 1px solid rgba(255, 255, 255, 0.1); font-weight: 700;">3</th>
        <th style="padding: 8px 4px; border: 1px solid rgba(255, 255, 255, 0.1); font-weight: 700;">4</th>
        <th style="padding: 8px 4px; border: 1px solid rgba(255, 255, 255, 0.1); font-weight: 700;">5</th>
        <th style="padding: 8px 4px; border: 1px solid rgba(255, 255, 255, 0.1); font-weight: 700;">6</th>
        <th style="padding: 8px 4px; border: 1px solid rgba(255, 255, 255, 0.1); font-weight: 700;">7</th>
        <th style="padding: 8px 4px; border: 1px solid rgba(255, 255, 255, 0.1); font-weight: 700;">8</th>
        <th style="padding: 8px 4px; border: 1px solid rgba(255, 255, 255, 0.1); font-weight: 700;">9</th>
      </tr>
    </thead>
    <tbody>
      <tr style="background-color: #80A080; vertical-align: top;">
        <td style="padding: 12px 6px; border: 1px solid rgba(255, 255, 255, 0.1); background-color: rgba(255, 255, 255, 0.05);"><img src="../../img/UPC-A_Q.png" alt="Quiet Zone" style="width: 27px; height: 241px; display: block; margin: 0 auto;" /></td>
        <td style="padding: 12px 6px; border: 1px solid rgba(255, 255, 255, 0.1);"><img src="../../img/UPC-A_S.png" alt="Start" style="width: 10px; height: 245px; display: block; margin: 0 auto;" /></td>
        <!-- L 0-9 -->
        <td style="padding: 12px 6px; border: 1px solid rgba(255, 255, 255, 0.1);"><img src="../../img/UPC-A_L0.png" alt="L0" style="width: 20px; height: 235px; display: block; margin: 0 auto;" /></td>
        <td style="padding: 12px 6px; border: 1px solid rgba(255, 255, 255, 0.1);"><img src="../../img/UPC-A_L1.png" alt="L1" style="width: 20px; height: 235px; display: block; margin: 0 auto;" /></td>
        <td style="padding: 12px 6px; border: 1px solid rgba(255, 255, 255, 0.1);"><img src="../../img/UPC-A_L2.png" alt="L2" style="width: 20px; height: 235px; display: block; margin: 0 auto;" /></td>
        <td style="padding: 12px 6px; border: 1px solid rgba(255, 255, 255, 0.1);"><img src="../../img/UPC-A_L3.png" alt="L3" style="width: 20px; height: 235px; display: block; margin: 0 auto;" /></td>
        <td style="padding: 12px 6px; border: 1px solid rgba(255, 255, 255, 0.1);"><img src="../../img/UPC-A_L4.png" alt="L4" style="width: 20px; height: 235px; display: block; margin: 0 auto;" /></td>
        <td style="padding: 12px 6px; border: 1px solid rgba(255, 255, 255, 0.1);"><img src="../../img/UPC-A_L5.png" alt="L5" style="width: 20px; height: 235px; display: block; margin: 0 auto;" /></td>
        <td style="padding: 12px 6px; border: 1px solid rgba(255, 255, 255, 0.1);"><img src="../../img/UPC-A_L6.png" alt="L6" style="width: 20px; height: 235px; display: block; margin: 0 auto;" /></td>
        <td style="padding: 12px 6px; border: 1px solid rgba(255, 255, 255, 0.1);"><img src="../../img/UPC-A_L7.png" alt="L7" style="width: 20px; height: 235px; display: block; margin: 0 auto;" /></td>
        <td style="padding: 12px 6px; border: 1px solid rgba(255, 255, 255, 0.1);"><img src="../../img/UPC-A_L8.png" alt="L8" style="width: 20px; height: 235px; display: block; margin: 0 auto;" /></td>
        <td style="padding: 12px 6px; border: 1px solid rgba(255, 255, 255, 0.1);"><img src="../../img/UPC-A_L9.png" alt="L9" style="width: 20px; height: 235px; display: block; margin: 0 auto;" /></td>
        <!-- M -->
        <td style="padding: 12px 6px; border: 1px solid rgba(255, 255, 255, 0.1);"><img src="../../img/UPC-A_M.png" alt="Middle" style="width: 15px; height: 245px; display: block; margin: 0 auto;" /></td>
        <!-- R 0-9 -->
        <td style="padding: 12px 6px; border: 1px solid rgba(255, 255, 255, 0.1);"><img src="../../img/UPC-A_R0.png" alt="R0" style="width: 20px; height: 235px; display: block; margin: 0 auto;" /></td>
        <td style="padding: 12px 6px; border: 1px solid rgba(255, 255, 255, 0.1);"><img src="../../img/UPC-A_R1.png" alt="R1" style="width: 20px; height: 235px; display: block; margin: 0 auto;" /></td>
        <td style="padding: 12px 6px; border: 1px solid rgba(255, 255, 255, 0.1);"><img src="../../img/UPC-A_R2.png" alt="R2" style="width: 20px; height: 235px; display: block; margin: 0 auto;" /></td>
        <td style="padding: 12px 6px; border: 1px solid rgba(255, 255, 255, 0.1);"><img src="../../img/UPC-A_R3.png" alt="R3" style="width: 20px; height: 235px; display: block; margin: 0 auto;" /></td>
        <td style="padding: 12px 6px; border: 1px solid rgba(255, 255, 255, 0.1);"><img src="../../img/UPC-A_R4.png" alt="R4" style="width: 20px; height: 235px; display: block; margin: 0 auto;" /></td>
        <td style="padding: 12px 6px; border: 1px solid rgba(255, 255, 255, 0.1);"><img src="../../img/UPC-A_R5.png" alt="R5" style="width: 20px; height: 235px; display: block; margin: 0 auto;" /></td>
        <td style="padding: 12px 6px; border: 1px solid rgba(255, 255, 255, 0.1);"><img src="../../img/UPC-A_R6.png" alt="R6" style="width: 20px; height: 235px; display: block; margin: 0 auto;" /></td>
        <td style="padding: 12px 6px; border: 1px solid rgba(255, 255, 255, 0.1);"><img src="../../img/UPC-A_R7.png" alt="R7" style="width: 20px; height: 235px; display: block; margin: 0 auto;" /></td>
        <td style="padding: 12px 6px; border: 1px solid rgba(255, 255, 255, 0.1);"><img src="../../img/UPC-A_R8.png" alt="R8" style="width: 20px; height: 235px; display: block; margin: 0 auto;" /></td>
        <td style="padding: 12px 6px; border: 1px solid rgba(255, 255, 255, 0.1);"><img src="../../img/UPC-A_R9.png" alt="R9" style="width: 20px; height: 235px; display: block; margin: 0 auto;" /></td>
        <!-- E -->
        <td style="padding: 12px 6px; border: 1px solid rgba(255, 255, 255, 0.1);"><img src="../../img/UPC-A_S.png" alt="End" style="width: 10px; height: 245px; display: block; margin: 0 auto;" /></td>
        <td style="padding: 12px 6px; border: 1px solid rgba(255, 255, 255, 0.1); background-color: rgba(255, 255, 255, 0.05);"><img src="../../img/UPC-A_Q.png" alt="Quiet Zone" style="width: 27px; height: 241px; display: block; margin: 0 auto;" /></td>
      </tr>
    </tbody>
  </table>
</div>

Cada número precisa usar um bloco de exatamente 7 módulos. A imagem abaixo ilustra bem isso:

<figure markdown="span">
  ![](../img/numeros.png){ align=center, width="400"}
</figure>

Com isso em mente, a "receita" do número 1 para o lado esquerdo é (3 brancos, 2 pretos, 1 branco, 1 preto):

$$\text{Branco} - \text{Branco} - \text{Branco} - \text{Preto} - \text{Preto} - \text{Branco} - \text{Preto}$$

Já para o lado direito do código, a receita do número 1 é diferente (basicamente é o inverso, onde era preto fica branco e vice-versa):

$$\text{Preto} - \text{Preto} - \text{Preto} - \text{Branco} - \text{Branco} - \text{Preto} - \text{Branco}$$

---

### Por que existe essa diferença?

A mudança de receita existe por um motivo simples: dar o sentido da direção para o computador, da mesma forma que uma placa de trânsito diz se uma rua é "mão" ou "contramão".

Por exemplo, se o número 1 fosse desenhado igual na esquerda e na direita, a estrada de fatias seria idêntica. Quando o produto passasse de cabeça para baixo, o laser começaria a ler o código pelo fim (pela direita) achando que era o começo (a esquerda).

O computador leria todos os números de trás para frente. Em vez de ler o código real do produto, ele leria uma sequência totalmente errada, o sistema não encontraria o preço e o caixa travaria.

É por isso que há esse truque de espelhar a receita de cada número. Assim:

- **No Lado Esquerdo**: Todos os números (de 0 a 9) foram desenhados com um número **ÍMPAR** de fatias pretas.
- **No Lado Direito**: Todos os números foram desenhados com um número **PAR** de fatias pretas.

Assim, quando o laser cruza o código de barras, a primeira coisa que o software faz é contar a paridade dos blocos de 7 fatias que ele acabou de ler. Se o resultado for ímpar, ele sabe que está lendo o lado esquerdo. Se for par, ele sabe que está lendo o lado direito.

Dessa forma, caso esteja sendo lido invertido, em vez de dar um erro e travar o caixa, o computador simplesmente faz uma operação matemática interna: ele espelha e inverte a ordem dos bits na memória, transformando o que ele leu de trás para frente no código correto.

---

Levando em conta essa organização, todo código UPC-A tem exatamente 30 barras pretas. Como ele usa 12 dígitos para dados, isso significa que a capacidade máxima é de 100 bilhões de combinações de produtos diferentes ($10^{11}$ ou $100.000.000.000$). É espaço de sobra para registrar produtos por décadas.

---

## E o que são aqueles números embaixo?

Quando olhamos para um código de barras impresso na embalagem de um produto, costumamos ver alguns números alinhados embaixo das barras. Como já citado, eles são exatamente os números que estão codificados nas barras. Foram feitos para que os humanos possam ler o código de barras caso precise digitar manualmente em algum sistema por algum problema.

Porém, se você reparar bem na organização de um código do tipo UPC-A, vai notar que o primeiro número e o último ficam "jogados" para fora, meio isolados nos cantos. No nosso exemplo anterior, temos o 0 e 2 isolados nas extremidades:

<div style="text-align: center; margin: 1.5rem 0;">
  <img src="../../img/upc_a_normal.svg" alt="Código de barras UPC-A normal" style="background-color: #ffffff; padding: 12px; border-radius: 6px; display: inline-block; width: 200px; box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);" />
</div>

Segundo as regras oficiais da GS1, eles significam:

- **Esquerdo**: É o dígito de agrupamento. Ele identifica o tipo de produto ou categoria ao qual o item pertence (no exemplo, é o número 0).
- **Direito**: É o dígito verificador. Ele é usado para garantir que o código de barras foi lido corretamente (no exemplo, é o número 2).

### Dígito de Agrupamento

Esse primeiro dígito (que fica isolado no canto esquerdo) avisa ao computador da loja com que tipo de produto ele está lidando:

| Código | Descrição | 
| --- | --- |
| 0, 1, 6, 7, 8, 9 | São para produtos comuns de supermercado. Onde os números seguintes identificam a fábrica e o produto. |
| 2 | É reservado para itens pesados na hora (como carne, queijo ou frutas). Quando o mercado embala uma bandeja de carne, o próprio mercado gera esse código. O sistema lê o número 2, entende que é um item de peso variável e usa os últimos números do código para puxar o peso ou o preço direto da balança. |
| 3 | Reservado para medicamentos e remédios (nos EUA, os números do meio correspondem ao registro oficial de drogas do governo, o NDC). |
| 4 | Reservado para uso interno da própria loja, geralmente usado em cartões de fidelidade ou cupons de desconto do próprio estabelecimento. |
| 5 | Reservado para cupons de desconto de fabricantes (aqueles que dão desconto cumulativo em produtos específicos). |

### Dígito Verificador

A única função dele é responder a uma pergunta para o computador: *"As barras foram lidas corretamente ou o código está riscado, sujo ou amassado?"*

Quando o laser passa pelo código de barras, o computador lê os 11 primeiros números e, em uma fração de milissegundo, faz uma conta matemática com eles. O resultado final dessa conta obrigatoriamente precisa dar igual ao último número.

> Veja os detalhes matemáticos e o passo a passo de como fazer essa conta em: [Como funciona o dígito verificador do código de barras](./calculo-digito-verificador.md)

### E o resto? (Código da Empresa e do Produto)

Os valores numéricos centrais são os dados em si, ou seja, o código do produto. Geralmente, são divididos entre código da empresa e código do produto. Então, usando aquele código de barras de exemplo:

- **36000**: Código da empresa (identifica quem fabricou ou distribui o produto). Por exemplo, sinaliza que o produto foi fabricado por "Colgate-Palmolive".
- **29145**: Código do produto (identifica o produto específico). Por exemplo, pode ser o "Creme Dental Colgate Total 12 de 90g".

As empresas não inventam os códigos do nada; elas alugam um bloco exclusivo de números da GS1 para garantir que nenhuma empresa no mundo tenha um código igual ao seu. A divisão do código depende do tamanho da fabricante. Grandes corporações recebem um prefixo de empresa curto (sobrando mais dígitos para cadastrar milhares de produtos). Pequenos produtores recebem um prefixo longo (sobrando poucos dígitos, o suficiente para uma linha pequena de produtos).

> Algo muito parecido com a divisão de IPs, onde uma faixa maior ou menor é separada para os hosts ou roteadores, dependendo do tamanho da empresa.
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

[<span class="nav-title">3) O Modelo Compacto UPC-E: O segredo para economizar espaço</span> <span class="nav-arrow">➔</span>](./modelo-upc-e.md)

</div>
