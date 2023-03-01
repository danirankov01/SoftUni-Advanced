number_months_to_word = {
    '01': 'January',
    '02': 'February',
    '03': 'March',
    '04': 'April',
    '05': 'May',
    '06': 'June',
    '07': 'July',
    '08': 'August',
    '09': 'September',
    '10': 'October',
    '11': 'November',
    '12': 'December',
}


class DVD:
    def __init__(self, name, id_number, year, month, age):
        self.name = name
        self.id = id_number
        self.creation_year = year
        self.creation_month = month
        self.age_restriction = age
        self.is_rented = False

    @classmethod
    def from_date(cls, id_number, name, date, age_restriction):
        day, creation_month, creation_year = date.split('.')
        return cls(name, id_number, creation_year, number_months_to_word[creation_month], age_restriction)

    def __repr__(self):
        status = 'rented' if self.is_rented else 'not rented'

        return f"{self.id}: {self.name} ({self.creation_month} " \
               f"{self.creation_year}) has age restriction " \
               f"{self.age_restriction}. Status: {status}"
