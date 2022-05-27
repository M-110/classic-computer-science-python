from __future__ import annotations
from enum import Enum
from typing import List, NamedTuple, Callable, Optional, Generic, TypeVar, Set, Union, Dict
import random
from math import sqrt
from SearchProblems.data_structures import Stack, Queue, PriorityQueue
#from generic_search import dfs, bfs, node_to_path, astar, Node


T = TypeVar('T')


class Cell(str, Enum):
    EMPTY = " "
    BLOCKED = "X"
    START = "S"
    GOAL = "G"
    PATH = "*"

        
def distance(goal: MazeCoordinates) -> Callable[[MazeCoordinates], float]:
    """Returns a function that returns the manhattan distance from the goal."""
    def distance(mc: MazeCoordinates) -> float:
        x: int = abs(mc.column - goal.column)
        y: int = abs(mc.row - goal.row)
        return x + y
    return distance
        

class MazeCoordinates(NamedTuple):
    row: int
    column: int
    

class Node(Generic[T]):
    def __init__(self, state: T, parent: Optional[Node], cost: float = 0.0,
                 heuristic: float = 0.0):
        self.state = state
        self.parent = parent
        self.cost = cost
        self.heuristic = heuristic
        
    def __repr__(self):
        return f'{self.state}'
        
    def __lt__(self, other: Node) -> bool:
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)


class Maze:
    def __init__(self, rows: int = 10, columns: int = 10,
                 sparseness: float = 0.2,
                 start: MazeCoordinates = MazeCoordinates(0, 0),
                 goal: MazeCoordinates = MazeCoordinates(9, 9)):
        self._rows: int = rows
        self._columns: int = columns
        self.start: MazeCoordinates = start
        self.goal: MazeCoordinates = goal
        
        self._grid: List[List[Cell]] = [[Cell.EMPTY for _ in range(columns)]
                                         for _ in range(rows)]
        
        self._solved_node = None
        self.path = None
        
        self._randomly_fill_grid(rows, columns, sparseness)
        self._fill_start_and_goal(start, goal)
        
    def _randomly_fill_grid(self, rows: int, columns: int, sparseness: float):
        for row in range(rows):
            for col in range(columns):
                if random.uniform(0, 1.0) < sparseness:
                    self._grid[row][col] = Cell.BLOCKED
        
    def _fill_start_and_goal(self, start: MazeCoordinates, goal: MazeCoordinates):
        self._grid[start.row][start.column] = Cell.START
        self._grid[goal.row][goal.column] = Cell.GOAL
        
    def __str__(self):
        output = ""
        for row in self._grid:
            output += str().join([cell.value for cell in row]) + "\n"
        return output
    
    def goal_test(self, mc: MazeCoordinates) -> bool:
        return mc == self.goal
    
    def get_possible_moves(self, mc: MazeCoordinates) -> List[MazeCoordinates]:
        neighbors = {MazeCoordinates(mc.row + row, mc.column + col) 
                     for row, col in [[-1,0],[1,0],[0,-1],[0,1]]
                     if (mc.row + row >= 0 and 
                         mc.column + col >= 0 and
                         mc.row + row < self._rows and
                         mc.column + col < self._columns)
                     }.difference({mc})
        
        return [neighbor for neighbor in neighbors
                if self._grid[neighbor.row][neighbor.column] != Cell.BLOCKED]
    
    def search(self, collection_type: Union[Stack, Queue]) -> Node or None:
        """Performs search using given collection type as frontier."""
        frontier = collection_type()
        n = Node(self.start, None)
        print(n)
        frontier.push(n)
        print(frontier)
        explored: Set[T] = {self.start}
        
        while not frontier.empty:
            current_node: Node[T] = frontier.pop()
            current_state: T = current_node.state
            
            # End search if goal is reached
            if self.goal_test(current_state):
                self._solved_node = current_node
                return current_node
            
            for child in self.get_possible_moves(current_state):
                if child in explored:
                    continue
                
                explored.add(child)
                
                # Add possible moves not explored to our frontier.
                frontier.push(Node(child, current_node))
        # Failed.
        
    def dfs(self) -> Node or None:
        """Depth-first search of the maze."""
        return self.search(Stack)
    
    def bfs(self) -> Node or None:
        """Breadth-first search of the maze."""
        return self.search(Queue)
    
    def astar_search(self) -> Node or None:
        """A* search of the maze."""
        frontier: PriorityQueue[Node[T]] = PriorityQueue()
        heuristic = distance(self.goal)
        n = Node(self.start, None, 0.0, heuristic(self.start))
        frontier.push(n)
        explored: Dict[T, float] = {self.start: 0.0}
        
        while not frontier.empty:
            current_node: Node[T] = frontier.pop()
            current_state: T = current_node.state
            
            # End search if goal is reached
            if self.goal_test(current_state):
                self._solved_node = current_node
                return current_node
            
            for child in self.get_possible_moves(current_state):
                new_cost: float = current_node.cost + 1
                if child not in explored or explored[child] > new_cost:
                    explored[child] = new_cost
                    frontier.push(Node(child, current_node, new_cost, heuristic(self.goal)))
                # Add possible moves not explored to our frontier.
        # Failed.
    
    def retrace_node_path(self, node: Optional[Node[T]] = None) -> List[T]:
        """Trace the node's parents and returns  list of all nodes it took
        to reach its current state.
        """
        if node is None:
            node =  self._solved_node
        try:
            path: List[T] = [node.state]
        except AttributeError:
            return [node]
        
        while node.parent is not None:
            node = node.parent
            path.append(node.state)
            
        path.reverse()
        self.path = path
        return path
    
    def draw_path(self, path: Optional[List[MazeCoordinates]] = None):
        """Draws the path in text form."""
        if path is None:
            path = self.path
        try:   
            for cell in path:
                self._grid[cell.row][cell.column] = Cell.PATH
            self._grid[self.start.row][self.start.column] = Cell.START
            self._grid[self.goal.row][self.goal.column] = Cell.GOAL
        except TypeError:
            pass
        
            
        print(self)
        
    def clear_path(self, path: Optional[List[MazeCoordinates]] = None):
        """Clears the path."""
        if path is None:
            path = self.path
            
        for cell in path:
            self._grid[cell.row][cell.column] = Cell.EMPTY
        self._grid[self.start.row][self.start.column] = Cell.START
        self._grid[self.goal.row][self.goal.column] = Cell.GOAL
                


    
    
if __name__ == "__main__":
    maze = Maze(start=MazeCoordinates(2,2))
    print(maze)
    
    print(maze.get_possible_moves(maze.start))
    
    
    
    maze.astar_search()
    maze.retrace_node_path()
    maze.draw_path()