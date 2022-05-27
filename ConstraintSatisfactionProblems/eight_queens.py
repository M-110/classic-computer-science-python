from csp import Constraint, CSP
from typing import Dict, List, Optional, Tuple

    
class QueenConstraint(Constraint[int, int]):
    def __init__(self, columns: List[int]):
        super().__init__(columns)
        self.columns = columns
        
    def satisfied(self, assignment: Dict[int, int]) -> bool:
        for qc1, qr1 in assignment.items():
            for qc2 in range(qc1 + 1, len(self.columns) + 1):
                if qc2 in assignment:
                    qr2: int = assignment[qc2]
                    if qr1 == qr2:
                        return False
                    if abs(qr1 - qr2) == abs(qc1 - qc2):
                        return False
        return True
                    
    

if __name__ == "__main__":
    cols = list(range(1,9))
    rows = {col: list(range(1, 9)) for col in cols}
    csp = CSP(cols, rows)
    csp.add_constraints(QueenConstraint(cols))
    
    solution = csp.backtracking_search()
    
    if solution:
        print(solution)
    else:
        print('No solution.')