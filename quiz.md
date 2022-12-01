Quiz title: Population Genetics, I

GROUP
pick: 1
```{.python3 .run}
import textwrap

for i in range(1, 5):
    answer=f"2^{i}"
    q=rf"""
    1. How many *genealogical* ancestors do you have ${i}$
       generations ago?

       Express you answer in the form of a base and exponent
       using the following notation: `x^y`, which means "x
       to the power of y", or $x^y$.

       Copyright 2020-2021 Kevin Thornton, licensed under CC BY-NC-SA v4.

    * {answer}
    """
    print(textwrap.dedent(q))
```
END_GROUP

GROUP
pick: 1

```{.python3 .run}
import textwrap

import numpy as np
import custom_rounding

for q in np.arange(1e-2, 0.5, 1e-2):
    qq = float(f"{q:0.2f}")
    answer = custom_rounding.round_half_up_via_decimal(2*qq*(1.0-qq), 4)
    question = rf"""
    1. A single gene has to alleles, $A$ and $a$.  The
       frequency of the $a$ allele in the population
       is ${qq}$.  Under the assumption of Hardy-Weinberg
       Equilibrium, what is the expected frequency
       of the $Aa$ genotype?

       Round your answer to four (4) digits after the decimal
       point.

       Copyright 2020-2021 Kevin Thornton, licensed under CC BY-NC-SA v4.

    = {answer} +- 0.0001
    """

    print(textwrap.dedent(question))
```

END_GROUP

GROUP
pick: 1

1. What is the $p$-value associated with a $\chi^2$ value of 3 and 1 degree of freedom?

   Use the calculator below to determine your answer.

   <iframe width="100%" height="186" frameborder="0" src="https://observablehq.com/embed/@molpopgen/chi-squared-calculator?cells=viewof+chisq_input%2Cviewof+chisq_dof%2Cpv"></iframe>

   Copyright 2020-2021 Kevin Thornton, licensed under CC BY-NC-SA v4.

= 0.0832 +- 0.001

END_GROUP
