# Como funciona o Código de Barras?

Você provavelmente ouve esse som quase todo dia: o "bipe" do caixa eletrônico ou do supermercado. Mas você já parou para pensar no que a tecnologia está olhando quando lê um código de barras?

A maioria de nós passa a vida inteira achando que o scanner está lendo aquelas linhas pretas. Mas a verdade é o oposto: o leitor óptico ignora o preto e lê os espaços em branco. Como assim?

Vamos entender como essa tecnologia funciona (e por que ela acabou ficando pequena demais para a indústria).

# Como tudo começou...

A ideia não nasceu em um laboratório de alta tecnologia, mas sim de uma conversa de corredor em 1948, nos Estados Unidos. Bernard Silver, um estudante do Drexel Institute, ouviu por acaso o presidente de uma rede de supermercados implorando a um diretor da faculdade por um sistema automático que agilizasse as filas do caixa e controlasse o estoque.

Naquela época, os operadores de caixa precisavam olhar para cada produto, identificar o preço impresso ou colado na embalagem e digitar manualmente, dígito por dígito, em caixas registradoras mecânicas. Esse movimento mecânico, acelerado e repetido milhares de vezes por dia fez com que muitos caixas desenvolvessem problemas crônicos de saúde, sendo a síndrome do túnel do carpo a mais comum e dolorosa delas (uma inflamação nos nervos do pulso causada por esforço repetitivo).

<figure markdown="span">
![](./img/caixa_passado.webp){ align=center, width="500"}
</figure>

Como o processo dependia totalmente da velocidade de digitação humana, as filas nos supermercados eram gigantescas, gerando gargalos operacionais monstruosos para os donos de redes de comércio.

Bernard correu para contar ao seu amigo, Norman Joseph Woodland. Woodland bitolou no problema. Ele se mudou para a Flórida para focar em uma solução e, em um belo dia na praia, começou a desenhar na areia os pontos e traços do Código Morse (tecnologia que ele conhecia bem por ter sido escoteiro). 

Para contextualizar, o Código Morse é, essencialmente, o avô do código binário que usamos hoje: ele transforma letras e números em apenas dois estímulos (um curto e um longo). Criado nos anos 1830 por Samuel Morse, esse sistema foi feito para transmitir mensagens à distância através do telégrafo (aquele aparelho que enviava impulsos elétricos por um fio). Como não dava para enviar a voz humana ou letras escritas pelo fio, Morse criou um alfabeto baseado em apenas dois tipos de sinais sonoros ou elétricos:

- O Ponto ($\cdot$): Um sinal rápido e curto.
- O Traço ($-$): Um sinal que dura o triplo do tempo do ponto.

Combinando esses pontos e traços, você consegue escrever qualquer palavra:

<figure markdown="span">
![](./img/codigo-morse.jpg){ align=center, width="500"}
</figure>

O grande estalo dele foi: E se, em vez de pontos e traços, eu puxar essas marcações para baixo, transformando-as em linhas verticais finas e grossas?

Ao fazer isso, Woodland percebeu que um feixe de luz (que mais tarde viria a ser o laser) poderia passar por aquelas linhas e ler o reflexo: as linhas pretas absorveriam a luz e as brancas a refletiriam de volta, gerando um sinal elétrico correspondente a uma sequência de números.


<figure markdown="span">
![](./img/praia.png){ align=center, width="500"}
</figure>


Em 1952, eles patentearam a ideia. No entanto, o primeiro código de barras comercial não era uma linha reta, era circular! Parecia um alvo de tiro ao alvo. Eles desenharam assim porque achavam que seria mais fácil para o funcionário do mercado passar o produto em qualquer direção sobre o leitor.

A imagem abaixo mostra exatamente o desenho técnico que constava no documento oficial dessa patente. Repare que eles incluíram uma nota super importante no rodapé do desenho: "As linhas 6, 7, 8 e 9 são menos reflexivas que as linhas 10". Ou seja, ali já nascia o conceito de usar a diferença de reflexão da luz (linhas escuras que absorvem a luz vs. espaços claros que refletem) para gerar dados digitais.

<figure markdown="span">
![](./img/patente_inicial.jpeg){ align=center, width="500"}
</figure>

> Você pode visualizar a patente completa no Google Patents ([US2612994A](https://patents.google.com/patent/US2612994A/en))

A ideia era brilhante, mas estava à frente do seu tempo. Os computadores da década de 1950 eram gigantescos, os lasers ainda não existiam e a tecnologia para ler aquelas linhas de forma barata simplesmente não existia. A patente acabou esquecida por um tempo.

O jogo só virou nos anos 1970, quando a IBM (onde Woodland agora trabalhava) e um engenheiro chamado George Laurer resgataram o conceito. Laurer percebeu que as linhas retas eram mais fáceis de imprimir sem borrar do que os círculos perfeitos. Isso porque, as gráficas da década de 1970 usavam prensas rotativas que corriam em alta velocidade. O grande problema técnico era que a tinta borrava na direção do movimento da prensa (conhecido na indústria gráfica como *ink slurring* ou *press gain*) e ocorria porque a pressão e o movimento contínuo do rolo faziam a tinta fresca "escorrer" levemente para frente ou para trás na direção em que o papel caminhava.


<figure markdown="span">
![](./img/rotative_print.jpg){ align=center, width="300"}
</figure>

Com isso, se você tentasse imprimir um círculo e a tinta borrasse um milímetro para o lado, o círculo virava uma elipse e o computador não conseguia calcular o diâmetro das linhas. O leitor falhava.

Com o código em linhas retas, o borrão apenas tornaria as linhas um pouco mais compridas, mas a espessura exata (que é o que carrega a informação) continuaria idêntica. Assim, ele redesenhou o sistema e criou o UPC (Universal Product Code), o tataravô do código de barras que está nos produtos que você consome até hoje. 

## A Anatomia Matemática do UPC (Universal Product Code)


A menor unidade de um código de barras é chamada de "módulo", com uma largura padrão de 0,33 milímetros. Ele é incrivelmente pequeno. 

> Essa padronização é mantida pela GS1 (Global System 1), uma organização internacional, neutra e sem fins lucrativos, responsável por desenvolver e manter os padrões globais de comunicação empresarial. A sua função mais conhecida é a emissão e a padronização dos códigos de barras e das identidades digitais de produtos.

Isso garante que um código de barras impresso no Brasil seja lido exatamente do mesmo jeito na China, nos Estados Unidos ou em qualquer outro lugar.

> Você pode ver as regras de tamanho em [GS1 - UPC Specifications](https://www.gs1ie.org/standards/data-carriers/barcodes/upc/).

A GS1 permite que esse tamanho varie um pouco para caber em embalagens diferentes:

- O tamanho mínimo permitido: $0,26 \text{ mm}$ (usado em produtos bem pequenos, como chicletes ou esmaltes).
- O tamanho máximo permitido: $0,66 \text{ mm}$ (usado em caixas grandes de papelão em estoques, para o operador conseguir ler de longe).

> Como a organização global GS1 precisava atender a diferentes tipos de indústrias, tamanhos de embalagens e necessidades de transporte, ela criou vários padrões de códigos de barras ao longo dos anos. No entanto, os que sobreviveram até hoje é o UPC-A (O código de barras tradicional) e o UPC-E (uma versão compacta do UPC-A, usada em produtos pequenos).

Quando olhamos para um código de barras de longe, vemos linhas pretas de vários tamanhos (umas finas, outras médias, outras bem grossas). Mas essas linhas grossas são apenas vários módulos pretos colocados colados um ao lado do outro. Na prática, isso significa que estamos codificando uma informação de forma binária: 
<figure markdown="span">
![](./img/scanner.png){ align=center, width="500"}
</figure>

- **Módulo de cor de fundo (Branco):** É definido normativamente com o valor lógico $0$.
- **Módulo de cor de primeiro plano (Preto):** É definido normativamente com o valor lógico $1$.

Assim, tudo que temos ali são números codificados em binário. No entanto, não temos apenas o código em si do produto, temos também uma série de módulos que servem para orientar o leitor e garantir que a leitura seja feita corretamente. Assim, podemos dividir um código de barras em três grandes grupos: 

1. **Blocos de dados (Data Blocks):** São os módulos que carregam a informação do produto. 

    > No código UPC-A tradicional (o mais comum), temos 6 blocos de dados à esquerda e 6 blocos de dados à direita.
    

2. **Portões (Guards):** São os módulos que servem para orientar o leitor. 

    > 6 módulos formam os portões de segurança (2 na entrada, 2 no meio, 2 na saída).

3. **Zona de silêncio (Quiet Zones):** É a área em branco antes do código de barras. 

    > É obrigatório ter um espaço em branco de pelo menos 9 módulos de largura antes e depois do código. Isso serve para o leitor entender onde o código começa e onde ele termina. 

Por exemplo, esse código:

<div style="text-align: center; margin: 1.5rem 0;">
  <img src="../img/upc_a_normal.svg" alt="Código de barras UPC-A normal" style="background-color: #ffffff; padding: 12px; border-radius: 6px; display: inline-block; width: 200px; box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);" />
</div>

pode ser dividido assim:

<div class="barcode-table-container" style="overflow-x: auto; margin: 2rem 0; box-shadow: 0 4px 20px rgba(0, 0, 0, 0.15); border-radius: 8px;">
  <table style="text-align: center; border-collapse: collapse; width: 100%; min-width: 800px; font-family: 'Outfit', 'Inter', system-ui, -apple-system, sans-serif; background-color: #80A080; border: none; color: #ffffff; margin: 0;">
    <caption style="padding: 14px; font-weight: 700; font-size: 1.1rem; background-color: #5a755a; color: #ffffff; letter-spacing: 0.5px; border-bottom: 2px solid rgba(255, 255, 255, 0.15);">
      Tabela de codificação para o padrão de código de barras UPC-A
    </caption>
    <thead>
      <tr style="background-color: #698b69; border-bottom: 2px solid rgba(255, 255, 255, 0.15);">
        <th rowspan="2" style="padding: 12px 6px; border: 1px solid rgba(255, 255, 255, 0.1); font-weight: 600; text-transform: uppercase; font-size: 0.85rem; letter-spacing: 0.5px;">Zona de Silêncio</th>
        <th rowspan="2" style="padding: 12px 6px; border: 1px solid rgba(255, 255, 255, 0.1); font-weight: 600; text-transform: uppercase; font-size: 0.85rem; letter-spacing: 0.5px;">PORTÃO</th>
        <th colspan="10" style="padding: 12px 6px; border: 1px solid rgba(255, 255, 255, 0.1); font-weight: 700; font-size: 0.9rem; text-transform: uppercase; letter-spacing: 1px;">Bloco de Dados (Esquerda)</th>
        <th rowspan="2" style="padding: 12px 6px; border: 1px solid rgba(255, 255, 255, 0.1); font-weight: 600; text-transform: uppercase; font-size: 0.85rem; letter-spacing: 0.5px;">PORTÃO</th>
        <th colspan="10" style="padding: 12px 6px; border: 1px solid rgba(255, 255, 255, 0.1); font-weight: 700; font-size: 0.9rem; text-transform: uppercase; letter-spacing: 1px;">Bloco de Dados (Direita)</th>
        <th rowspan="2" style="padding: 12px 6px; border: 1px solid rgba(255, 255, 255, 0.1); font-weight: 600; text-transform: uppercase; font-size: 0.85rem; letter-spacing: 0.5px;">PORTÃO</th>
        <th rowspan="2" style="padding: 12px 6px; border: 1px solid rgba(255, 255, 255, 0.1); font-weight: 600; text-transform: uppercase; font-size: 0.85rem; letter-spacing: 0.5px;">Zona de
      silêncio</th>
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
        <td style="padding: 12px 6px; border: 1px solid rgba(255, 255, 255, 0.1); background-color: rgba(255, 255, 255, 0.05);"><img src="../img/UPC-A_Q.png" alt="Quiet Zone" style="width: 27px; height: 241px; display: block; margin: 0 auto;" /></td>
        <td style="padding: 12px 6px; border: 1px solid rgba(255, 255, 255, 0.1);"><img src="../img/UPC-A_S.png" alt="Start" style="width: 10px; height: 245px; display: block; margin: 0 auto;" /></td>
        <!-- L 0-9 -->
        <td style="padding: 12px 6px; border: 1px solid rgba(255, 255, 255, 0.1);"><img src="../img/UPC-A_L0.png" alt="L0" style="width: 20px; height: 235px; display: block; margin: 0 auto;" /></td>
        <td style="padding: 12px 6px; border: 1px solid rgba(255, 255, 255, 0.1);"><img src="../img/UPC-A_L1.png" alt="L1" style="width: 20px; height: 235px; display: block; margin: 0 auto;" /></td>
        <td style="padding: 12px 6px; border: 1px solid rgba(255, 255, 255, 0.1);"><img src="../img/UPC-A_L2.png" alt="L2" style="width: 20px; height: 235px; display: block; margin: 0 auto;" /></td>
        <td style="padding: 12px 6px; border: 1px solid rgba(255, 255, 255, 0.1);"><img src="../img/UPC-A_L3.png" alt="L3" style="width: 20px; height: 235px; display: block; margin: 0 auto;" /></td>
        <td style="padding: 12px 6px; border: 1px solid rgba(255, 255, 255, 0.1);"><img src="../img/UPC-A_L4.png" alt="L4" style="width: 20px; height: 235px; display: block; margin: 0 auto;" /></td>
        <td style="padding: 12px 6px; border: 1px solid rgba(255, 255, 255, 0.1);"><img src="../img/UPC-A_L5.png" alt="L5" style="width: 20px; height: 235px; display: block; margin: 0 auto;" /></td>
        <td style="padding: 12px 6px; border: 1px solid rgba(255, 255, 255, 0.1);"><img src="../img/UPC-A_L6.png" alt="L6" style="width: 20px; height: 235px; display: block; margin: 0 auto;" /></td>
        <td style="padding: 12px 6px; border: 1px solid rgba(255, 255, 255, 0.1);"><img src="../img/UPC-A_L7.png" alt="L7" style="width: 20px; height: 235px; display: block; margin: 0 auto;" /></td>
        <td style="padding: 12px 6px; border: 1px solid rgba(255, 255, 255, 0.1);"><img src="../img/UPC-A_L8.png" alt="L8" style="width: 20px; height: 235px; display: block; margin: 0 auto;" /></td>
        <td style="padding: 12px 6px; border: 1px solid rgba(255, 255, 255, 0.1);"><img src="../img/UPC-A_L9.png" alt="L9" style="width: 20px; height: 235px; display: block; margin: 0 auto;" /></td>
        <!-- M -->
        <td style="padding: 12px 6px; border: 1px solid rgba(255, 255, 255, 0.1);"><img src="../img/UPC-A_M.png" alt="Middle" style="width: 15px; height: 245px; display: block; margin: 0 auto;" /></td>
        <!-- R 0-9 -->
        <td style="padding: 12px 6px; border: 1px solid rgba(255, 255, 255, 0.1);"><img src="../img/UPC-A_R0.png" alt="R0" style="width: 20px; height: 235px; display: block; margin: 0 auto;" /></td>
        <td style="padding: 12px 6px; border: 1px solid rgba(255, 255, 255, 0.1);"><img src="../img/UPC-A_R1.png" alt="R1" style="width: 20px; height: 235px; display: block; margin: 0 auto;" /></td>
        <td style="padding: 12px 6px; border: 1px solid rgba(255, 255, 255, 0.1);"><img src="../img/UPC-A_R2.png" alt="R2" style="width: 20px; height: 235px; display: block; margin: 0 auto;" /></td>
        <td style="padding: 12px 6px; border: 1px solid rgba(255, 255, 255, 0.1);"><img src="../img/UPC-A_R3.png" alt="R3" style="width: 20px; height: 235px; display: block; margin: 0 auto;" /></td>
        <td style="padding: 12px 6px; border: 1px solid rgba(255, 255, 255, 0.1);"><img src="../img/UPC-A_R4.png" alt="R4" style="width: 20px; height: 235px; display: block; margin: 0 auto;" /></td>
        <td style="padding: 12px 6px; border: 1px solid rgba(255, 255, 255, 0.1);"><img src="../img/UPC-A_R5.png" alt="R5" style="width: 20px; height: 235px; display: block; margin: 0 auto;" /></td>
        <td style="padding: 12px 6px; border: 1px solid rgba(255, 255, 255, 0.1);"><img src="../img/UPC-A_R6.png" alt="R6" style="width: 20px; height: 235px; display: block; margin: 0 auto;" /></td>
        <td style="padding: 12px 6px; border: 1px solid rgba(255, 255, 255, 0.1);"><img src="../img/UPC-A_R7.png" alt="R7" style="width: 20px; height: 235px; display: block; margin: 0 auto;" /></td>
        <td style="padding: 12px 6px; border: 1px solid rgba(255, 255, 255, 0.1);"><img src="../img/UPC-A_R8.png" alt="R8" style="width: 20px; height: 235px; display: block; margin: 0 auto;" /></td>
        <td style="padding: 12px 6px; border: 1px solid rgba(255, 255, 255, 0.1);"><img src="../img/UPC-A_R9.png" alt="R9" style="width: 20px; height: 235px; display: block; margin: 0 auto;" /></td>
        <!-- E -->
        <td style="padding: 12px 6px; border: 1px solid rgba(255, 255, 255, 0.1);"><img src="../img/UPC-A_S.png" alt="End" style="width: 10px; height: 245px; display: block; margin: 0 auto;" /></td>
        <td style="padding: 12px 6px; border: 1px solid rgba(255, 255, 255, 0.1); background-color: rgba(255, 255, 255, 0.05);"><img src="../img/UPC-A_Q.png" alt="Quiet Zone" style="width: 27px; height: 241px; display: block; margin: 0 auto;" /></td>
      </tr>
    </tbody>
  </table>
</div>



Cada número precisa usar um bloco de exatamente 7 módulos. A imagem abaixo ilustra bem isso:

<figure markdown="span">
![](./img/numeros.png){ align=center, width="400"}
</figure>

Com isso em mente, a "receita" do número 1 para o lado esquerdo é (3 branco, 2 preto, 1 branco, 1 preto):

$$\text{Branco} - \text{Branco} - \text{Branco} - \text{Preto} - \text{Preto} - \text{Branco} - \text{Preto}$$

Já para o lado direito do código, a receita do número 1 é diferente (basicamente é o inverso, onde era preto fica branco e vice-versa):

$$\text{Preto} - \text{Preto} - \text{Preto} - \text{Branco} - \text{Branco} - \text{Preto} - \text{Branco}$$

---
### Por que existe essa diferença?

A mudança de receita existe por um motivo simples: dar o sentido da direção para o computador, da mesma forma que uma placa de trânsito diz se uma rua é "mão" ou "contramão".

Por exemplo, se o número 1 fosse desenhado igual na esquerda e na direita, a estrada de fatias seria idêntica. Quando o produto passasse de cabeça para baixo, o laser começaria a ler o código pelo lado fim (pela direita) achando que era o começo (a esquerda).

O computador leria todos os números de trás para frente. Em vez de ler o código real do produto, ele leria uma sequência totalmente errada, o sistema não encontraria o preço e o caixa travaria.

É por isso que há esse truque de espelhar a receita de cada número. Assim:

- No Lado Esquerdo: Todos os números (de 0 a 9) foram desenhados com um número ÍMPAR de fatias pretas.

- No Lado Direito: Todos os números foram desenhados com um número PAR de fatias pretas.

Assim, quando o laser cruza o código de barras, a primeira coisa que o software faz é contar a paridade dos blocos de 7 fatias que ele acabou de ler. Se o resultado for ímpar, ele sabe que está lendo o lado esquerdo. Se for par, ele sabe que está lendo o lado direito. Dessa forma, caso esteja sendo lido invertido Em vez de dar um erro e travar o caixa, o computador simplesmente faz uma operação matemática interna: ele espelha e inverte a ordem dos bits na memória, transformando o que ele leu de trás para frente no código correto.

---

