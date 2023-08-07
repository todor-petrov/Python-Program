from project.formula_teams.formula_team import FormulaTeam


class RedBullTeam(FormulaTeam):

    SPONSORS = {'Oracle': {1: 1500000, 2: 800000},
                'Honda': {8: 20000, 10: 10000}}
    EXPENSES = 250000

    def __init__(self, budget):
        super().__init__(budget)
