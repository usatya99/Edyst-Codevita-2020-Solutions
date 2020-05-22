def solve(n, k, p):
    binsum = 0

    if n < 1e6:
        # pre-compute factorials and inverses
        facts, invfacts = fermat_compute(n, p)
        for i in range(0, k + 1, 2):
            binsum += binom_pre_computed(facts, invfacts, n, i, p)
            binsum %= p
    else:
        for i in range(0, k + 1, 2):
            binsum += fermat_binom(n, i, p)
            binsum %= p

    return binsum % p


# Using Fermat's little theorem to compute nCk mod p
# Note: p must be prime and k < p
# calculate numerator
# calculate denominator
# numerator * denominator^(p-2) (mod p)
def fermat_binom(n, k, p):
    if k > n:
        return 0

    num = 1
    for i in range(n, n - k, -1):
        num = (num * i) % p

    denom = 1
    for i in range(1, k + 1):
        denom = (denom * i) % p

    return (num * pow(denom, p - 2, p)) % p


# Using Fermat's little theorem to pre-compute factorials and inverses
# Note: only works when p is prime and k < p
def fermat_compute(n, p):
    facts = [0] * (n + 1)
    invfacts = [0] * (n + 1)

    facts[0] = 1
    invfacts[0] = 1
    for i in range(1, n + 1):
        # calculate factorial and corresponding inverse
        facts[i] = (facts[i - 1] * i) % p
        invfacts[i] = pow(facts[i], p - 2, p)

    return facts, invfacts


# Compute binomial coefficient from given pre-computed factorials and inverses
def binom_pre_computed(facts, invfacts, n, k, p):
    # n! / (k!^(p-2) * (n-k)!^(p-2)) (mod p)
    return (facts[n] * ((invfacts[k] * invfacts[n - k] % p))) % p


if __name__ == "__main__":
    n, k = input().strip().split()
    n = int(n)
    k = int(k)
    p = int(1e9 + 7)

    print(solve(n, k, p))
