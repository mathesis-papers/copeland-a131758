# Three companion transforms

A generating series packs a sequence into one object: the coefficient of $x^n/n!$ holds the $n$th entry. We can multiply or substitute in the series and read off a new sequence, without evaluating an infinite sum. Here the entries are themselves polynomials in $t$. This chapter follows §3 of the [version 2 paper by Haobo Ma and Wenlin Zhang](https://doi.org/10.5281/zenodo.24445683).

## A single series for all the rows

Let $R_n(t)=tP_n(t)/(n!(1-t)^{n+1})$, $G(x,t)=\sum_{n\ge0}P_n(t)x^n/n!$, and $y=x(t-1)$. Let $s_j$ be [A000262](https://oeis.org/A000262), defined by $\sum_{j\ge0}s_ju^j/j!=\exp(u/(1-u))$. Define $E_n$ by $\sum_{v\ge1}v^n t^v=tE_n(t)/(1-t)^{n+1}$, with $E_0=1$. These Eulerian polynomials record the numerators for ordinary powers, where our rows record numerators for Laguerre samples.

::: {.corollary #row-transforms title="Generating series, recurrence and Eulerian transform" mathesis="collected:copeland-a131758:2:s5" status="written-proof" proof="pf-row-transforms" doi="10.5281/zenodo.24445683" source="Corollary 5" request="https://github.com/the-omega-institute/trureturing-requests/issues/467"}
Over $\mathbb Q(t)$, the formal series are

$$
\sum_{n\ge0}R_n(t)z^n=\frac{t}{(1+z)(\exp(-z/(1+z))-t)},\qquad
G(x,t)=\frac{t-1}{(1-y)(t-\exp(y/(1-y)))}.
$$

For $n\ge1$ the modified Riordan recurrence is

$$
P_n(t)=n!(t-1)^n+\sum_{j=0}^{n-1}\binom nj s_{n-j}(t-1)^{n-j-1}P_j(t).
$$

For $n\ge0$ the Eulerian transform is

$$
\frac{E_n(t)}{n!}=\sum_{j=0}^n\binom nj(1-t)^{n-j}\frac{P_j(t)}{j!}.
$$

Its inverse exchanges $E$ with $P$ and uses $(t-1)^{n-j}$ instead. In particular $P_n(-1)=n!\sum_{j=0}^n\binom nj(-2)^{n-j}E_j(-1)/j!$. Polynomial identities hold at removable specializations as well.
:::

::: {.proof #pf-row-transforms}
Summing the ordinary Laguerre coefficients gives $\sum_{n\ge0}L_n(v)(-z)^n=(1+z)^{-1}\exp(vz/(1+z))$. The sample identity says $R_n(t)=\sum_{v\ge1}(-1)^n L_n(v)t^v$. Summing the geometric series in $t\exp(z/(1+z))$ gives the first formula; substituting $z=x(1-t)$ and extracting $G$ gives the second. Clear the factor $t-\exp(y/(1-y))$ in the second formula and read the coefficient of $x^n/n!$ to obtain the recurrence.

Expanding $L_n$ expresses $R_n(t)$ as the alternating binomial transform of $\operatorname{Li}_{-j}(t)/j!$, where $\operatorname{Li}_{-j}(t)=\sum_{v\ge1}v^jt^v$ at the origin. Binomial inversion, followed by replacing these power sums with $tE_j(t)/(1-t)^{j+1}$, gives the displayed forward and inverse transforms. Evaluate the inverse at $t=-1$ for the alternating sum.
:::

## A neighboring table and a misplaced exponent

The rows $A_n(t)$ in [A131202](https://oeis.org/A131202) have exponential generating series $(t-1)/(t-\exp(y/(1-y)))$, with $A_0=1$. Compared with $G$, this simply removes one factor. That small adjustment is enough to detect an exponent error in the printed reconstruction rule.

::: {.corollary #sibling-rows title="Reconstructing the rows from A131202" mathesis="collected:copeland-a131758:2:s6" status="written-proof" proof="pf-sibling-rows" doi="10.5281/zenodo.24445683" source="Corollary 6" request="https://github.com/the-omega-institute/trureturing-requests/issues/468"}
For $n\ge1$, $A_n(t)=P_n(t)-n(t-1)P_{n-1}(t)$; for $n\ge0$,

$$
P_n(t)=\sum_{k=0}^n\binom nk A_{n-k}(t)k!(t-1)^k.
$$

The exponent in the reconstruction is $k$, not $k-1$: the printed rule gives $2$ at $n=1$ in place of $P_1(t)=t$. At $t=2$ the first identity gives $A_n(2)=P_n(2)-nP_{n-1}(2)$ for $n\ge1$ as in [A084358](https://oeis.org/A084358). The matrix $[\binom nk A_{n-k}(2)]_{0\le k\le n}$ is [A133289](https://oeis.org/A133289), with inverse $2I-$[A129652](https://oeis.org/A129652). Also $A_n(1)=n!$ for all $n\ge0$, and for $n\ge1$ the degree is $n-1$ and the leading coefficient is $s_n$.
:::

::: {.proof #pf-sibling-rows}
The series for $A$ is $(1-y)G$. Multiplication by $1-y$ gives the difference formula; multiplication by $1/(1-y)=\sum_{k\ge0}x^k(t-1)^k$ gives its inverse. At $t=2$, the series becomes $1/(2-\exp(x/(1-x)))$. Its reciprocal $2-\exp(x/(1-x))$ gives the inverse matrix, since multiplication of exponential series is binomial convolution. Its constant term is $1$, and the $n$th exponential coefficient for $n>0$ is $-s_n$. At $t=1$, the difference formula reduces to $P_n(1)=n!$. To see the degree and leading term, write $S=\exp(y/(1-y))$. After $x\mapsto x/t$, the series for $A$ is $1+(S-1)/(t-S)$, and $S$ tends coefficientwise to $\exp(x/(1-x))$. For each $n>0$, $A_n(t)/t^{n-1}$ therefore tends to $s_n\ne0$. Since the $A_n$ are polynomials, this gives both claims.
:::

## Ordered partitions need a factor of one half

Let $F_n$ count partitions of an $n$-element set into an **ordered** list of nonempty blocks, [A000670](https://oeis.org/A000670): $\sum F_nz^n/n!=1/(2-e^z)$. There is one ordered partition of the empty set. Define $b_n=(-1)^nF_n$.

::: {.corollary #signed-bell title="Signed ordered Bell numbers and reciprocal transforms" mathesis="collected:copeland-a131758:2:s7" status="written-proof" proof="pf-signed-bell" doi="10.5281/zenodo.24445683" source="Corollary 7" request="https://github.com/the-omega-institute/trureturing-requests/issues/469"}
For $n\ge0$, the sequences $b_n$ and $P_n(2)$ are exchanged by the parameter-zero Laguerre transform

$$
(\mathcal T_0 u)_n=\sum_{j=0}^n(-1)^j\frac{n!}{j!}\binom nj u_j.
$$

With rational continuation, $b_n=-\tfrac12\operatorname{Li}_{-n}(2)$, not $-\operatorname{Li}_{-n}(2)$. Also $P_n(2)/n!=(-1)^{n+1}R_n(2)/2$.
:::

::: {.proof #pf-signed-bell}
More generally, replacing $\binom nj$ by $\binom{n+\alpha}{n-j}$ sends the exponential series $f(z)$ of $u$ to $(1-z)^{-\alpha-1}f(-z/(1-z))$. The substitution undoes itself and the prefactors cancel when applied twice. At $\alpha=0$, applying it to $1/(2-e^{-z})$ gives $G(z,2)$, proving both directions. On the other hand $\sum -\operatorname{Li}_{-n}(2)z^n/n!=2/(2-e^{-z})$ by continuing the geometric sum in $te^z$ to $t=2$. Comparing coefficients gives the half factor, visible already at $n=0$. The last formula comes from substituting $t=2$ in the definition of $R_n$.
:::

These are identities of formal series or polynomials, with rational continuation where specified; they do not settle analytic interpolation or other conjectures about neighboring sequences. To contribute a proof in Lean, coordinate in the linked request and open a focused PR from a contributor fork to [trureturing's upstream development branch](https://github.com/the-omega-institute/trureturing/blob/dev/docs/CONTRIBUTING.md).
