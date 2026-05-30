# O Modelo Compacto UPC-E (Para Embalagens Pequenas)

Toda a estrutura tradicional do UPC-A de 12 dígitos funciona perfeitamente em caixas de cereal, garrafas de refrigerante ou livros. Mas o que acontece quando o produto é minúsculo, como um chiclete, um batom ou um esmalte? O código padrão simplesmente não cabe na embalagem.

Para resolver isso, a GS1 criou o **UPC-E**, que é a versão "compactada" do código de barras. Ele possui as seguintes diferenças:

1. **Elimina os zeros excedentes**: Ele compacta os zeros no meio do código de barras usando um padrão de compressão numérico especial.
2. **Portões otimizados**: Ele não possui as barras de portão centrais (o divisor do meio), reduzindo o espaço físico necessário para a leitura.
3. **Usa 6 dígitos visuais**: Ele exibe apenas 6 dígitos no rótulo, mas o scanner consegue expandir digitalmente esses 6 dígitos de volta para os 12 dígitos do padrão UPC-A antes de enviar a informação ao sistema da loja.

Abaixo temos um exemplo comparativo para você notar a diferença de tamanho e visual:

<figure markdown="span">
  ![](../img/UPC-A%20and%20UPC-E.webp){ align=center, width="500"}
</figure>

> Já que o UPC-E possui 6 dígitos estruturais na sua codificação de barras, ele possui uma capacidade máxima de 1 milhão de produtos diferentes ($10^6$ ou $1.000.000$).

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

[<span class="nav-title">4) Outros Padrões do Mercado (EAN-13, Code 39 e mais)</span> <span class="nav-arrow">➔</span>](./outros-padroes-codigos.md)

</div>
