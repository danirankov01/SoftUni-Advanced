from project_movie_world.customer import Customer
from project_movie_world.dvd import DVD


class MovieWorld:
    def __init__(self, name):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer: Customer):
        if MovieWorld.customer_capacity() > len(self.customers):
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if MovieWorld.dvd_capacity() > len(self.dvds):
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id, dvd_id):
        for customer in self.customers:
            if customer.id == customer_id:
                for dvd in customer.rented_dvds:
                    if dvd.id == dvd_id:
                        return f"{customer.name} has already rented {dvd.name}"
            elif customer.id != customer_id:
                for dvd in customer.rented_dvds:
                    if dvd.id == dvd_id:
                        return "DVD is already rented"

        for customer in self.customers:
            if customer.id == customer_id:
                for dvd in self.dvds:
                    if dvd.id == dvd_id:
                        if customer.age < dvd.age_restriction:
                            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"

                        customer.rented_dvds.append(dvd)
                        dvd.is_rented = True
                        return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        for customer in self.customers:
            if customer.id == customer_id:
                for dvd in customer.rented_dvds:
                    if dvd.id == dvd_id:
                        dvd.is_rented = False
                        del customer.rented_dvds[dvd]
                        return f"{customer.name} has successfully returned {dvd.name}"

                return f"{customer.name} does not have that DVD"

    def __repr__(self):
        result = ""
        for customer in self.customers:
            result += f"{str(customer)}\n"

        for dvd in self.dvds:
            result += f"{str(dvd)}\n"

        return result.rstrip()
