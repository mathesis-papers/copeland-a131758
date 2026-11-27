# Why do these polynomial rows share only 1 or 2?

The coefficients of $4-14t+10t^2+6t^3$ are $4,-14,10,6$. Their greatest common divisor is $2$: you can divide the whole row by $2$, but not by any larger positive integer. This gcd is called the polynomial's **content**. Signs don't affect it, and neither do any zero coefficients. This example is row $3$ of Tom Copeland's table [OEIS A131758](https://oeis.org/A131758).

Copeland proposed a shortcut. At positive row number $n$, count the positive divisors $d$ of $n$ with $d^2\le n$, and call the count $D(n)$. At $n=8$ only $1$ and $2$ qualify, so the shortcut predicts $2$. But the first two coefficients are $6209$ and $-41417$ in G. C. Greubel's [table](https://oeis.org/A131758/b131758.txt). Already $-6417\cdot6209-962\cdot(-41417)=1$. A factor common to the *whole* row would divide that combination. Hence the content is $1$, whatever the other seven coefficients are. Can we replace the shortcut by one rule that works every time?

::: {.film src="001-content"}
:::

## From a row to samples

Set

$$
B_n(x)=\sum_{j=0}^{n}(-1)^{n+j}\binom nj\frac{n!}{j!}x^j.
$$

This is the ordinary Laguerre polynomial multiplied by $(-1)^n n!$. The coefficient of $x^n$ is $1$, and $n!/j!$ is an integer. Sample $B_n$ at $1,2,3,\ldots$. Copeland's row is built by weighted differences of these samples:

$$
P_n(t)=\sum_{m=0}^n a(n,m)t^m,\qquad
a(n,m)=\sum_{k=0}^m(-1)^k\binom{n+1}{k}B_n(m-k+1).
$$

::: {.proposition #row-bridge title="The row and its fixed divisor" mathesis="collected:copeland-a131758:2:s1" status="written-proof" proof="pf-row-bridge" doi="10.5281/zenodo.24445683" source="Proposition 1" request="https://github.com/the-omega-institute/trureturing-requests/issues/463"}
For all $n\ge0$, $P_n$ is integral, has degree $n$ and leading coefficient $n!$, and $P_n(1)=n!$. As a formal power series,

$$
P_n(t)=(1-t)^{n+1}\sum_{r\ge0}B_n(r+1)t^r,\qquad
c_n=\gcd\{B_n(v):v\in\mathbb Z_{>0}\},
$$

where $c_n$ is the content of $P_n$.
:::

::: {.proof #pf-row-bridge}
Taking a forward difference $f(x+1)-f(x)$ lowers the degree by one and multiplies the leading coefficient by the old degree. Thus the $n$th difference of $B_n$ is $n!$, and the next is zero. Multiplying the sample series by $(1-t)^{n+1}$ produces the defining coefficients through degree $n$; every later coefficient is a full $(n+1)$st difference and vanishes. At degree $n$ the one omitted term in the full difference at $0$ is $(-1)^{n+1}B_n(0)$, so the coefficient is $(-1)^n B_n(0)=n!$. The coefficient of $t^n$ in $P_n(t)/(1-t)$ is the row sum; expanding $(1-t)^n$ times the sample series makes it the $n$th difference at $1$, also $n!$.

Any divisor common to the samples still divides their integer combinations. Conversely, the formal inverse $(1-t)^{-n-1}$ has integer coefficients, so every sample is an integer combination of the row entries. The common divisors therefore agree in both directions; no convergence assumption is needed.
:::

## Look for one sample that escapes each prime

For instance $B_3(x)=x^3-9x^2+18x-6$. The samples $B_3(1)=4$ and $B_3(3)=-6$ are enough to bound the gcd above by $2$. To get equality one must still show that *every* sample is even. The general argument turns those two tasks—finding a witness and proving universal divisibility—into arithmetic with remainders.

::: {.theorem #exact-content title="Exact contents" mathesis="collected:copeland-a131758:2:s2" status="written-proof" proof="pf-exact-content" doi="10.5281/zenodo.24445683" source="Theorem 2" request="https://github.com/the-omega-institute/trureturing-requests/issues/464"}
The content $c_n$ is $1$ for $n=0,1$ and every even $n$. It is $2$ for every odd $n\ge3$.
:::

::: {.proof #pf-exact-content}
**Odd primes.** For a prime $p$ divide $n$ with remainder: $n=qp+r$, $0\le r<p$. The factorial quotient kills the terms with $j<qp$ modulo $p$. For $j=qp+s$, comparing coefficients in $(1+z)^n\equiv(1+z^p)^q(1+z)^r$ replaces $\binom n{qp+s}$ by $\binom rs$; the factorial quotient becomes $r!/s!$ and the sign is unchanged. This gives Carlitz's congruence $B_n(x)\equiv x^{qp}B_r(x)\pmod p$.

Among the $p-1$ nonzero remainders, the factor $x^{qp}$ is never zero. For odd $p$, if $r<p-1$, a monic polynomial of degree $r$ cannot vanish at all $p-1$ of them: each distinct root consumes one linear factor. If $r=p-1$, vanishing at all of them would force $B_r=x^{p-1}-1$ modulo $p$ by monicity and Fermat's little theorem. But the coefficient of $x^{p-2}$ in $B_r$ is $-(p-1)^2\equiv-1$, not $0$. In either case a positive representative supplies a sample not divisible by $p$.

**The prime $2$.** For $n\ge2$, modulo $2$ only the two highest coefficients can survive, and the second is $-n^2$. For even $n$, $B_n(x)\equiv x^n$ and the sample at $1$ is odd. For odd $n\ge3$, $x^{n-1}(x+1)$ vanishes on both remainders. All samples are even.

**But not $4$.** For odd $n\ge3$, modulo $4$ only the highest four terms can contribute. Their coefficients are $1,-n^2,n^2(n-1)^2/2,-n^2(n-1)^2(n-2)^2/6$. The last two reduce to $0,0$ or $2,2$ according as $n\equiv1$ or $3\pmod4$. At $x=3$ the corresponding powers are $3$ and $1$ modulo $4$, so the two contributions sum to zero. The top two contribute $3-1=2$. Thus $B_n(3)\equiv2\pmod4$. With the odd primes already excluded this gives $c_n=2$. The initial rows are $P_0=1$ and $P_1=t$.
:::

## What the shortcut gets right

::: {.corollary #agreement title="When the divisor counts agree" mathesis="collected:copeland-a131758:2:s3" status="written-proof" proof="pf-agreement" doi="10.5281/zenodo.24445683" source="Corollary 3" request="https://github.com/the-omega-institute/trureturing-requests/issues/465"}
For $n>0$, $c_n=D(n)$ exactly at $n=1,2$ and odd $n$ of the form $p^2,p^3,pq$, with odd primes $p,q$ distinct in the product $pq$. The shifted equation $c_n=D(n+1)$ holds exactly at $n=0,1$, at even $n\ge2$ with $n+1$ prime, and at odd $n=3,7,2q-1$ for odd primes $q$ in the last family. Both equations fail at every $n=6s+8$, $s\ge0$.
:::

::: {.proof #pf-agreement}
Pair each divisor of $u$ with $u/d$, leaving a square root unpaired if it exists. Hence $D(u)=\lceil\tau(u)/2\rceil$, where $\tau(u)$ counts all positive divisors. In the factorization of $u$, an exponent $a$ supplies $a+1$ choices for a divisor. Therefore $D=1$ means $1$ or a prime, and $D=2$ means a prime square, prime cube, or two distinct primes multiplied. Match those two lists to the content formula. In the shifted odd case $n+1$ is even, so the second list reduces to $4,8,2q$. If $n=6s+8$, then $n$ is even composite and $n+1$ is a multiple of $3$ at least $9$, so both counts exceed $c_n=1$.
:::

The shift is a comparison, not a conjecture attributed to Copeland. Knowing the gcd does not tell us which coefficients are odd. For that we can keep the entire polynomial while reducing each coefficient modulo two.

::: {.corollary #row-parity title="Parity of the whole row" mathesis="collected:copeland-a131758:2:s4" status="written-proof" proof="pf-row-parity" doi="10.5281/zenodo.24445683" source="Corollary 4" request="https://github.com/the-omega-institute/trureturing-requests/issues/466"}
Modulo $2$, $P_n(t)=(1+t)^{n-1}$ for even $n\ge2$, and $P_n(t)=0$ for odd $n\ge3$.
:::

::: {.proof #pf-row-parity}
For even $n\ge2$ the sampled series reduces to $1+0t+t^2+0t^3+\cdots=1/(1-t)^2$ in characteristic two. Multiplying by $(1-t)^{n+1}$ gives $(1+t)^{n-1}$. For odd $n\ge3$ every sample is even, so the reduced series is zero.
:::

## What has been shown, and by whom?

The [version 2 paper](https://doi.org/10.5281/zenodo.24445683) by Haobo Ma and Wenlin Zhang gives the all-index proofs. [Carlitz's earlier polynomial congruence](https://doi.org/10.1007/BF01180274) (Theorem 3, equation (4.8)) is the source of the prime step; [Krylov and Li](https://math.colgate.edu/~integers/q57/q57.pdf) later gave a direct proof. Peter Bala's congruence in [A009940](https://oeis.org/A009940) concerns the constant column, with $a(n,0)=(-1)^n n!L_n(1)$; the row result controls all coefficients.

The [frozen Lean counterexample](https://github.com/the-omega-institute/trureturing/blob/742ce086eb9c8e6e36cde0fcdf712f63260c045c/D5/S0/Certificates/CopelandA131758PolynomialContentRefutation.lean) checks that the *joint* assertion of integer realizations for all rows and Copeland's proposed gcd for all positive rows cannot hold. It uses row $8$ under the joint assertion; it neither proves integrality for all rows nor proves the universal replacement formula. The [formalization request for the replacement formula](https://github.com/the-omega-institute/trureturing-requests/issues/464) tracks that distinct mathematical statement. The [next chapter](transforms.md) explains companion identities, not a solution to the unrelated operational, Bessel, zeta or complex-interpolation formulas mentioned in the source.

The English seminar deck follows the same argument, with speaker notes for the steps involving remainders.

::: {.slides src="seminar"}
:::
