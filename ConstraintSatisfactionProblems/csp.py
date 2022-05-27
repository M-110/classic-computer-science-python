from typing import Generic, TypeVar, Dict, List, Optional
from abc import ABC, abstractmethod

V = TypeVar('V') # Variable Type
D = TypeVar('D') # Domain Type

class Constraint(Generic[V, D], ABC):
    def __init__(self, variables: List[V]):
        self.variables = variables
        
    @abstractmethod
    def satisfied(self, assignment: Dict[V, D]) -> bool:
        ...
        
    
class CSP(Generic[V, D]):
    def __init__(self, variables: List[V], domains: Dict[V, List[D]]):
        self.variables = variables
        self.domains = domains
        self.constraints = {}
        for variable in self.variables:
            self.constraints[variable] = []
            if variable not in self.domains:
                raise LookupError("Every variable should have a domain.")
                
    def add_constraints(self, constraint: Constraint[V, D]):
        for variable in constraint.variables:
            if variable not in self.variables:
                raise LookupError(f'{variable!r} not in CSP.')
            else:
                self.constraints[variable].append(constraint)
                
    def consistent(self, variable: V, assignment: Dict[V, D]) -> bool:
        for constraint in self.constraints[variable]:
            if not constraint.satisfied(assignment):
                return False
        return True
    
    def backtracking_search(self, assignment: Dict[V, D] = None) -> Optional[Dict[V,D]]:
        if assignment is None:
            assignment = {}
        
        if len(assignment) == len(self.variables):
            return assignment
        
        unassigned: List[V] = [var for var in self.variables
                               if var not in assignment]
        
        first: V = unassigned[0]
        for value in self.domains[first]:
            local_assignment = assignment.copy()
            local_assignment[first] = value
            
            if self.consistent(first, local_assignment):
                result = self.backtracking_search(local_assignment)
                if result is not None:
                    return result
        return None