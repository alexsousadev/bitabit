# How the Barcode Check Digit Works

For this example, let's use the same image:

<div style="text-align: center; margin: 1.5rem 0;">
  <img src="../../img/upc_a_normal.svg" alt="Normal UPC-A barcode" style="background-color: #ffffff; padding: 12px; border-radius: 6px; display: inline-block; width: 200px; box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);" />
</div>

The UPC-A check digit is calculated by following these steps:

1. **Sum the digits in the odd positions** (the 1st, 3rd, 5th, 7th, 9th, and 11th numbers).
2. **Multiply the result by 3**.
3. **Sum the digits in the even positions** (the 2nd, 4th, 6th, 8th, and 10th numbers) to the previous result.
4. **Find the remainder of the division by 10** (modulo 10) and call this value $M$.
5. **Find the final digit**: If $M$ is equal to zero, then the check digit is $0$; otherwise, the check digit will be $10 - M$.

---

## Practical Calculation Example

Let's calculate the unknown digit ($x$) of the example barcode: **03600029145x** (these are the numbers at the bottom)

* **Step 1: Sum the digits in the odd positions:**
  $0 + 6 + 0 + 2 + 1 + 5 = 14$

* **Step 2: Multiply the result by 3:**
  $14 \times 3 = 42$

* **Step 3: Sum the digits in the even positions to the result:**
  $42 + (3 + 0 + 0 + 9 + 4) = 42 + 16 = 58$

* **Step 4: Find the remainder of the division by 10 (Modulo 10):**
  $58 \pmod{10} = 8 \quad (\text{Therefore, } M = 8)$

* **Step 5: Since $M$ is not zero, subtract $M$ from 10:**
  $10 - 8 = 2$

**Result:** The check digit ($x$) is **2**. The complete and valid code is **036000291452**. So, everything is correct.

If the final value of the mathematical calculation does not match the last number (the check digit), the supermarket system immediately knows there was an error.

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

[<span class="nav-title">4) The Compact UPC-E Model</span> <span class="nav-arrow">➔</span>](./modelo-upc-e.en.md)

</div>
