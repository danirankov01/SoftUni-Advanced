from band import Band
from concert import Concert


class ConcertTrackerApp:
    def __init__(self):
        self.bands = []
        self.musicians = []
        self.concerts = []

    def create_band(self, name):
        try:
            band_name = next(filter(lambda b: b.name == name, self.bands))
        except StopIteration:
            band = Band(name)
            self.bands.append(band)
            return f"{name} was created."

        raise Exception(f"{name} band is already created!")

    def create_concert(self, genre, audience, ticket_price, expenses, place):
        try:
            concert_place = next(filter(lambda c: c.place == place, self.concerts))
        except:
            concert = Concert(genre, audience, ticket_price, expenses, place)
            self.concerts.append(concert)
            return f"{genre} concert in {place} was added."

        raise Exception(f"{place} is already registered for {genre} concert!")

    def add_musician_to_band(self, musician_name, band_name):
        try:
            m_name = next(filter(lambda m: m.name == musician_name, self.musicians))
        except:
            raise Exception(f"{musician_name} isn't a musician!")

        try:
            b_name = next(filter(lambda b: b.name == band_name, self.bands))
        except:
            raise Exception(f"{band_name} isn't a band!")

        self.bands.append(m_name)
        return f"{musician_name} was added to {band_name}"

    def remove_musician_from_band(self, musician_name, band_name):
        try:
            b_name = next(filter(lambda b: b.name == band_name, self.bands))
        except:
            raise Exception(f"{band_name} isn't a band!")













