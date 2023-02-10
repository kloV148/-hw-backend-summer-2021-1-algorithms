from typing import Any

__all__ = (
    'corresponding_pairs',
)


def corresponding_pairs(arr1: list[Any], arr2: list[Any]) -> list[tuple[Any, Any]]:
    arr_3 = []
    for i in range (min(len(arr1), len(arr2))):
        arr_3.append((arr1[i], arr2[i]))
    return arr_3
