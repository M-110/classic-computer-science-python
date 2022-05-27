from __future__ import annotations
from dataclasses import dataclass

@dataclass
class Edge:
    u: int # from
    v: int # to
    
    def reversed(self) -> Edge:
        return Edge(self.v, self.u)
    
    def __str__(self):
        return f'{self.u} -> {self.v}'
