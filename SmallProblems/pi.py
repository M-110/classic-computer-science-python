import math


def calculate_pi(number_of_terms: int) -> float:
    """Approximate pi using the Leibniz formula"""
    denominator: int = 1
    operation: int = 1
    pi: float = 0
    
    for _ in range(number_of_terms):
        pi += 4 / denominator * operation
        denominator += 2
        operation *= -1
    return pi


if __name__ == "__main__":
    my_pi = calculate_pi(1_000_000)
    
    print(f'pi approximation using 1,000,0000 Leibniz terms: {my_pi}')
    print(f'pi from math module: {math.pi}\n')
    
    print(f'accurate to about {math.pi - my_pi:f}')

