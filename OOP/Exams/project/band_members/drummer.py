from band_members.musician import Musician


class Drummer(Musician):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.drummer_skills = []

    def learn_new_skill(self, new_skill):
        valid_skills = ["play the drums with drumsticks", "play the drums with drum brushes", "read sheet music"]
        if new_skill in valid_skills and new_skill not in self.drummer_skills:
            self.drummer_skills.append(new_skill)
