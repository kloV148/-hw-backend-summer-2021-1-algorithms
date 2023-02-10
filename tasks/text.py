from typing import Optional

__all__ = (
    'find_shortest_longest_word',
)


def find_shortest_longest_word(text: str) -> tuple[Optional[str], Optional[str]]:
    symbols = [".", ","]
    for i in symbols:
        text = text.replace(i, "")
    worlds = text.split()
    if len(worlds)<2:
        return (None, None)
    else:
        longest = max(worlds, key = len)
        shortest = min(worlds, key = len)
        return (shortest, longest)

