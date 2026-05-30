# Other Barcode Standards (EAN-13, Code 39 and more)

Although the UPC was the pioneer on supermarket shelves, the need to automate different industries led the tech world to create dozens of other formats.

**Every barcode model in existence today was born to solve a limitation of geography, physical space, or type of information that IBM's original standard couldn't handle on its own.**

<figure markdown="span">
  ![](../img/typesbarcode.jpeg){ align=center, width="500"}
</figure>

---

## 1) EAN-13: The Global Standard

When barcode technology crossed the ocean in 1977, Europe and the rest of the world wanted to adopt it. However, there was a geographical issue: the UPC had been custom-made for the United States and Canada. The rest of the world needed a system that would identify the country of origin of each product in international trade.

To solve this, the **EAN-13** was born. Engineers took the exact same mathematical structure of the UPC we saw earlier, but added a thirteenth ($13^{\text{th}}$) digit to the front of the code to indicate the country.

But then a big problem arose: if computers worldwide began using 13 digits, how would they read the billions of American products that were already printed with the 12-digit UPC?

The solution from GS1 (the global standards organization) was a stroke of mathematical elegance: they turned the number zero ($0$) into the official code for the United States and Canada.

It works like this: in the GS1 global table of countries, the range from `000` to `139` was reserved exclusively for the US and Canada. Therefore, for the international system to read an American 12-digit UPC code, the checkout software automatically places an invisible zero in front of it.

*If we take our previous example code, the UPC-A `036000291452` (12 digits) is read by the global system as `0036000291452` (13 digits).*

And just like that, the mystery was solved in a unified way. That is why today, any computer on the planet reads both formats without locking up:

- If the code has 13 digits and starts between `000` and `139`, the system knows it is a native American code (UPC) adapted with a zero in front.
- If it starts with `789` or `790`, the system knows the company registered the product in Brazil.
- If it starts with `560`, it was registered in Portugal.

> **The Origin Myth:** An important detail to avoid falling for tricks is that this prefix only indicates the country where the company registered its brand, not where the goods were actually manufactured. An American brand can manufacture its t-shirts in China, but the barcode will still start with the US zero.

Following the same portability logic, Europeans also created the **EAN-8**, a reduced 8-digit version used exclusively to label very small packages where a 13-digit code wouldn't fit.

> You can check a complete table of main country prefixes at [GS1 Company Prefix](https://www.gs1.org/standards/id-keys/company-prefix). Wikipedia also organized this list in a slightly more user-friendly way at [List of GS1 country codes](https://en.wikipedia.org/wiki/List_of_GS1_country_codes).

---

## 2) Code 39

Outside of traditional retail, the requirements were different, as industries and shipping carriers needed to register letters and not just numbers. To solve this, **Code 39** was created, the first alphanumeric model in history, widely adopted by the automotive sector and the US Department of Defense due to its high error protection, ideal for large inventories and metal parts.

---

## 3) Code 128

Shortly after, seeking better space efficiency, **Code 128** was developed, a very high-density code that stores letters, numbers, and symbols in a much more compact form, becoming the absolute standard for tracking parcels in global logistics and on corporate ID badges.

---

## 4) Interleaved 2 of 5

To deal with lower-quality printing, such as rough cardboard boxes in warehouses, the **Interleaved 2 of 5** was created, which stores numbers in pairs and has a high tolerance for ink smudging — a feature that made it perfect for banking slips/boleto reading to this day.

---

## 5) Codabar

The **Codabar** was born in 1972 focusing on old thermal printers, using special letters to mark the start and end of the scan, which guaranteed its historical use in blood bank test tubes and library book labels.

---

## 6) PostNet

Finally, even postal services got unique solutions, such as **PostNet**, a peculiar code made of bars of varying heights (short and long) custom-designed by the US postal service to decipher ZIP codes on envelopes and speed up mail sorting at extremely high speed.

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

[<span class="nav-title">6) Implementation Challenges and Skepticism</span> <span class="nav-arrow">➔</span>](./desafios-e-ceticismo.en.md)

</div>
