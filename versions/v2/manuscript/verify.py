#!/usr/bin/env python3
"""Exact finite checks for Copeland's polynomial-content conjecture."""

import json
from fractions import Fraction
from functools import reduce
from math import comb, factorial, gcd, isqrt


EXPECTED_ROW = [
    6209, -41417, 48645, 376259, -1724861,
    3233925, -2977609, 1078849, 40320,
]
EXPECTED_PREFIX = [
    [1], [0, 1], [-1, 1, 2], [4, -14, 10, 6],
    [-15, 83, -157, 89, 24], [56, -424, 1266, -1724, 826, 120],
    [-185, 1887, -8038, 17642, -19593, 8287, 720],
    [204, -4976, 36226, -126944, 239576, -234688, 90602, 5040],
]


def require(condition, label):
    if not condition:
        raise ValueError(label)


def rational_row(degree):
    values = [
        sum(
            (Fraction((-1) ** power * comb(degree, power) * argument ** power,
                      factorial(power)) for power in range(degree + 1)),
            Fraction(0),
        )
        for argument in range(1, degree + 2)
    ]
    coefficients = []
    for column in range(degree + 1):
        value = (-1) ** degree * factorial(degree) * sum(
            ((-1) ** shift * comb(degree + 1, shift) * values[column - shift]
             for shift in range(column + 1)), Fraction(0),
        )
        require(value.denominator == 1, f"integrality: {degree}, {column}")
        coefficients.append(value.numerator)
    return coefficients


def recurrence_value(degree, argument):
    previous, current = 1, argument - 1
    if degree == 0:
        return previous
    for index in range(1, degree):
        previous, current = current, (argument - 2 * index - 1) * current - index ** 2 * previous
    return current


def recurrence_row(degree):
    values = [recurrence_value(degree, argument) for argument in range(1, degree + 2)]
    return [
        sum((-1) ** shift * comb(degree + 1, shift) * values[column - shift]
            for shift in range(column + 1))
        for column in range(degree + 1)
    ]


def small_divisors(number):
    return [divisor for divisor in range(1, isqrt(number) + 1) if number % divisor == 0]


def main():
    rows = []
    for degree in range(33):
        row = rational_row(degree)
        require(row == recurrence_row(degree), f"two representations: {degree}")
        require(row[-1] == factorial(degree), f"leading coefficient: {degree}")
        require(sum(row) == factorial(degree), f"row sum: {degree}")
        if degree < len(EXPECTED_PREFIX):
            require(row == EXPECTED_PREFIX[degree], f"source prefix: {degree}")
        if degree >= 2 and degree % 2 == 0:
            require([value % 2 for value in row] ==
                    [comb(degree - 1, column) % 2 for column in range(degree)] + [0],
                    f"even-index polynomial congruence: {degree}")
        if degree >= 3 and degree % 2 == 1:
            require(all(value % 2 == 0 for value in row), f"odd-index parity: {degree}")
        rows.append(row)
    contents = [reduce(gcd, row, 0) for row in rows]
    require(contents == [2 if degree >= 3 and degree % 2 else 1 for degree in range(33)],
            'complete content formula')
    fixed_divisors = []
    for degree in range(33):
        values = [recurrence_value(degree, argument) for argument in range(1, degree + 2)]
        fixed_divisors.append(reduce(gcd, values, 0))
        require(fixed_divisors[-1] == contents[degree], f'fixed divisor: {degree}')
        if degree >= 3 and degree % 2:
            require(recurrence_value(degree, 3) % 4 == 2, f'modulo four: {degree}')
    primes = [2, 3, 5, 7, 11, 13, 17, 19]
    for prime in primes:
        for degree in range(81):
            quotient, remainder = divmod(degree, prime)
            for argument in range(prime):
                require(recurrence_value(degree, argument) % prime ==
                        pow(argument, quotient * prime, prime) * recurrence_value(remainder, argument) % prime,
                        f'prime polynomial congruence: {prime}, {degree}, {argument}')
    equality_cases = []
    for degree in range(1, 1001):
        content_value = 2 if degree >= 3 and degree % 2 else 1
        if degree % 6 == 2 and degree >= 8:
            require(content_value != len(small_divisors(degree)) and
                    content_value != len(small_divisors(degree + 1)), 'arithmetic progression')
        if content_value == len(small_divisors(degree)):
            equality_cases.append(degree)
    sets_of_lists = [1]
    lists_of_sets = [1]
    for degree in range(1, 33):
        sets_of_lists.append(sum(comb(degree - 1, block - 1) * factorial(block) *
                                  sets_of_lists[degree - block] for block in range(1, degree + 1)))
        lists_of_sets.append(sum(comb(degree, block) * sets_of_lists[block] *
                                 lists_of_sets[degree - block] for block in range(1, degree + 1)))
    eulerian_rows = [[1]]
    for degree in range(1, 33):
        previous = eulerian_rows[-1]
        eulerian_rows.append([
            (column + 1) * (previous[column] if column < len(previous) else 0) +
            (degree - column) * (previous[column - 1] if column else 0)
            for column in range(degree)
        ])
    ordered_bell = [1]
    for degree in range(1, 33):
        ordered_bell.append(sum(comb(degree, count) * ordered_bell[degree - count]
                                for count in range(1, degree + 1)))
    for argument in [-2, -1, 0, 1, 2, 3]:
        values = [sum(value * argument ** column for column, value in enumerate(row)) for row in rows]
        related_direct = [1]
        for degree in range(1, 33):
            related_direct.append(sum(comb(degree, count) * sets_of_lists[count] *
                                      (argument - 1) ** (count - 1) * related_direct[degree - count]
                                      for count in range(1, degree + 1)))
        for degree in range(1, 33):
            expected = factorial(degree) * (argument - 1) ** degree + sum(
                comb(degree, lower) * sets_of_lists[degree - lower] *
                (argument - 1) ** (degree - lower - 1) * values[lower]
                for lower in range(degree))
            require(values[degree] == expected, f'MRA recurrence: {degree}, {argument}')
            transformed = sum(Fraction(comb(degree, lower) * (1 - argument) ** (degree - lower) *
                                       values[lower], factorial(lower)) for lower in range(degree + 1))
            target = sum(value * argument ** column for column, value in enumerate(eulerian_rows[degree]))
            require(transformed == Fraction(target, factorial(degree)), f'Eulerian transform: {degree}, {argument}')
            if argument == 2:
                require(values[degree] - degree * values[degree - 1] == lists_of_sets[degree],
                        f'lists-of-sets difference: {degree}')
        for degree in range(33):
            related = [values[index] - (index * (argument - 1) * values[index - 1] if index else 0)
                       for index in range(degree + 1)]
            require(related[degree] == related_direct[degree], f'A131202 generating function: {degree}, {argument}')
            require(values[degree] == sum(comb(degree, count) * related[degree - count] *
                                         factorial(count) * (argument - 1) ** count
                                         for count in range(degree + 1)),
                    f'reconstruction: {degree}, {argument}')
            if argument == 2:
                transform = sum((-1) ** lower * Fraction(factorial(degree), factorial(lower)) *
                                comb(degree, lower) * (-1) ** lower * ordered_bell[lower]
                                for lower in range(degree + 1))
                require(transform == values[degree], f'Fubini transform: {degree}')
    for degree in range(1, 33):
        related_coefficients = [rows[degree][column] + degree *
                                (rows[degree - 1][column] if column < degree else 0) -
                                degree * (rows[degree - 1][column - 1] if column else 0)
                                for column in range(degree + 1)]
        require(related_coefficients[-1] == 0 and related_coefficients[-2] == sets_of_lists[degree],
                f'A131202 leading coefficient: {degree}')
        require(sum(related_coefficients) == factorial(degree), f'A131202 row sum: {degree}')
        require(sum(comb(degree, count) * lists_of_sets[count] *
                    (1 if degree == count else -sets_of_lists[degree - count])
                    for count in range(degree + 1)) == 0, f'inverse matrix: {degree}')
    row = rows[8]
    require(row == EXPECTED_ROW, "ninth row")
    content = reduce(gcd, row, 0)
    require(content == 1 and -6417 * row[0] - 962 * row[1] == 1, "Bezout identity")
    require(small_divisors(8) == [1, 2] and small_divisors(9) == [1, 3], "divisor counts")
    family = []
    for parameter in range(3):
        exponent = 12 * parameter + 7
        number = 2 ** exponent
        predicted = sum((2 ** power) ** 2 <= number for power in range(exponent + 1))
        shifted = len(small_divisors(number + 1))
        quotient, remainder = divmod(number + 1, 3)
        require(predicted == 6 * parameter + 4 and predicted % 2 == 0, "family count")
        require(remainder == 0 and quotient % 3 != 0 and quotient % 8 == 3, "family residues")
        require(shifted % 2 == 0, "shifted family count")
        family.append({"s": parameter, "n": number, "D_n": predicted, "D_n_plus_1": shifted})
    for parameter in range(101):
        exponent = 12 * parameter + 7
        require(pow(2, exponent, 9) == 2 and exponent >= 7, "modular family")
    result = {
        "status": "passed",
        "arithmetic": "unbounded integers and exact rational numbers; no rounding",
        "rows_compared": {"first": 0, "last": 32, "count": 33},
        "representations": ["finite Laguerre expansion", "integer three-term recurrence"],
        "source_comments_rows": {"first": 0, "last": 7},
        "properties": ["integrality", "row sum", "leading coefficient", "polynomial parity"],
        "ninth_row": row,
        "content": content,
        "bezout": {"multipliers": [-6417, -962], "value": 1},
        "D_8": 2,
        "D_9": 2,
        "family_divisor_counts": family,
        "family_modular_parameters": {"first": 0, "last": 100},
        "scope": "finite checks; universal statements are proved in note.tex",
        "contents": contents,
        "fixed_divisor_values": fixed_divisors,
        "prime_congruences": {"primes": primes, "degree_first": 0, "degree_last": 80,
                              "arguments": "every residue modulo each listed prime"},
        "literal_equality_indices_through_1000": equality_cases,
        "sibling_identity_checks": {"degrees": [0, 32], "arguments": [-2, -1, 0, 1, 2, 3],
                                    "identities": ["modified Riordan recurrence", "Eulerian binomial transform",
                                                   "A131202 reconstruction and generating function",
                                                   "A131202 leading coefficient and row sum", "A084358 finite difference",
                                                   "A133289 inverse", "signed Fubini Laguerre transform"]},
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
