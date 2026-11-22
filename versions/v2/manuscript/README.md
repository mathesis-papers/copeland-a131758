# Exact contents in Copeland's polynomial-content conjecture via Carlitz's congruence

Haobo Ma (ChronoAI Pte Ltd, Singapore), then Wenlin Zhang (National University
of Singapore; ChronoAI Pte Ltd, Singapore). November 19, 2026. Revision 2.

## Result

For the ordinary Laguerre array defined in OEIS A131758, the complete
coefficient-row content is 1 at indices 0 and 1 and every even index, and
2 at every odd index at least 3. The proof identifies content with the gcd
of the integer values of a monic Laguerre polynomial, excludes all odd
prime factors, and determines its exact power of 2.

This corrects the conjectured divisor-count formula. Both that formula
and the one-place shifted formula fail at every index `6s+8`, `s>=0`.
The latter is not asserted in the posing source. The note also gives the
exact indices where either equation holds.

## Contents and rebuilding

- `note.tex`: self-contained LaTeX, including the bibliography.
- `note.pdf`: the rendered note, supplied alongside the source archive.
- `metadata.json`: scientific title, abstract, creators, license and source link.
- `verify.py`: Python 3 standard-library exact-arithmetic checks.
- `verification.json`: the expected checker output.
- `MANIFEST.sha256`: scientific source-file hashes.

Build with Tectonic 0.17.0:

```sh
tectonic note.tex
```

Alternatively run `pdflatex -interaction=nonstopmode -halt-on-error note.tex`
twice. The embedded bibliography requires no BibTeX step. Run:

```sh
python3 verify.py > verification.actual.json
python3 -c 'import json; assert json.load(open("verification.actual.json")) == json.load(open("verification.json"))'
```

The checker requires neither third-party Python packages nor network access.
It compares a finite Laguerre expansion with the integer recurrence
`B_(n+1)(x)=(x-2n-1)B_n(x)-n^2 B_(n-1)(x)`, with `B_0=1`, `B_1=x-1`.

## Mathematical coverage

The universal arguments in the note prove the exact content formula,
integrality, degree and row sum, the equality classifications, and the
simultaneous failure progression. They prove the prime-polynomial
congruence, the whole-row parity law, the modified Riordan recurrence,
the Eulerian binomial transforms, the A131202 reconstruction and its
leading coefficient and row sum, the A084358 finite-difference formula,
the A133289 inverse matrix, and reciprocal generalized Laguerre transforms.
The A131202 reconstruction exponent and signed ordered-Bell normalization
are corrected explicitly. The source formulas receive their original
attributions. Carlitz's Theorem 3, equation (4.8), p. 479 (1953/54), is the
polynomial congruence antecedent; Krylov and Li supplied a later direct proof
(2014 preprint; 2016 journal, Corollary 2, equation (10)). Bala's 2017
corollary, p. 5, specializes to the constant-column congruence recorded by
him in A009940 in 2023. The note gives a self-contained proof of the needed
prime-modulus specialization of Carlitz's result.

The finite checks cover complete rows 0 through 32, exact gcds, fixed-divisor
representatives, the modulo-4 witness, and prime congruences for degrees
0 through 80 at every residue for primes 2, 3, 5, 7, 11, 13, 17 and 19.
Sibling identities are checked at degrees 0 through 32 and arguments
-2, -1, 0, 1, 2, 3. Necessary divisor counts and the progression through
index 1000 are checked separately. All arithmetic uses integers and rational
numbers without rounding. These finite ranges do not substitute for the
universal written proofs.

The declaration `result` in
`D5.S0.Certificates.CopelandA131758PolynomialContentRefutation` in the
[pinned Lean file](https://github.com/the-omega-institute/trureturing/blob/742ce086eb9c8e6e36cde0fcdf712f63260c045c/D5/S0/Certificates/CopelandA131758PolynomialContentRefutation.lean)
has proposition `not claim`: it negates the joint assertion of global
integer-row existence and the positive-index content equation with
A038548(n). Its argument uses the first two coefficients at index 8 and
D(8)=2. The exact content formula and all other extensions listed above
have written proofs in the note; they are not conclusions of that declaration.

The source assertion is in [A131758](https://oeis.org/A131758), revision 48,
COMMENTS block signed Tom Copeland, September 9, 2008. The two coefficients
6209 and -41417 are already present in
[Greubel's table](https://oeis.org/A131758/b131758.txt), flattened indices
36 and 37. Their combination `-6417*6209-962*(-41417)=1` gives a short
individual example of the general content theorem.

## License

The note and original accompanying material are licensed under Creative
Commons Attribution 4.0 International, CC BY 4.0 (`cc-by-4.0`). The cited
OEIS entries, papers and DLMF retain their respective terms.
