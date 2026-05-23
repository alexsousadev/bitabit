# Como funciona o dígito verificador do Código de Barras

Para exemplificar, vamos utilizar a mesma imagem:

<div style="text-align: center; margin: 1.5rem 0;">
  <img src="../img/upc_a_normal.svg" alt="Código de barras UPC-A normal" style="background-color: #ffffff; padding: 12px; border-radius: 6px; display: inline-block; width: 200px; box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);" />
</div>




O dígito verificador do UPC-A é calculado seguindo estes passos:

1. **Some os dígitos das posições ímpares** (o 1º, 3º, 5º, 7º, 9º e 11º número).
2. **Multiplique o resultado por 3**.
3. **Some os dígitos das posições pares** (o 2º, 4º, 6º, 8º e 10º número) ao resultado anterior.
4. **Encontre o resto da divisão por 10** (módulo 10) e chame esse valor de $M$.
5. **Descubra o dígito final**: Se $M$ for igual a zero, então o dígito verificador é $0$; caso contrário, o dígito verificador será $10 - M$.

---

## Exemplo Prático de Cálculo

Vamos calcular o dígito desconhecido ($x$) do código de barras de exemplo: **03600029145x** (é os números que ficam embaixo)

* **Passo 1: Somar os dígitos das posições ímpares:**
  $0 + 6 + 0 + 2 + 1 + 5 = 14$

* **Passo 2: Multiplicar o resultado por 3:**
  $14 \times 3 = 42$

* **Passo 3: Somar os dígitos das posições pares ao resultado:**
  $42 + (3 + 0 + 0 + 9 + 4) = 42 + 16 = 58$

* **Passo 4: Encontrar o resto da divisão por 10 (Módulo 10):**
  $58 \pmod{10} = 8 \quad (\text{Portanto, } M = 8)$

* **Passo 5: Como $M$ não é zero, subtraia $M$ de 10:**
  $10 - 8 = 2$

**Resultado:** O dígito verificador ($x$) é **2**. O código completo e válido é **036000291452**. Então, está tudo okay.

Se o valor final da conta matemática não for igual ao último número (o dígito verificador), o sistema do supermercado sabe na hora que houve um erro.