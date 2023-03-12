from project_f1_manager.formula_teams.formula_team import FormulaTeam


class RedBullTeam(FormulaTeam):
    RED_BULL_EXPENSES = 250000

    def __init__(self, budget):
        super().__init__(budget)

    @property
    def sponsors(self):
        return {
            "Oracle": {
                1: 1500000,
                2: 800000,
            },
            "Honda": {
                8: 10000,
                10: 10000,
            }
        }

    def expenses_for_one_race(self):
        pass

    def calculate_revenue_after_race(self, race_pos):
        pass