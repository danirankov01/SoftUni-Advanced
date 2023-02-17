class Pokemon:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def pokemon_details(self):
        return f"{self.name} with health {self.health}"


class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemons = []

    def add_pokemon(self, pokemon: Pokemon):
        if(pokemon.name in self.pokemons):
            return "This pokemon is already caught"
        
        self.pokemons.append(pokemon)
        return f"Caught {pokemon.pokemon_details()}"

    def release_pokemon(self, pokemon_name):
        if(pokemon_name in self.pokemons):
            self.pokemons.remove(pokemon_name)
            return f"You have released {pokemon_name}"

        return "Pokemon is not caught"

    def trainer_data(self):
        result = []
        result.append(f"Pokemon Trainer {self.name}")
        result.append(f"Pokemon count {len(self.pokemons)}")
        for i in range(len(self.pokemons)):
            result.append(f"- {self.pokemons[i].pokemon_details()}")

        return '\n'.join(result)
        

pokemon = Pokemon("Pikachu", 90)
print(pokemon.pokemon_details())
trainer = Trainer("Ash")
print(trainer.add_pokemon(pokemon))
second_pokemon = Pokemon("Charizard", 110)
print(trainer.add_pokemon(second_pokemon))
print(trainer.add_pokemon(second_pokemon))
print(trainer.release_pokemon("Pikachu"))
print(trainer.release_pokemon("Pikachu"))
print(trainer.trainer_data())
