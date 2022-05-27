from csp import Constraint, CSP
from typing import Dict, List, Optional, Tuple


class MapColoringConstraint(Constraint[str, str]):
    def __init__(self, place1: str, place2: str):
        super().__init__([place1, place2])
        self.place1 = place1
        self.place2 = place2
        
    def satisfied(self, assignment: Dict[str, str]) -> bool:
        """Returns True if the the colors are not the same"""
        if self.place1 not in assignment or self.place2 not in assignment:
            return True
        
        return assignment[self.place1] != assignment[self.place2]
    

if __name__ == "__main__":
    variables = ['Western Australia', 'Northern Territory', 'South Australia',
                 'Queensland', 'New South Wales', 'Victoria', 'Tasmania']
    domains: Dict[str, List[str]] = {}
    for variable in variables:
        domains[variable] = ['red', 'green', 'blue']
        
    csp: CSP[str, str] = CSP(variables, domains)
    
    shared_borders = [('Western Australia', 'Northern Territory'),
                      ('Western Australia', 'South Australia'),
                      ('South Australia', 'Northern Territory'),
                      ('Queensland', 'Northern Territory'),
                      ('Queensland', 'South Australia'),
                      ('Queensland', 'New South Wales'),
                      ('New South Wales', 'South Australia'),
                      ('Victoria', 'South Australia'),
                      ('Victoria', 'New South Wales'),
                      ('Victoria', 'Tasmania')]
    
    for shared_border in shared_borders:
        csp.add_constraints(MapColoringConstraint(*shared_border))
                      
    solution = csp.backtracking_search()
    
    if solution:
        print(solution)
    else:
        print('No solution.')