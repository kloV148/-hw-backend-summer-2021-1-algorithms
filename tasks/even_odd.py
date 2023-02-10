__all__ = (
    'even_odd',
)


def even_odd(arr: list[int]) -> float:
    odd_summ = 0
    even_summ = 0
    for i in arr:
        if i%2 == 1:
            odd_summ += i
        else:
            even_summ+=i
    if odd_summ!=0: return even_summ/odd_summ
    else:
        return 0
