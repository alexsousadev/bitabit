---
date: 2026-02-28
categories:
    - Segurança da Informação
tags:
    - Criptografia
    - RSA
    - Segurança
---

# Como o Algoritmo RSA funciona?



Este post explica os fundamentos que permitem a segurança e o uso do RSA, um dos sistemas de criptografia mais usados e seguros do mundo.



## 1) O que é o RSA?

De forma direta, o RSA é um algoritmo de criptografia assimétrica amplamente usado para proteger dados sensíveis, como em comunicações online e assinaturas digitais. 

Ele foi desenvolvido em 1977 por Ron Rivest, Adi Shamir e Leonard Adleman (daí o nome RSA), revolucionando a segurança digital ao eliminar a necessidade de trocar chaves secretas previamente. 
> O título oficial do trabalho é: ["A Method for Obtaining Digital Signatures and Public-Key Cryptosystems"](https://apps.dtic.mil/sti/citations/ADA606588).

Para entender melhor a importância disso, é necessário entender o que é criptografia.

<figure markdown="span">
![](./img/criptografia.png){ align=center, width="500"}
</figure>

Podemos definir a criptografia como o processo de codificar informações para protegê-las contra acesso não autorizado, transformando dados legíveis (texto simples) em formato ilegível (texto cifrado) usando algoritmos matemáticos. Para tornar os textos ilegíveis, temos basicamente 2 formas:

- **Criptografia simétrica:** uma mesma chave é utilizada para criptografar e descriptografar.

    > Utilizada em VPNs, WPA (Redes Wi-Fi), Criptografia de disco (BitLocker, Veracrypt), entre outros.
    
- **Criptografia assimétrica:** utiliza duas chaves diferentes, uma para criptografar e outra para descriptografar.

    > Utilizada no SSL/TLS (HTTPS), Certificados digitais, PGP/GPG (Criptografia de email), SSH (Acesso remoto seguro), Blockchain, entre outros.


## 2) Entendendo as partes

Então, podemos resumir que, para criptografar alguma coisa, temos a combinação de 2 elementos:

- **Chave**: É o "segredo", ou senha que vai permitir acessar aquela informação.
- **Algoritmo**: É a "estratégia", o cálculo utilizado que vai permitir usar aquela chave para esconder as informações de alguma forma.

Para deixar isso mais claro, podemos usar como exemplo um algoritmo bastante famoso: a [Cifra de César](https://pt.wikipedia.org/wiki/Cifra_de_C%C3%A9sar). Trata-se de um método simples de criptografia usado pelo general romano Júlio César para proteger mensagens militares.

<figure markdown="span">
![](./img/cifra_cesar.png){ align=center, width="500"}
</figure>

Desenvolvida por volta de 50 a.C., essa cifra substitui cada letra do texto pela letra três posições à frente no alfabeto (ex.: A vira D, B vira E). Assim, uma mensagem como **"ATAQUE AO AMANHECER"** com deslocamento 3 vira **"DWDXHDDRDPDQDNHFHU"**. Para decifrar, desloca-se três posições para trás. 

Assim, podemos entender que, nesse caso:

- **Algoritmo:** pegar cada letra e substituí-la pela letra que está *n* posições à frente no alfabeto.
- **Chave:** o número 3. Se mudássemos a chave para 4 ou 5, obteríamos um texto diferente, que só quem soubesse o deslocamento conseguiria decifrar.

> Note que a Cifra de César pode ser considerada uma criptografia simétrica, já que a mesma chave (no caso, o número de deslocamento das posições) é usada para criptografar e descriptografar.

## 3) Entendendo a Criptografia Assimétrica

<figure markdown="span">
![](./img/criptografia_assimetrica.webp){ align=center, width="500"}
</figure>

Nesse modelo, a criptografia é feita usando um par de chaves: chave pública e chave privada. A chave pública pode ser compartilhada com qualquer pessoa, enquanto a chave privada deve ser mantida em segredo (porque só ela consegue acessar os dados).

Um dos algoritmos mais famosos que utilizam essa estratégia é o RSA, no qual estamos focados aqui.

### 3.1) Onde reside a segurança desse método? (O Fundamento Matemático)

Essa criptografia que utilizamos atualmente se baseia no fato de que não temos processamento suficiente para encontrar a chave de criptografia por força bruta (no caso, a chave privada). Isso significa que, se alguém tentar descobrir a chave por tentativa e erro, levaria uma quantidade enorme de anos, tornando o ataque inviável.

O RSA é fundamentado em um ingrediente secreto: números primos. Esses números são considerados os "átomos" da matemática, porque dão origem a todos os outros números.

> Como assim? Qualquer número composto é resultado da multiplicação de primos. Qualquer um. 15 = 3×5, 20 = 5×2×2...

<figure markdown="span">
![](./img/numeros_primos.png){ align=center, width="500"}
</figure>

Por esse motivo, são chamados de blocos de construção da matemática. Eles são os mais estudados pelos matemáticos porque são cobertos de mistérios. Por exemplo, é impossível predizer onde estará o próximo número; houve muitas tentativas ao longo da história, mas todas falharam. Eles parecem ser completamente aleatórios.

E é aí que entra a ideia do RSA: multiplicação de primos. É fácil multiplicar dois números primos, mas é incrivelmente difícil descobrir quais números primos foram usados para formar esse número. Isso é conhecido como uma **função de alçapão** ou uma **função unidirecional**. Embora seja fácil percorrer um caminho, é computacionalmente inviável percorrer o outro caminho.

> Cozinhar um ovo é uma função unidirecional: é fácil ferver um ovo, mas não é possível desfervê-lo.

Tudo começa com dois números primos. No mundo real, eles têm centenas de dígitos; aqui usaremos dois primos pequenos para facilitar o acompanhamento.

---
---
O RSA é classificado em bits, se referindo justamente ao tamanho do resultado da multiplicação dos primos. O mais utilizado atualmente é o **RSA-2048.**

| RSA (bits) | Dígitos de cada primo (aprox.) | Dígitos de n (aprox.) |
|------------|--------------------------------|-----------------------|
| 512 bits   | 77 dígitos                     | 155 dígitos           |
| 1024 bits  | 155 dígitos                    | 309 dígitos           |
| 2048 bits  | 309 dígitos                    | 617 dígitos           |
| 3072 bits  | 463 dígitos                    | 926 dígitos           |
| 4096 bits  | 617 dígitos                    | 1234 dígitos          |
---
---

Nosso primos serão esses:

- ### $p = 5$
- ### $q = 11$

Multiplicamos os dois para obter o **módulo** $n$:

$$
n = p \times q = 5 \times 11 = 55
$$

Em seguida, calculamos o **totiente** — conceito explicado abaixo.

---

### 3.3) O que é o Totiente? (Calculando a Chave Privada)

O totiente é o número que nos permitirá criar a chave privada. Também é conhecido como *“O segredo de Euler”*.

<figure markdown="span">
![](./img/euler.jpg ){ align=center, width="500"}
</figure>

**Euler** foi um matemático suíço que descobriu uma fórmula para calcular esse total — ou seja, o totiente — quando conhecemos a fatoração de $n$.

> **Coprimo:** dois números são coprimos quando o máximo divisor comum (MDC) entre eles é $1$.

Então, podemos definir o totiente de um número n como a quantidade de números menores que n n que são coprimos com n

Por exemplo, qual seria o totiente de 8?

Queremos o número de inteiros entre $1$ e $7$ que são coprimos a $8$. Para isso, calculamos o MDC de $8$ com cada um:

| Número | MDC(8, número) | É coprimo? |
|--------|----------------|------------|
| 1 | 1 | ✓ |
| 2 | 2 | ✗ |
| 3 | 1 | ✓ |
| 4 | 4 | ✗ |
| 5 | 1 | ✓ |
| 6 | 2 | ✗ |
| 7 | 1 | ✓ |

Portanto existem **4** números coprimos a $8$: $1$, $3$, $5$ e $7$. Ou seja, o **totiente de 8 é 4**. Não vamos ter todo esse trabalho massivo, e por isso é que citamos o Euler, pois ele criou uma fórmula para facilitar isso.

Quando $n$ é o produto de dois primos $p$ e $q$, Euler mostrou que o totiente pode ser calculado assim:

$$
\phi(n) = (p - 1) \times (q - 1)
$$

Com nossos valores ($p = 5$, $q = 11$):

$$
\phi(n) = (5 - 1) \times (11 - 1) = 4 \times 10 = 40
$$

Assim, o número 40 é o nosso segredo que deve ser guardado a sete chaves!

### 3.4) Calculando a Chave Pública





---

## Histórico de Evolução

### 2026-02-28 - Fundamentos do RSA
- Entendendo o conceito de criptografia e diferenças da simétrica para assimétrica
- Explicando os fundamentos do algoritmo

### 2026-03-01 - Começando a exploração do Algoritmo
- Introdução ao fundamento matemático (totiente, coprimos)
- Explicando a classificação do RSA

