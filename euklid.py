def gcd(a, b):
    assert (a, b) != (0, 0), "Could not find"
    while b != 0:
        a, b = b, a % b
    return a


def ext_gcd(a, b):
    r0, r1 = a, b
    t0, t1, s0, s1 = 0, 1, 1, 0
    while r1 != 0:
        q = r0 // r1
        r0, r1 = r1, r0 - q * r1
        s0, s1 = s1, s0 - q * s1
        t0, t1 = t1, t0 - q * t1
    assert s0 * a + t0 * b == gcd(a, b)
    return s0, t0
