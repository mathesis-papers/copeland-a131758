# 这些多项式的系数为何只公有因数 1 或 2？

多项式 $4-14t+10t^2+6t^3$ 的系数为 $4,-14,10,6$。它们的最大公因数是 $2$：整行都能除以 $2$，却不能同时除以更大的正整数。这个最大公因数称为多项式的**内容**，系数有正有负或等于零都无妨。这个例子是 Tom Copeland 在 [OEIS A131758](https://oeis.org/A131758) 中所列数表的第 $3$ 行。

Copeland 曾提出一种简便算法：对正行号 $n$，把满足 $d^2\le n$ 的正因数 $d$ 数一遍，记为 $D(n)$。当 $n=8$ 时，只有 $1,2$ 合格，算法预测内容是 $2$。但 G. C. Greubel 的[数表](https://oeis.org/A131758/b131758.txt)给出的前两项是 $6209$ 和 $-41417$，并且 $-6417\cdot6209-962\cdot(-41417)=1$。整行的公因数也必须整除这个组合，所以即使不看另外七项，也知道该行的内容是 $1$。有没有一条对每一行都成立的规则？

::: {.film src="001-content"}
:::

## 从系数行到取样值

令

$$
B_n(x)=\sum_{j=0}^{n}(-1)^{n+j}\binom nj\frac{n!}{j!}x^j.
$$

它是普通 Laguerre 多项式乘以 $(-1)^n n!$。最高项 $x^n$ 的系数为 $1$，且 $n!/j!$ 是整数。在 $1,2,3,\ldots$ 处取样，再把样本做带权差分，就得到 Copeland 的系数行：

$$
P_n(t)=\sum_{m=0}^n a(n,m)t^m,\qquad
a(n,m)=\sum_{k=0}^m(-1)^k\binom{n+1}{k}B_n(m-k+1).
$$

::: {.proposition #row-bridge title="系数行与固定因数" mathesis="collected:copeland-a131758:2:s1" status="written-proof" proof="pf-row-bridge" doi="10.5281/zenodo.24445683" source="Proposition 1" request="https://github.com/the-omega-institute/trureturing-requests/issues/463"}
对所有 $n\ge0$，$P_n$ 的系数都是整数，次数为 $n$，首项系数为 $n!$，且 $P_n(1)=n!$。作为形式幂级数，

$$
P_n(t)=(1-t)^{n+1}\sum_{r\ge0}B_n(r+1)t^r,\qquad
c_n=\gcd\{B_n(v):v\in\mathbb Z_{>0}\},
$$

其中 $c_n$ 为 $P_n$ 的内容。
:::

::: {.proof #pf-row-bridge}
取一次前向差分 $f(x+1)-f(x)$，次数降一，首项系数乘以原次数。所以 $B_n$ 的第 $n$ 次差分恒为 $n!$，再差分一次就变成零。把取样级数乘以 $(1-t)^{n+1}$，直到 $t^n$ 的系数都恰好是定义中的和；更高项是完整的第 $n+1$ 次差分，因而消失。计算 $t^n$ 项时，与 $0$ 处的完整差分相比，只少了 $(-1)^{n+1}B_n(0)$，所以该系数为 $(-1)^nB_n(0)=n!$。而 $P_n(t)/(1-t)$ 的 $t^n$ 系数就是整行之和；用 $(1-t)^n$ 乘以样本级数，也看出它等于 $1$ 处第 $n$ 次差分，即 $n!$。

样本的公因数整除其所有整数组合。反过来，形式逆 $(1-t)^{-n-1}$ 的系数也都是整数，因此每个样本又是行系数的整数组合。两边公因数完全相同，无须假设级数收敛。
:::

## 每个素数只需找一个例外

例如 $B_3(x)=x^3-9x^2+18x-6$。$B_3(1)=4$、$B_3(3)=-6$ 已足以把最大公因数限制在 $2$ 以内。要断定它正好是 $2$，还要证明**每个**样本都是偶数。一般情形也分为找反例和证明普遍整除两步，都可以用余数来做。

::: {.theorem #exact-content title="内容的精确公式" mathesis="collected:copeland-a131758:2:s2" status="written-proof" proof="pf-exact-content" doi="10.5281/zenodo.24445683" source="Theorem 2" request="https://github.com/the-omega-institute/trureturing-requests/issues/464"}
当 $n=0,1$ 或 $n$ 为偶数时，内容 $c_n=1$；当 $n\ge3$ 为奇数时，$c_n=2$。
:::

::: {.proof #pf-exact-content}
**先排除奇素数。** 对素数 $p$，带余除法给出 $n=qp+r$、$0\le r<p$。若 $j<qp$，阶乘商含有因数 $p$，这一项模 $p$ 为零。若 $j=qp+s$，比较 $(1+z)^n\equiv(1+z^p)^q(1+z)^r$ 的系数，把 $\binom n{qp+s}$ 换成 $\binom rs$；阶乘商也化成 $r!/s!$，符号不变。这就得到 Carlitz 的同余式 $B_n(x)\equiv x^{qp}B_r(x)\pmod p$。

在 $p-1$ 个非零余数上，$x^{qp}$ 从不为零。若奇素数 $p$ 满足 $r<p-1$，则首项系数为 $1$ 的 $r$ 次多项式不可能在这些余数上全为零，因为每个不同的根都需要一个一次因子。若 $r=p-1$，首项系数和费马小定理说明：若全为零，$B_r$ 模 $p$ 必等于 $x^{p-1}-1$。但 $B_r$ 的 $x^{p-2}$ 项系数为 $-(p-1)^2\equiv-1$，不是零。因此总能挑一个正整数样本，不被 $p$ 整除。

**再看素数 $2$。** 当 $n\ge2$ 时，模 $2$ 只有最高两项可能留下来，次高项系数为 $-n^2$。偶数行化为 $x^n$，在 $1$ 处取到奇数；对于奇数 $n\ge3$，$x^{n-1}(x+1)$ 在两个余数上都为零，所以样本全为偶数。

**最后排除 $4$。** 当 $n\ge3$ 为奇数，模 $4$ 只需考虑最高四项，系数依次为 $1,-n^2,n^2(n-1)^2/2,-n^2(n-1)^2(n-2)^2/6$。后两项的系数在 $n\equiv1$ 或 $3\pmod4$ 时分别化为 $0,0$ 或 $2,2$。取 $x=3$，相应的幂模 $4$ 为 $3,1$，所以后两项的贡献相加为零。最高两项的贡献为 $3-1=2$，得到 $B_n(3)\equiv2\pmod4$。由于奇素数也已排除，故此时 $c_n=2$。初始行是 $P_0=1$、$P_1=t$。
:::

## 原算法在何时凑巧正确？

::: {.corollary #agreement title="与因数个数吻合的行号" mathesis="collected:copeland-a131758:2:s3" status="written-proof" proof="pf-agreement" doi="10.5281/zenodo.24445683" source="Corollary 3" request="https://github.com/the-omega-institute/trureturing-requests/issues/465"}
对 $n>0$，$c_n=D(n)$ 当且仅当 $n=1,2$，或 $n$ 为形如 $p^2,p^3,pq$ 的奇数，其中 $p,q$ 是奇素数，且在乘积 $pq$ 中互不相同。移位等式 $c_n=D(n+1)$ 成立的行号恰为 $0,1$，满足 $n+1$ 为素数的偶数 $n\ge2$，以及奇数 $3,7,2q-1$（最后一类中 $q$ 是奇素数）。对任意 $s\ge0$，$n=6s+8$ 处两个等式都不成立。
:::

::: {.proof #pf-agreement}
把 $u$ 的因数 $d$ 与 $u/d$ 配对，若有平方根，则它单独一组。因此 $D(u)=\lceil\tau(u)/2\rceil$，其中 $\tau(u)$ 是正因数总数。素因数分解中指数 $a$ 为因数提供 $a+1$ 种选择，于是 $D=1$ 对应 $1$ 或素数，$D=2$ 对应素数的平方、立方或两个不同素数的乘积。将两组与内容公式对照即可；在移位等式的奇数情形，偶数 $n+1$ 只能是 $4,8,2q$。当 $n=6s+8$ 时，$n$ 是偶合数，$n+1$ 是至少为 $9$ 的 $3$ 的倍数，因此两个计数都大于 $c_n=1$。
:::

移位只是用来比较，并不是 Copeland 提出的猜想。知道最大公因数也还不能读出每一项的奇偶性；要做这件事，可以把整个多项式逐项模 $2$ 化简。

::: {.corollary #row-parity title="整行的奇偶性" mathesis="collected:copeland-a131758:2:s4" status="written-proof" proof="pf-row-parity" doi="10.5281/zenodo.24445683" source="Corollary 4" request="https://github.com/the-omega-institute/trureturing-requests/issues/466"}
模 $2$，当 $n\ge2$ 为偶数时 $P_n(t)=(1+t)^{n-1}$；当 $n\ge3$ 为奇数时 $P_n(t)=0$。
:::

::: {.proof #pf-row-parity}
偶数 $n\ge2$ 的取样级数在特征二中化为 $1+0t+t^2+0t^3+\cdots=1/(1-t)^2$；乘以 $(1-t)^{n+1}$，便得 $(1+t)^{n-1}$。若 $n\ge3$ 是奇数，所有样本都是偶数，故化简后级数为零。
:::

## 结论的来历与边界

Haobo Ma 与 Wenlin Zhang 的[论文第 2 版](https://doi.org/10.5281/zenodo.24445683)证明了覆盖所有行号的结论。其中素数步骤用到 [Carlitz 的多项式同余](https://doi.org/10.1007/BF01180274)（定理 3，式 (4.8)）；[Krylov 与 Li](https://math.colgate.edu/~integers/q57/q57.pdf) 后来给出了直接证明。Peter Bala 在 [A009940](https://oeis.org/A009940) 中的同余涉及常数列，其中 $a(n,0)=(-1)^n n!L_n(1)$；这里的奇偶性结论则控制整行。

[已冻结的 Lean 反例](https://github.com/the-omega-institute/trureturing/blob/742ce086eb9c8e6e36cde0fcdf712f63260c045c/D5/S0/Certificates/CopelandA131758PolynomialContentRefutation.lean)排除了两个断言同时成立：每行都存在整数实现，并且每个正行号的内容都等于 Copeland 的因数计数。它在这一联合假设下使用第 $8$ 行，并没有另外证明每行整性或适用于所有行的替代公式。[替代公式的形式化请求](https://github.com/the-omega-institute/trureturing-requests/issues/464)追踪的是后一个不同的结果。[下一章](transforms.md)讲解相关恒等式，不涉及原文中其他算子、Bessel 函数、zeta 函数或复插值公式。

英文讲稿沿用同一证明思路，并在讲者注释中解释余数计算。

::: {.slides src="seminar"}
:::
