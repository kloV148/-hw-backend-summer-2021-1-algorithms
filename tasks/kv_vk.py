from typing import TypeVar

__all__ = (
    'flip_kv_vk',
    'flip_kv_vk_safe',
)


KT = TypeVar('KT')
KV = TypeVar('KV')


def flip_kv_vk(d: dict[KT, KV]) -> dict[KV, KT]:
    reversed_d = {}
    for i in d:
        reversed_d[d[i]] = i
    return reversed_d

def flip_kv_vk_safe(d: dict[KT, KV]) -> dict[KV, list[KT]]:
    reversed_d = {}
    for i in d:
        if d[i] in reversed_d.keys():
            reversed_d[d[i]] = reversed_d[d[i]] + [i]
        else:
            reversed_d[d[i]] = [i]
    return reversed_d
