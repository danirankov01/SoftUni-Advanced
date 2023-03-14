from band_members.musician import Musician


class Guitarist(Musician):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.guitarist_skills = []

    def learn_new_skill(self, new_skill):
        valid_skills = ["play metal", "play rock", "play jazz"]
        if new_skill in valid_skills and new_skill not in self.guitarist_skills:
            self.guitarist_skills.append(new_skill)
