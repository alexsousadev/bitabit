# The History of the Barcode: How It All Began

The idea was not born in a high-tech lab, but rather in a hallway conversation in 1948, in the United States. Bernard Silver, a student at the Drexel Institute in Philadelphia, overheard the president of a supermarket chain begging a college director for an automated system that would speed up checkout lines and control inventory. But what was the problem?

Back then, checkout operators had to look at each product, identify the price printed or stickered on the packaging, and manually type it, digit by digit, into mechanical cash registers. This fast, repetitive mechanical movement, done thousands of times a day, caused many cashiers to develop chronic health issues, with [carpal tunnel syndrome](https://share.google/aimode/mvH9ppXfqoA0GWQ3w) being the most common and painful (an inflammation of the wrist nerves caused by repetitive strain).

<figure markdown="span">
  ![](../img/caixa_passado.webp){ align=center, width="500"}
</figure>

Since the process depended entirely on the speed of human typing, supermarket lines were massive, creating huge operational bottlenecks for store owners.

Bernard ran to tell his friend, Norman Joseph Woodland. Woodland became obsessed with the problem. He moved to Florida to focus on a solution, and one day on the beach, he started drawing the dots and dashes of Morse Code (a technology he knew well from his time as a Boy Scout) in the sand. But what was that?

---

## What is Morse Code?

For context, Morse Code is essentially the grandfather of the binary code we use today: it translates letters and numbers into just two impulses (one short, one long). Created in the 1830s by Samuel Morse, this system was designed to transmit messages over distances using the telegraph (a device that sent electrical impulses through a wire). Since human voice or written letters couldn't be sent over the wire, Morse created an alphabet based on just two types of audio or electrical signals:

- The Dot ($\cdot$): A quick, short signal.
- The Dash ($-$): A signal that lasts three times longer than a dot.

By combining these dots and dashes, you can write any word:

<figure markdown="span">
  ![](../img/codigo-morse.jpg){ align=center, width="500"}
</figure>

---

Back on the beach, Bernard's big breakthrough was: What if, instead of dots and dashes, I pull these marks downwards, turning them into thin and thick vertical lines?

By doing this, Woodland realized that a beam of light (which would later become the laser) could pass over those lines and read the reflection: the black lines would absorb the light and the white spaces would reflect it back, generating an electrical signal corresponding to a sequence of numbers.

<figure markdown="span">
  ![](../img/praia.png){ align=center, width="500"}
</figure>

In 1952, they patented the idea. However, the first commercial barcode was not a straight line; it was circular! It looked like a bullseye. They designed it this way because they thought it would be easier for the cashier to pass the product in any direction over the scanner.

The image below shows the exact technical drawing from the official patent document. Notice that they included a very important note at the bottom of the drawing: "Lines 6, 7, 8, and 9 are less reflective than lines 10". In other words, the concept of using differences in light reflection (dark lines absorbing light vs. light spaces reflecting it) to generate digital data was born right there.

<figure markdown="span">
  ![](../img/patente_inicial.jpeg){ align=center, width="500"}
</figure>

> You can view the full patent on Google Patents ([US2612994A](https://patents.google.com/patent/US2612994A/en))

The idea was brilliant, but it was ahead of its time. 1950s computers were massive, lasers did not exist yet, and the technology to read those lines cheaply simply wasn't available. The patent was forgotten for a while.

The game only started to change in late 1969. The checkout line problem escalated so much that the largest retail associations in the United States joined forces and hired the famous consulting firm McKinsey & Company. Together, they founded a committee called the Uniform Product Code Council (UPCC). The mission was clear: define a standard numeric format and challenge technology companies to create, from scratch, a visual symbol that could be read by machines.

> This would later be called the UPC (Universal Product Code).

This kicked off a fierce competition in Silicon Valley. Tech giants like RCA, Singer, Pitney Bowes, and IBM itself set up secret labs to design competitive proposals to present to the committee.

## The Birth of the UPC by George Laurer

At that time, engineer Heard Baumeister presented two linear code formulas that IBM had in its archives, named Delta A and Delta B.

The Delta B version tried to calculate information by comparing the exact width of the black bar with the width of the white space. It was a disaster in testing: if the printing press applied slightly too much pressure or ink, the black line blurred outwards (*ink spread*), swallowing the white space, and the computer misread it.

That's when, in mid-1971, another IBM engineer named William "Bill" Crouse had a stroke of genius and invented a new code called Delta C. Instead of measuring the thickness of the entire black line, Delta C's mathematics measured only the distance from the leading (left) edge of one line to the leading edge of the next line.

This change changed everything: if the print blurred and made the black line thicker, it would grow equally on both sides, but the distance between the start of one line and the start of the next would remain mathematically identical. The code became immune to ink bleeding.

> Unfortunately, there are no websites or direct links exclusively dedicated to Delta B and Delta C documentation, as they were only internal IBM codifications. But the Delta C code, which solved the blurring problem by measuring "edge-to-edge", was patented by William Crouse in 1971 and can be accessed at [US Patent US3723710A](https://patents.google.com/patent/US4533825A/en28)

### The Circle vs. The Straight Line

Even with Delta C's math working, the industry was still obsessed with the circular code (the "bullseye"). Competitors like RCA and Litton Industries insisted the circle was better because the cashier could swipe the product in any direction over the scanner window.

However, Baumeister and George Laurer proved that circles were impossible to print at high speeds without warping. If the printing press ran fast, the circle turned into an ellipse (an oval shape) and the scanner failed.

This was because 1970s printing presses used rotary drums running at very high speeds. The main technical issue was that ink smeared in the direction of the press movement — a phenomenon known in the printing industry as *ink slurring* or *press gain*. The pressure and continuous movement of the roller caused the wet ink to slightly "run" forward or backward in the direction the paper was traveling.

<figure markdown="span">
  ![](../img/rotative_print.jpg){ align=center, width="300"}
</figure>

With straight lines, Laurer realized that the machine's blur would only make the vertical lines slightly taller or longer, but the exact width of each one (which is where the information is stored) would remain identical. The next day, he suggested something even better: splitting the barcode into two halves (left side and right side).

With these two proposals, they managed to reduce the barcode size to a third of RCA's circular "bullseye". Laurer took Bill Crouse's Delta C logic and shrank the final label size to just $38\text{ mm} \times 23\text{ mm}$. This was the visual birth of the barcode we know today.

### The "Magic Ring" and Approval

To convince IBM's board and the supermarket committee that this small piece of straight lines actually worked, Bill Crouse built a prototype ring-scanner that was worn on the finger, connected to a wrist strap.

On December 1, 1972, the team presented the project in Minnesota. During the meeting, Crouse used his "magic ring" to read the printed codes. To shock the executives, he swiped the scanner over a worn, poorly printed magazine photo full of two-dimensional flaws. The scanner worked perfectly on almost every try. The robustness of IBM's mathematics crushed the competition.

To make the system 100% secure against fraud, mathematician David Savir and George Laurer added the rule of inverting colors on the right side so the computer could identify if the product was scanned upside down.

> This detail will be explained in more depth in the topic on the [Mathematical Anatomy of the UPC](./anatomia-matematica-upc.md).

Finally, an MIT scientist named Murray Eden suggested the human touch: placing human-readable numbers at the bottom of the design, serving as a fail-safe in case the optical reader broke.

---

For curiosity, the image below shows the competitor designs that Laurer (IBM) defeated. Historical records preserved the exact visual concepts presented to the UPCC committee:

<figure markdown="span">
  ![](../img/concorrencia.jpeg){ align=center, width="500"}
</figure>

Although Crouse's ring scanner was the ultimate portability argument to convince IBM's board that the technology worked simply and quickly, it was the printing engineering of the straight lines that won over the committee.

---

## The First "Beep"

The first product scanned in history was not a large box or an expensive item, but a single pack of Wrigley's Juicy Fruit chewing gum (tutti-frutti flavor). This event occurred on June 26, 1974, at 8:01 AM, at a supermarket called Marsh's Supermarket in Troy, Ohio (USA). The cashier who did the honors was Sharon Buchanan, and the customer was Clyde Dawson. Dawson came to the register with a cart full of items but pulled the gum out first for the historic test. The scanner (developed by Spectra-Physics using IBM's linear code technology) read the code on the first try with a clean "beep". Below is the photo of the chewing gum and the first scanner used.

<figure markdown="span">
  ![](../img/primeirp_beep.jpeg){ align=center, width="500"}
</figure>

<figure markdown="span">
  ![](../img/scanner1.png){ align=center, width="500"}
</figure>

> The success was so significant that today, [a replica of this original scanner and one of the gum packs from that same 1974 batch are preserved and on display at the prestigious Smithsonian Museum (the National Museum of American History) in Washington, D.C.](https://www.si.edu/object/supermarket-scanner:nmah_892778)

The choice was not accidental. The supermarket committee and the engineers wanted to prove a crucial point: if the optical scanner and the printer could work perfectly on a tiny, cylindrical, wrinkled, plastic-wrapped pack of gum that cost only 67 cents, it would work on anything else on the planet.

### Has it always made a sound?

No. The "beep" was introduced in 1974 for psychological and efficiency reasons. In the early tests, the scanners were silent. This forced cashiers to stop and look at the screen for every single product to make sure the price registered, which slowed down the lines.

To solve this, engineers added a small speaker to the scanner with a simple rule: if the check digit calculation was correct, the machine emitted a short sound.

The beep is the computer saying: "The math checks out, the price is registered. You can scan the next one."

The sound is a high-pitched click (between 2 kHz and 4 kHz) because that is the frequency range the human ear detects best, allowing the employee to isolate the sound even amid supermarket noise.

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

[<span class="nav-title">2) The Mathematical Anatomy of the UPC</span> <span class="nav-arrow">➔</span>](./anatomia-matematica-upc.en.md)

</div>
