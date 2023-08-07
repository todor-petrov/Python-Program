from abc import ABC, abstractmethod


class FormulaTeam(ABC):
    SPONSORS = {}
    EXPENSES = 0

    def __init__(self, budget):
        self.budget = budget

    @property
    def budget(self):
        return self._budget

    @budget.setter
    def budget(self, value):
        if value < 1000000:
            raise ValueError('F1 is an expensive sport, find more sponsors!')
        self._budget = value

    def calculate_revenue_after_race(self, race_pos: int):
        revenue = 0
        for sponsor in self.SPONSORS:
            for place in self.SPONSORS[sponsor]:
                if race_pos <= place:
                    revenue += self.SPONSORS[sponsor][place]
                    break
        revenue -= self.EXPENSES
        self.budget += revenue
        return f'The revenue after the race is {revenue}$. Current budget {self.budget}$'
