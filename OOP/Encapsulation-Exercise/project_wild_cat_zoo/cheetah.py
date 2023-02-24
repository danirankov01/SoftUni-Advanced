from project_wild_cat_zoo.animal import Animal


class Cheetah(Animal):
    def __init__(self, name, gender, age, money_for_care=0):
        super().__init__(name, gender, age, money_for_care)
        self.money_for_care = 60
