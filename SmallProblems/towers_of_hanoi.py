"""A game of Towers of Hanoi along with a solver class that solves it."""

from typing import TypeVar, Generic, List
from string import ascii_uppercase
import math

T = TypeVar('T')


class Tower(Generic[T]):
    """Tower containing a stack of items of generic type."""

    def __init__(self, id_value: int):
        self.stack: List[T] = []
        self.id = id_value

    def __repr__(self):
        return repr(self.stack)
    
    def is_empty(self) -> bool:
        return len(self.stack) == 0

    def pop(self) -> T:
        """Remove and return the top item from the tower."""
        return self.stack.pop()

    def push(self, item: T):
        """Push the item  to the top of the tower."""
        self.stack.append(item)
        
    def peek(self) -> T:
        """Peeks at the item on the top of the tower.
        
        If tower is empty, return infinity for comparison purposes.
        """
        try:
            return self.stack[-1]
        except IndexError:
            return math.inf


class TowersOfHanoi:
    """Game consisting of user-defined number of towers"""

    def __init__(self, number_of_towers: int = 3, number_of_discs: int = 3):
        self.towers: List[Tower[int]] = []
        self.number_of_discs: int = number_of_discs
        self.moves: int = 0
        self.move_log: List[str] = []
        
        for i in range(number_of_towers):
            self.towers.append(Tower(i))

        for i in range(number_of_discs, 0, -1):
            self.towers[0].push(i)

    def __repr__(self):
        repr_output: List[str] = []
        for tower, letter in zip(self.towers, ascii_uppercase):
            repr_output.append(f'Tower {letter}: {tower}')
        return '\n'.join(repr_output)
    
    def copy(self):
        """Create a copy of the current game."""
        return TowersOfHanoi(len(self.towers), self.number_of_discs)
    
    def move_disc(self, from_tower: int, to_tower: int):
        """Move disc from one tower to another."""
        if self.towers[from_tower].peek() > self.towers[to_tower].peek():
            raise ValueError('Disc cannot be placed on disc of smaller value.')
        
        disc: int = self.towers[from_tower].pop()
        self.towers[to_tower].push(disc)
        self.moves += 1
        self.move_log.append(f'{ascii_uppercase[from_tower]} to {ascii_uppercase[to_tower]}')
        
        self.victory_check()
    
    def victory_check(self):
        """Check whether all discs are on the final tower."""
        if all(tower.is_empty() for tower in self.towers[:-1]):
            print(f'Solved {self.number_of_discs} disc game in {self.moves} moves')
            self.print_move_log()
            
    def print_move_log(self):
        """Print log of each move made by this game."""
        for i, move in enumerate(self.move_log, start=1):
            print(f'{i}: {move}')
              
        
class Solver:
    """Solver which takes a game and solves it"""
    def __init__(self, game: TowersOfHanoi):
        self.game = game
        self.copy_game: TowersOfHanoi = game.copy()
        
    def solve(self):
        """Solve the current game."""
        self.hanoi(self.copy_game.towers[0], self.copy_game.towers[2], self.copy_game.towers[1],
                   self.copy_game.number_of_discs)
    
    def hanoi(self, begin: Tower[int], end: Tower[int], temp: Tower[int], n: int):
        """A recursive method for solving the game."""
        if n == 1:
            self.game.move_disc(begin.id, end.id)
            end.push(begin.pop())
        else:
            self.hanoi(begin, temp, end, n - 1)
            self.hanoi(begin, end, temp, 1)
            self.hanoi(temp, end, begin, n - 1)
        

if __name__ == "__main__":
    game = TowersOfHanoi(number_of_discs=5)
    solver = Solver(game)
    solver.solve()
