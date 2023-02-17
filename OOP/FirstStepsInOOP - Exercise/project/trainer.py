from pokemon import Pokemon


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
        result.extend(f"Pokemon Trainer {self.name}", f"Pokemon count {len(self.pokemons)}")
        for i in range(len(self.pokemons)):
            result.append(f"- {self.pokemons[i].pokemon_details()}")

        return '\n'.join(result)