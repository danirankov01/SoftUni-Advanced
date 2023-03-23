from project.band import Band
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.musician import Musician
from project.band_members.singer import Singer
from project.concert import Concert


class ConcertTrackerApp:
    VALID_TYPES_OF_MUSICIANS = {
        "Guitarist": Guitarist,
        "Drummer": Drummer,
        "Singer": Singer
    }

    VALID_TYPES_OF_CONCERTS = [
        "Rock",
        "Metal",
        "Jazz"
    ]

    def __init__(self):
        self.bands = []
        self.musicians = []
        self.concerts = []

    def create_musician(self, musician_type, name, age):
        if musician_type not in ConcertTrackerApp.VALID_TYPES_OF_MUSICIANS:
            raise ValueError("Invalid musician type!")

        if name in [m.name for m in self.musicians]:
            raise Exception(f"{name} is already a musician!")

        self.musicians.append(self.VALID_TYPES_OF_MUSICIANS[musician_type](name, age))
        return f"{name} is now a {musician_type}."

    def create_band(self, name):
        if name in [b.name for b in self.bands]:
            raise Exception(f"{name} band is already created!")

        self.bands.append(Band(name))
        return f"{name} was created."

    def create_concert(self, genre, audience, ticket_price, expenses, place):
        try:
            concert = next(filter(lambda c: c.place == place, self.concerts))
        except StopIteration:
            self.concerts.append(Concert(genre, audience, ticket_price, expenses, place))
            return f"{genre} concert in {place} was added."

        raise Exception(f"{concert.place} is already registered for {concert.genre} concert!")

    def add_musician_to_band(self, musician_name, band_name):
        try:
            musician = next(filter(lambda m: m.name == musician_name, self.musicians))
        except StopIteration:
            raise Exception(f"{musician_name} isn't a musician!")

        try:
            band = next(filter(lambda b: b.name == band_name, self.bands))
        except StopIteration:
            raise Exception(f"{band_name} isn't a band!")

        band.members.append(musician)
        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name, band_name):
        try:
            band = next(filter(lambda b: b.name == band_name, self.bands))
        except StopIteration:
            raise Exception(f"{band_name} isn't a band!")

        if musician_name not in [b.name for b in band.members]:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")

        musician = next(filter(lambda m: m.name == musician_name, self.musicians))
        band.members.remove(musician)
        return f"{musician_name} was removed from {band_name}."

    def start_concert(self, concert_place, band_name):
        band = next(filter(lambda b: b.name == band_name, self.bands))

        singer = 0
        drummer = 0
        guitarist = 0

        for member in band.members:
            if member.__class__.__name__ == "Singer":
                singer += 1

            elif member.__class__.__name__ == "Drummer":
                drummer += 1

            elif member.__class__.__name__ == "Guitarist":
                guitarist += 1

        if singer == 0 or drummer == 0 or guitarist == 0:
            raise Exception(f"{band.name} can't start the concert because it doesn't have enough members!")

        concert = next(filter(lambda c: c.place == concert_place, self.concerts))

        result_concert_type = ""

        for types in ConcertTrackerApp.VALID_TYPES_OF_CONCERTS:
            singer, drummer, guitarist = False, False, False

            if concert.genre == "Rock":
                for members in band.members:
                    if members.__class__.__name__ == "Singer" and "sing high pitch notes" in members.skills:
                        singer = True
                    elif members.__class__.__name__ == "Drummer" and "play the drums with drumsticks" in members.skills:
                        drummer = True
                    elif members.__class__.__name__ == "Guitarist" and "play rock" in members.skills:
                        guitarist = True

            elif concert.genre == "Metal":
                for members in band.members:
                    if members.__class__.__name__ == "Singer" and "sing low pitch notes" in members.skills:
                        singer = True
                    elif members.__class__.__name__ == "Drummer" and "play the drums with drumsticks" in members.skills:
                        drummer = True
                    elif members.__class__.__name__ == "Guitarist" and "play metal" in members.skills:
                        guitarist = True

            elif concert.genre == "Jazz":
                for members in band.members:
                    if members.__class__.__name__ == "Singer" and "sing high pitch notes and sing low pitch notes" in members.skills:
                        singer = True
                    elif members.__class__.__name__ == "Drummer" and "play the drums with drum brushes" in members.skills:
                        drummer = True
                    elif members.__class__.__name__ == "Guitarist" and "play jazz" in members.skills:
                        guitarist = True

            if singer and drummer and guitarist:
                result_concert_type = types
                break

        if not singer or not drummer or not guitarist:
            raise Exception(f"The {band_name} band is not ready to play at the concert!")

        profit = (concert.audience * concert.ticket_price) - concert.expenses
        result_profit = "{:.2f}".format(profit)
        return f"{band_name} gained {result_profit}$ from the {result_concert_type} concert in {concert_place}."
