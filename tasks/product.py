from typing import Any

__all__ = (
    'cartesian_product',
)


def cartesian_product(arr1: list[Any], arr2: list[Any]) -> list:
    arr3 = []
    if len(arr1)== 0 or len(arr2) == 0:
        return arr3
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            arr3.append((arr1[i], arr2[j]))
    return arr3
