def prime_factors(n: int) -> list[int]:
    """Returns the prime factors of a number.

    Parameters
    ----------
    n : int
        The number to factorize.

    Returns
    -------
    list[int]
        The prime factors of the number.
    """
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)

    return factors


def time_signature_factors(
    nominator: int, denominator: int, metric_level: int = 16
) -> list[int]:
    """Returns the prime factors of a time signature.

    Parameters
    ----------
    nominator : int
        The nominator of the time signature.
    denominator : int
        The denominator of the time signature.

    Returns
    -------
    list[int]
        The prime factors of the time signature.
    """
    subdivisions = metric_level // denominator

    return prime_factors(nominator) + prime_factors(subdivisions)

def product_top(z: int, factors: list[int]):
    mult = 1

    for j in range(1, z + 1):
        mult *= factors[j]

    return mult


def product_bottom(z: int, r: int, factors: list[int]):
    mult = 1

    for k in range(r + 1):
        mult *= factors[z + 1 - k]

    return mult

def indispensability(pulse: int, primes: list[int]) -> int:
    """Returns the indispensability of a pulse.

    Parameters
    ----------
    pulse : int
        The pulse to calculate the indispensability of.
    primes : list[int]
        The prime factors of the time signature.

    Returns
    -------
    int
        The indispensability of the pulse.
    """
    primes = [1] + primes + [1]

    z = len(primes) - 2
    top = product_top(z, primes)
    sum = 0
    for r in range(z):
        bot = product_bottom(z, r, primes)

        mult = 1
        for i in range(z - r):
            mult *= primes[i]

        modulo = primes[z - r]
        temp = ((pulse - 2) % top) / bot
        temp = int(1 + temp)
        temp = temp % modulo
        temp = 1 + temp

        basic = basic_indispensability(temp, primes[z - r])

        sum += mult * basic

    return sum


def w_func(x: int) -> int:
    """Returns the w function of a number.

    Parameters
    ----------
    x : int
        The number to calculate the w function of.

    Returns
    -------
    int
        The w function of the number.
        If the number is 0, 0 is returned.
        else 1 is returned.
    """

    if x == 0:
        return 0

    return 1


def basic_indispensability(pulse: int, prime: int) -> int:
    """Returns the basic indispensability of a pulse.

    Parameters
    ----------
    pulse : int
        The pulse to calculate the basic indispensability of.
    prime : int
        The prime to calculate the basic indispensability of.

    Returns
    -------
    int
        The basic indispensability of the pulse.
    """
    if prime <= 3:
        return (prime + pulse - 2) % prime

    new_pulse = pulse - 1 + w_func(prime - pulse)
    factors = prime_factors(prime - 1)[::-1]
    q = indispensability(new_pulse, factors)

    return (q + w_func(int(q / (prime // 4)))) * w_func(prime - pulse - 1) + (
        prime // 4
    ) * (1 - w_func(prime - pulse - 1))
