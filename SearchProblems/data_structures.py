from collections import deque
from heapq import heappop, heappush
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


class Queue(Generic[T]):
    """A FIFO queue implimentation"""
    
    def __init__(self):
        self._container: deque[T] = deque()
        
    @property
    def empty(self) -> bool:
        return not self._container
    
    def push(self, item: T):
        self._container.append(item)
    
    def pop(self) -> T:
        return self._container.popleft()
    
    def __repr__(self):
        return repr(self._container)
    
class PriorityQueue(Generic[T]):
    def __init__(self):
        self._container: List[T] = []
        
    @property
    def empty(self) -> bool:
        return not self._container
    
    def push(self, item: T):
        heappush(self._container, item)
        
    def pop(self) -> T:
        return heappop(self._container)
    
    def __repr__(self):
        return repr(self._container)
    
    
