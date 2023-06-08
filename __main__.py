from metric_indispensability import time_signature_factors, indispensability

def pulse_weights(
    nominator: int, denominator: int, metric_level: int = 16
) -> list[float]:
    primes = time_signature_factors(nominator, denominator, metric_level)
    pulses = metric_level // denominator * nominator

    indispensabilities = [
        indispensability(pulse, primes)
        for pulse in range(1, pulses + 1)
    ]
    return indispensabilities

if __name__ == "__main__":
    print(pulse_weights(3, 4, 16))
