
from typing import TypeVar, Generic, List

T = TypeVar('T')

class Stack(Generic[T]):
    """A LIFO stack implimentation"""
    
    def __init__(self):
        self._container: List[T] = []
        
    @property
    def empty(self) -> bool:
        return not self._container
    
    def push(self, item: T):
        self._container.append(item)
    
    def pop(self) -> T:
        return self._container.pop()
    
    def __repr__(self):
        return repr(self._container)
