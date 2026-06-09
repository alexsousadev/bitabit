# The Compact UPC-E Model (For Small Packaging)

The entire traditional 12-digit UPC-A structure works perfectly on cereal boxes, soda bottles, or books. But what happens when the product is tiny, like chewing gum, lipstick, or nail polish? The standard code simply doesn't fit on the packaging.

To solve this, GS1 created the **UPC-E**, which is the "compressed" version of the barcode. It has the following differences:

1. **Eliminates excess zeros**: It compresses the zeros in the middle of the barcode using a special numeric compression pattern.
2. **Optimized guards**: It does not have the central guard bars (the middle divider), reducing the physical space required for scanning.
3. **Uses 6 visual digits**: It displays only 6 digits on the label, but the scanner can digitally expand those 6 digits back into the 12 digits of the standard UPC-A before sending the information to the store's system.

Below is a comparative example so you can see the difference in size and appearance:

<figure markdown="span">
  ![](../img/UPC-A%20and%20UPC-E.webp){ align=center, width="500"}
</figure>

> Since the UPC-E has 6 structural digits in its barcode encoding, it has a maximum capacity of 1 million different products ($10^6$ or $1,000,000$).

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

[<span class="nav-title">5) Other Barcode Standards (EAN-13, Code 39 and more)</span> <span class="nav-arrow">➔</span>](./outros-padroes-codigos.en.md)

</div>
