# Chinese Remainder Theorem
An implementation of the [Chinese Remainder Theorem](https://en.wikipedia.org/wiki/Chinese_remainder_theorem), which states that if one knows the remainders of the [Euclidean division](https://en.wikipedia.org/wiki/Euclidean_division) of an integer $x$ by several integers, then one can determine uniquely the remainder of the division of $x$ by the product of these integers, under the condition that the divisors are [pairwise coprime](https://en.wikipedia.org/wiki/Pairwise_coprime).


## Satement
Let $\set{n_1, n_2, ..., n_k}$ be integers greater than 1 (called as _moduli_ or _divisors_), also denote by $N$ the production of $n_i$.   
If the $n_i$ are pairwise coprime, and if $\set{a_1, a_2, ..., a_k}$ are integers such that $0 \leq a_i \lt n_i$, then the system

$$
x \equiv a_1 \mod{n_1} \newline
x \equiv a_2 \mod{n_2} \newline
\vdots \newline
x \equiv a_k \mod{n_k}
$$

has a unique solution, and any two solutions, say $x_1$ and $x_2$, are congruent modulo $N$, that is $x_1 \equiv x_2 \mod{N}$.


## Examples
Congruence equations:   
```
x = 1 mod 3
x = 4 mod 5
x = 6 mod 7
```

Solving by our script:
```
number of congruences: 3
remainders: 1 4 6
moduli: 3 5 7
(34, 105)
```

>Note: the remainders and moduli are separated by single space, the result is returned as (x, N)
