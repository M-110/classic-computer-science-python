from __future__ import annotations
from typing import TypeVar, Tuple, Type
from abc import ABC, abstractmethod

# T must be a subclass of chromosome.
T = TypeVar('T', bound='Chromosome')


class Chromosome(ABC):
    """Abstract base class for all chromosomes."""
    @abstractmethod
    def fitness(self) -> float:
        ...
    
    @classmethod
    @abstractmethod
    def random_instance(cls: Type[T]) -> T:
        ...
    
    @abstractmethod
    def crossover(self: T, other: T) -> Tuple[T, T]:
        ...
    
    @abstractmethod
    def mutate(self) -> None:
        ...
