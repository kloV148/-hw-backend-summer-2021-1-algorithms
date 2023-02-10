from typing import Any

__all__ = (
    'Node',
    'Graph'
)


class Node:
    def __init__(self, value: Any):
        self.value = value

        self.outbound = []
        self.inbound = []

    def point_to(self, other: 'Node'):
        self.outbound.append(other)
        other.inbound.append(self)

    def __str__(self):
        return f'Node({repr(self.value)})'

    __repr__ = __str__


class Graph:
    def __init__(self, root: Node):
        self._root = root

    def dfs(self) -> list[Node]:
        visited = [self._root]
        stack = self._root.outbound[::-1]
        while len(stack)>0:
            if stack[-1] not in visited: visited.append(stack[-1])
            current = stack.pop(-1)
            for i in current.outbound[::-1]:
                if i not in visited:
                    stack.append(i)
        return visited

    def bfs(self) -> list[Node]:
        queu = [self._root]
        visited = [self._root]
        while len(queu)!= 0:
            current = queu.pop(0)
            for i in current.outbound:
                if i not in visited:
                    queu.append(i)
                    visited.append(i)
        return visited


