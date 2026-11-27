# Exact contents in Copeland's polynomial-content conjecture via Carlitz's congruence

**Authors:** Haobo Ma, Wenlin Zhang

For Copeland's polynomial-content conjecture (OEIS A131758, revision 48, COMMENTS block signed September 9, 2008), we determine every row content using Carlitz's polynomial congruence (1953/54, Theorem 3, equation (4.8)). The content is 1 at indices 0, 1 and all even indices, and 2 at every odd index at least 3. This replaces the proposed divisor-count formula; every index 6s+8, s>=0, also excludes its one-place shift. The proof identifies content with a fixed divisor of an integer Laguerre polynomial. Direct proofs of associated transform identities and normalization corrections are included.

- PDF: [frozen public file](paper.pdf)
- DOI: [https://doi.org/10.5281/zenodo.24445683](https://doi.org/10.5281/zenodo.24445683)
- Concept DOI: [https://doi.org/10.5281/zenodo.24445682](https://doi.org/10.5281/zenodo.24445682)
- License: CC-BY-4.0
- Version: 2
- Mathesis record: [copeland-a131758](https://mathesis-omega-research.apps.chrono-ai.fun/papers/copeland-a131758?version=2)

## How to cite

Haobo Ma, Wenlin Zhang (2026). Exact contents in Copeland's polynomial-content conjecture via Carlitz's congruence. Mathesis, version 2. https://doi.org/10.5281/zenodo.24445683

## Statement progress

| Statement | Formalization status | Source | Verification basis |
|---|---|---|---|
| Proposition (s1) | preparing | [Lean source](https://github.com/the-omega-institute/trureturing/blob/742ce086eb9c8e6e36cde0fcdf712f63260c045c/D5/S0/Certificates/CopelandA131758PolynomialContentRefutation.lean) | No public receipt |
| Theorem (s2) | preparing | [Lean source](https://github.com/the-omega-institute/trureturing/blob/742ce086eb9c8e6e36cde0fcdf712f63260c045c/D5/S0/Certificates/CopelandA131758PolynomialContentRefutation.lean) | No public receipt |
| Corollary (s3) | preparing | [Lean source](https://github.com/the-omega-institute/trureturing/blob/742ce086eb9c8e6e36cde0fcdf712f63260c045c/D5/S0/Certificates/CopelandA131758PolynomialContentRefutation.lean) | No public receipt |
| Corollary (s4) | preparing | [Lean source](https://github.com/the-omega-institute/trureturing/blob/742ce086eb9c8e6e36cde0fcdf712f63260c045c/D5/S0/Certificates/CopelandA131758PolynomialContentRefutation.lean) | No public receipt |
| Corollary (s5) | preparing | [Lean source](https://github.com/the-omega-institute/trureturing/blob/742ce086eb9c8e6e36cde0fcdf712f63260c045c/D5/S0/Certificates/CopelandA131758PolynomialContentRefutation.lean) | No public receipt |
| Corollary (s6) | preparing | [Lean source](https://github.com/the-omega-institute/trureturing/blob/742ce086eb9c8e6e36cde0fcdf712f63260c045c/D5/S0/Certificates/CopelandA131758PolynomialContentRefutation.lean) | No public receipt |
| Corollary (s7) | preparing | [Lean source](https://github.com/the-omega-institute/trureturing/blob/742ce086eb9c8e6e36cde0fcdf712f63260c045c/D5/S0/Certificates/CopelandA131758PolynomialContentRefutation.lean) | No public receipt |

## Contributions

Original authors are listed above. Formalization contributors and attribution are retained in `formalization/nodes.json`; repository pull requests do not confer verification or credit. Submit formalization attempts through the Mathesis attempt path described in [CONTRIBUTING.md](CONTRIBUTING.md).

<!-- Mathesis generated repository guide; refresh with paper.py front. -->

## Reading and materials

[Paper site](https://papers.trureturing.org/copeland-a131758/) · [Frozen PDF](paper.pdf) · [Citation](CITATION.cff)

[中文阅读](https://papers.trureturing.org/copeland-a131758/copeland-a131758/zh/) · [Read in English](https://papers.trureturing.org/copeland-a131758/copeland-a131758/en/)

[Slides](https://papers.trureturing.org/copeland-a131758/copeland-a131758/slides/) ([sources](books/copeland-a131758/slides/)) · [Videos](https://papers.trureturing.org/copeland-a131758/copeland-a131758/films/) ([sources](books/copeland-a131758/films/))

These are publication routes; available built materials are inventoried in [mathesis-materials.json](https://papers.trureturing.org/copeland-a131758/mathesis-materials.json).

## Book and formalization

Catalog formalization status above is separate from the statement comparisons below. A nearby declaration does not verify the complete written result.

| Book result | Comparison with formal base | Compared declaration |
|---|---|---|
| `row-bridge` | variant | `D5/S0/Certificates/CopelandA131758PolynomialContentRefutation.result` |
| `exact-content` | variant | `D5/S0/Certificates/CopelandA131758PolynomialContentRefutation.result` |
| `agreement` | variant | `D5/S0/Certificates/CopelandA131758PolynomialContentRefutation.result` |
| `row-parity` | variant | `D5/S0/Certificates/CopelandA131758PolynomialContentRefutation.result` |
| `row-transforms` | none | — |
| `sibling-rows` | none | — |
| `signed-bell` | none | — |

Book stage: **complete**; 0 pending claims. [Statement comparisons](.mathesis/review.json).

## Repository map

| Zone | Location |
|---|---|
| Paper record | `paper.json`, `CITATION.cff`, `paper.pdf`, `manuscript/`, `formalization/nodes.json`, `LICENSES/`, `.mathesis/` |
| Content | `books/copeland-a131758/`: Chinese/English text, figures, visualizations, videos, slides, assets |
| Machinery | Upstream and layer managed paths; update with `tbook template update` |
| Repository front | This README, changelog, contribution guide, licence, project/site/pin configuration, `template.d/` |

See [the enforced layout](docs/layer-mathesis/LAYOUT.md). Preparation run records and built outputs stay outside the committed tree.
