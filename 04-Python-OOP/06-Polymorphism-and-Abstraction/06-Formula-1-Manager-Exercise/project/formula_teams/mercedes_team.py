from project.formula_teams.formula_team import FormulaTeam


class MercedesTeam(FormulaTeam):

    SPONSORS = {'Petronas': {1: 1000000, 3: 500000},
                'TeamViewer': {5: 100000, 7: 50000}}
    EXPENSES = 200000

    def __init__(self, budget):
        super().__init__(budget)
