from band_members.musician import Musician


class Singer(Musician):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.singer_skills = []

    def learn_new_skill(self, new_skill):
        valid_skills = ["sing high pitch notes", "sing low pitch notes"]
        if new_skill in valid_skills and new_skill not in self.singer_skills:
            self.singer_skills.append(new_skill)
