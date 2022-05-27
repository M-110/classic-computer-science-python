from csp import Constraint, CSP
from typing import Dict, List, Optional, Tuple,  NamedTuple
from random import choice
from string import ascii_uppercase


class GridLocation(NamedTuple):
    row: int
    col: int
    
    
Grid = List[List[str]] # Type
Domain = List[List[GridLocation]] # Type

def generate_grid(rows: int, cols: int) -> Grid:
    """Generate random grid of letters"""
    return [[choice(ascii_uppercase) for _ in range(cols)] for _ in range(rows)]


def display_grid(grid: Grid):
    """Print grid."""
    for row in grid:
        print("".join(row))
        
        
def generate_domain(word: str, grid: Grid) -> Domain:
    domain: Domain = []
    height = len(grid)
    width = len(grid[0])
    length = len(word)
    
    for row in range(height):
        for col in range(width):
            cols = range(col, col + length + 1)
            rows = range(row, row + length + 1)
        
            if col + length <= width:
                domain.append([GridLocation(row, c) for c in cols])

                if row + length <= height:
                    domain.append([GridLocation(r, col + (r - row)) for r in rows])
            
            if row + length <= height:
                domain.append([GridLocation(r, col) for r in rows])
                if col - length >= 0:
                    domain.append([GridLocation(r, col - (r - row)) for r in rows])
    return domain

class WordSearchConstraint(Constraint[str, List[GridLocation]]):
    def __init__(self, words: List[str]):
        super().__init__(words)
        self.words = words

    def satisfied(self, assignment: Dict[str, List[GridLocation]]) -> bool:
        all_locations = [loc for values in assignment.values() for loc in values]
        return len(set(all_locations)) == len(all_locations)


if __name__ == "__main__":
    grid: Grid = generate_grid(10, 10)
    words: List[str] = ["MATTHEW", "JOE", "MARY", "SARAH", "SALLY"]
    locations: Dict[str, Domain] = {}
    for word in words:
        locations[word] = generate_domain(word, grid)
    
    csp = CSP(words, locations)
    csp.add_constraints(WordSearchConstraint(words))
    
    solution = csp.backtracking_search()
    
    if solution:
        print(solution)
    else:
        print('No solution.')