from __future__ import annotations
from typing import Tuple, List
from random import randrange, random, choice, sample, shuffle
from copy import deepcopy
from GeneticAlgorithms.chromosome import Chromosome
from GeneticAlgorithms.genetic_algorithm import GeneticAlgorithm


# s, e, n, d, m, o, r, y
# [0, 1, 2, 3, 4, 5, 6, 7]
class SendMoreMoney(Chromosome):
    def __init__(self, code: List[int]):
        self.code = code
        if self.code[4] == 0:
            self.code[4] = choice(list(set(range(1, 10)) - set(self.code)))

    def __str__(self) -> str:
        return f'code={self.code}, fitness: {self.fitness()}'

    def fitness(self) -> float:
        s = self.code[0]
        e = self.code[1]
        n = self.code[2]
        d = self.code[3]
        m = self.code[4]
        o = self.code[5]
        r = self.code[6]
        y = self.code[7]

        # send = (self.code[0] * 1000 + self.code[1] * 100 + self.code[2] * 10 + self.code[3])
        # more = (self.code[4] * 1000 + self.code[5] * 100 + self.code[6] * 10 + self.code[1])
        # money = (self.code[4] * 10000 + self.code[5] * 1000 + self.code[2] * 100 + self.code[1] * 10 + self.code[7])

        send = int(f'{s}{e}{n}{d}')
        more = int(f'{m}{o}{r}{e}')
        money = int(f'{m}{o}{n}{e}{y}')
        return -abs(money - (send + more))

    def p_fitness(self):
        s = self.code[0]
        e = self.code[1]
        n = self.code[2]
        d = self.code[3]
        m = self.code[4]
        o = self.code[5]
        r = self.code[6]
        y = self.code[7]

        # send = (self.code[0] * 1000 + self.code[1] * 100 + self.code[2] * 10 + self.code[3])
        # more = (self.code[4] * 1000 + self.code[5] * 100 + self.code[6] * 10 + self.code[1])
        # money = (self.code[4] * 10000 + self.code[5] * 1000 + self.code[2] * 100 + self.code[1] * 10 + self.code[7])
        out = f"""
{s}{e}{n}{d}
{m}{o}{r}{e}
{m}{o}{n}{e}{y}
"""
        print(out)

        send = int(f'{s}{e}{n}{d}')
        more = int(f'{m}{o}{r}{e}')
        money = int(f'{m}{o}{n}{e}{y}')
        return -abs(money - (send + more))

    @classmethod
    def random_instance(cls) -> SendMoreMoney:
        return SendMoreMoney(sample(range(10), 8))

    def crossover(self, other: SendMoreMoney) -> Tuple[SendMoreMoney, SendMoreMoney]:
        child1: SendMoreMoney = deepcopy(self)
        child2: SendMoreMoney = deepcopy(other)
        for i in range(8):
            if random() > 0.5:
                child1.code[i] = other.code[i]
                child2.code[i] = self.code[i]
        return child1, child2

    def mutate(self) -> None:
        if random() > 0.5:
            return
        else:
            self.code[randrange(8)] = choice(list(set(range(10)) - set(self.code)))
            
        if self.code[4] == 0:
            self.code[4] = choice(list(set(range(1, 10)) - set(self.code)))


if __name__ == '__main__':
    initial_population: List[SendMoreMoney] = [SendMoreMoney.random_instance()
                                               for _ in range(20)]

    ga: GeneticAlgorithm[SendMoreMoney] = GeneticAlgorithm(initial_population,
                                                           threshold=0,
                                                           max_generations=10000,
                                                           mutation_chance=0.3,
                                                           crossover_chance=0.3,
                                                           selection_type=GeneticAlgorithm.SelectionType.TOURNAMENT)
    result: SendMoreMoney = ga.run()
    s = result.code
    print(result)
    print(f"""
      {s[0]} {s[1]} {s[2]} {s[3]}
  +   {s[4]} {s[5]} {s[6]} {s[1]}
    -------------
  = {s[4]} {s[5]} {s[2]} {s[1]} {s[7]}
    """)
    result.p_fitness()

# s, e, n, d, m, o, r, y
# [0, 1, 2, 3, 4, 5, 6, 7]
