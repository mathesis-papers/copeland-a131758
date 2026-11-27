# 三个相关变换

生成级数把整个数列装入一个表达式：$x^n/n!$ 的系数存放第 $n$ 项。对级数做乘法或代换，再逐项读出结果，就能得到新数列，无须求任何无穷和的数值。这里的每一项还可以是关于 $t$ 的多项式。本章依据 Haobo Ma 与 Wenlin Zhang 的[论文第 2 版](https://doi.org/10.5281/zenodo.24445683)第 3 节。

## 用一个级数表示所有行

令 $R_n(t)=tP_n(t)/(n!(1-t)^{n+1})$、$G(x,t)=\sum_{n\ge0}P_n(t)x^n/n!$、$y=x(t-1)$。设 $s_j$ 为 [A000262](https://oeis.org/A000262)，由 $\sum_{j\ge0}s_ju^j/j!=\exp(u/(1-u))$ 定义。再用 $\sum_{v\ge1}v^nt^v=tE_n(t)/(1-t)^{n+1}$ 定义 Eulerian 多项式 $E_n$，包括 $E_0=1$。$E_n$ 记录的是普通幂 $v^n$ 的生成级数分子，正如 $P_n$ 记录 Laguerre 取样值的分子。

::: {.corollary #row-transforms title="生成级数、递推与 Euler 变换" mathesis="collected:copeland-a131758:2:s5" status="written-proof" proof="pf-row-transforms" doi="10.5281/zenodo.24445683" source="Corollary 5" request="https://github.com/the-omega-institute/trureturing-requests/issues/467"}
在 $\mathbb Q(t)$ 上，形式级数满足

$$
\sum_{n\ge0}R_n(t)z^n=\frac{t}{(1+z)(\exp(-z/(1+z))-t)},\qquad
G(x,t)=\frac{t-1}{(1-y)(t-\exp(y/(1-y)))}.
$$

对 $n\ge1$，修正 Riordan 递推为

$$
P_n(t)=n!(t-1)^n+\sum_{j=0}^{n-1}\binom nj s_{n-j}(t-1)^{n-j-1}P_j(t).
$$

对 $n\ge0$，与 Eulerian 多项式的变换关系为

$$
\frac{E_n(t)}{n!}=\sum_{j=0}^n\binom nj(1-t)^{n-j}\frac{P_j(t)}{j!}.
$$

逆变换交换 $E$ 与 $P$，并把幂换成 $(t-1)^{n-j}$。特别地，$P_n(-1)=n!\sum_{j=0}^n\binom nj(-2)^{n-j}E_j(-1)/j!$。作为多项式的恒等式也适用于可去的特殊取值。
:::

::: {.proof #pf-row-transforms}
对 Laguerre 多项式的有限展开式求和，得 $\sum_{n\ge0}L_n(v)(-z)^n=(1+z)^{-1}\exp(vz/(1+z))$。取样公式给出 $R_n(t)=\sum_{v\ge1}(-1)^nL_n(v)t^v$。对公比为 $t\exp(z/(1+z))$ 的等比级数求和，得到第一个公式；代入 $z=x(1-t)$，整理出 $G$ 即为第二个公式。消去其中分母的因子 $t-\exp(y/(1-y))$，比较 $x^n/n!$ 的系数可得递推。

直接展开 $L_n$，可把 $R_n(t)$ 表成 $\operatorname{Li}_{-j}(t)/j!$ 的交错二项变换，其中 $\operatorname{Li}_{-j}(t)=\sum_{v\ge1}v^jt^v$ 是在原点的展开。二项反演后，以 $tE_j(t)/(1-t)^{j+1}$ 替换这些幂和，即得正逆两个变换。在逆变换中取 $t=-1$，得到交错行和。
:::

## 相邻数表与错位的指数

[A131202](https://oeis.org/A131202) 的行 $A_n(t)$ 由指数生成级数 $(t-1)/(t-\exp(y/(1-y)))$ 给出，且 $A_0=1$。与 $G$ 比，只少了一个因子；这个差别足以发现刊出的重建公式有一处指数偏移。

::: {.corollary #sibling-rows title="由 A131202 重建系数行" mathesis="collected:copeland-a131758:2:s6" status="written-proof" proof="pf-sibling-rows" doi="10.5281/zenodo.24445683" source="Corollary 6" request="https://github.com/the-omega-institute/trureturing-requests/issues/468"}
对 $n\ge1$，$A_n(t)=P_n(t)-n(t-1)P_{n-1}(t)$；对 $n\ge0$，

$$
P_n(t)=\sum_{k=0}^n\binom nk A_{n-k}(t)k!(t-1)^k.
$$

重建因子的指数是 $k$，不是 $k-1$：原式在 $n=1$ 时给出 $2$ 而不是 $P_1(t)=t$。取 $t=2$，第一个等式对 $n\ge1$ 化为 [A084358](https://oeis.org/A084358) 中的 $A_n(2)=P_n(2)-nP_{n-1}(2)$。矩阵 $[\binom nk A_{n-k}(2)]_{0\le k\le n}$ 是 [A133289](https://oeis.org/A133289)，其逆为 $2I$ 减去 [A129652](https://oeis.org/A129652)。对所有 $n\ge0$，$A_n(1)=n!$；对 $n\ge1$，次数为 $n-1$，首项系数为 $s_n$。
:::

::: {.proof #pf-sibling-rows}
$A$ 的级数是 $(1-y)G$。乘以 $1-y$ 得差分式，乘以 $1/(1-y)=\sum_{k\ge0}x^k(t-1)^k$ 得逆式。取 $t=2$，级数变为 $1/(2-\exp(x/(1-x)))$。指数生成级数相乘对应二项卷积，因而倒数 $2-\exp(x/(1-x))$ 对应逆矩阵：其常数项为 $1$，$n>0$ 的指数系数为 $-s_n$。取 $t=1$，差分式化为 $P_n(1)=n!$。最后记 $S=\exp(y/(1-y))$，将 $x$ 换成 $x/t$ 后，$A$ 的级数是 $1+(S-1)/(t-S)$。当 $t$ 趋于无穷时，$S$ 逐项趋于 $\exp(x/(1-x))$；对每个 $n>0$，$A_n(t)/t^{n-1}$ 因而趋于 $s_n\ne0$。由多项式性质可读出次数和首项系数。
:::

## 有序分拆需要一半

$F_n$ 是把 $n$ 元集合分成一列**有顺序**的非空块的方法数，即 [A000670](https://oeis.org/A000670)，满足 $\sum F_nz^n/n!=1/(2-e^z)$。空集只有一个有序分拆。令 $b_n=(-1)^nF_n$。

::: {.corollary #signed-bell title="带符号的有序 Bell 数与互逆变换" mathesis="collected:copeland-a131758:2:s7" status="written-proof" proof="pf-signed-bell" doi="10.5281/zenodo.24445683" source="Corollary 7" request="https://github.com/the-omega-institute/trureturing-requests/issues/469"}
对 $n\ge0$，参数为零的 Laguerre 变换交换两个数列 $b_n$ 和 $P_n(2)$：

$$
(\mathcal T_0 u)_n=\sum_{j=0}^n(-1)^j\frac{n!}{j!}\binom nj u_j.
$$

用有理延拓定义多重对数的负整数阶取值时，$b_n=-\tfrac12\operatorname{Li}_{-n}(2)$，而不是 $-\operatorname{Li}_{-n}(2)$。此外 $P_n(2)/n!=(-1)^{n+1}R_n(2)/2$。
:::

::: {.proof #pf-signed-bell}
一般地，把二项系数 $\binom nj$ 换成 $\binom{n+\alpha}{n-j}$，数列 $u$ 的指数生成级数 $f(z)$ 就变为 $(1-z)^{-\alpha-1}f(-z/(1-z))$。代换两次回到原变量，两个因子也互相消去。取 $\alpha=0$，变换 $1/(2-e^{-z})$ 得到 $G(z,2)$，所以两个方向都成立。另一方面，把公比为 $te^z$ 的等比和有理延拓到 $t=2$，得 $\sum -\operatorname{Li}_{-n}(2)z^n/n!=2/(2-e^{-z})$。比较系数便得到一半因子，在 $n=0$ 时就能看出差别。最后一个等式由 $R_n$ 的定义代入 $t=2$ 得到。
:::

这里证明的是形式级数与多项式恒等式，只有指定取值用到有理延拓，并没有解决解析插值或相邻数列的其他猜想。如想贡献 Lean 证明，请先在对应请求中协调范围，然后从贡献者自己的分支向 [trureturing 的上游开发分支](https://github.com/the-omega-institute/trureturing/blob/dev/docs/CONTRIBUTING.md) 提交聚焦于该结果的 PR。
