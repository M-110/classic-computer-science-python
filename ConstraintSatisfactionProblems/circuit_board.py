"""Create a circuit board with a set of rectangles that are constrained
to fit within the board without overlapping."""

from csp import Constraint, CSP
from typing import Dict, List, NamedTuple
import matplotlib.pyplot as plt


class Rectangle(NamedTuple):
    width: int
    height: int
    value: int


class GridLocation(NamedTuple):
    row: int
    col: int


Domain = List[List[GridLocation]]
Grid = List[List[int]]


class CircuitBoardConstraint(Constraint[Rectangle, List[GridLocation]]):
    def __init__(self, rectangles: List[Rectangle]):
        super().__init__(rectangles)
        self.rectangles = rectangles

    def satisfied(self, assignment: Dict[Rectangle, List[GridLocation]]) -> bool:
        """Check to make sure there is no overlap"""
        all_locations = [loc for values in assignment.values() for loc in values]
        return len(set(all_locations)) == len(all_locations)


def generate_grid(rows: int, cols: int) -> Grid:
    """Generate grid with all values at 0"""
    return [[0 for _ in range(cols)] for _ in range(rows)]


def display_grid(grid: Grid):
    """Print grid."""
    for row in grid:
        print("".join(row))


def generate_domain(rectangle: Rectangle, grid: Grid) -> Domain:
    domain: Domain = []
    grid_height = len(grid)
    grid_width = len(grid[0])

    for row in range(grid_height):
        for col in range(grid_width):
            rows = range(row, row + rectangle.height + 1)
            cols = range(col, col + rectangle.width + 1)
            if (col + rectangle.width <= grid_width) and (row + rectangle.height <= grid_height):
                domain.append([GridLocation(r, c) for r in rows for c in cols])

    return domain


if __name__ == "__main__":
    grid: Grid = generate_grid(19, 19)
    rectangles = [Rectangle(1, 1, 1), Rectangle(4, 4, 2), Rectangle(2, 2, 3),
                  Rectangle(5, 2, 4), Rectangle(3, 3, 5), Rectangle(6, 10, 6),
                  Rectangle(1, 10, 7), Rectangle(12, 1, 8), Rectangle(5, 5, 9),
                  Rectangle(3, 7, 10), Rectangle(6, 6, 11), Rectangle(1, 3, 12),
                  Rectangle(4, 2, 13), Rectangle(6, 1, 14), Rectangle(3, 2, 15),
                  Rectangle(5, 1, 16)]
    locations: Dict[Rectangle, Domain] = {}
    for rectangle in rectangles:
        locations[rectangle] = generate_domain(rectangle, grid)
    csp = CSP(rectangles, locations)
    csp.add_constraints(CircuitBoardConstraint(rectangles))

    solution = csp.backtracking_search()

    if solution:
        grid = generate_grid(20, 20)
        for rect, locs in solution.items():
            for loc in locs:
                grid[loc.row][loc.col] = rect.value
        plt.pcolor(grid[::-1], linewidths=3)
        plt.show()
    else:
        print('No solution.')
