from euklid import gcd, ext_gcd


def __congruence(eq1: tuple[int,...], eq2: tuple[int,...]) -> tuple[int,...]:
    a1, n1 = eq1
    a2, n2 = eq2
    g = gcd(n1, n2)


    if g == 1:
        '''
        in case of coprime
        '''
        p, q = ext_gcd(n1, n2)
        return ((a1 * q * n2 + a2 * p * n1) % (n1 * n2), n1 * n2)
    
    else:
        '''
        in case of non-coprime
        '''
        assert (a1 % g == a2), "Solution does not exist!!"
        p, q = ext_gcd(n1//g, n2//g)
        lcm = (n1 * n2) // g
        return (a1 * q * (n2//g) + a2 * p * (n1//g) % lcm, lcm)



def crt(rs: list[int,...], moduli: list[int,...]) -> tuple[int,...]:
    assert (len(rs) > 0 and len(rs) == len(moduli)), "Invalid system"

    # solution for 1 congruence
    if len(rs) == 1: return rs[0]

    solution = __congruence((rs[0], moduli[0]), (rs[1], moduli[1]))

    for r, m in zip(rs[2:], moduli[2:]):
        solution = __congruence(solution, (r, m))

    return solution


if __name__ == '__main__':
    while True:
        try:
            nums = int(input("number of congruences: "))
            rs = [int(r) for r in input('remainders: ').strip().split(' ')]
            moduli = [int(m) for m in input('moduli: ').strip().split(' ')]
            print(crt(rs, moduli))
        except AssertionError as e:
            print(e)
            continue