__all__ = (
    'is_prime',
)


def is_prime(number: int) -> bool:
    if number in [0,1]:
        return False
    for i in range(2, int(number**0.5)+1):
        if number%i == 0:
            return False
    return True
