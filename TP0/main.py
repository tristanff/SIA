from catching import attempt_catch
from pokemon import PokemonFactory, StatusEffect
import json
import random
import matplotlib.pyplot as plt


if __name__ == "__main__":
    factory = PokemonFactory("pokemon.json")
    snorlax = factory.create("snorlax", 100, StatusEffect.NONE, 1)
    print("No noise: ", attempt_catch(snorlax, "heavyball"))
    for _ in range(10):
        print("Noisy: ", attempt_catch(snorlax, "heavyball", 0.15))

    factory = PokemonFactory("pokemon.json")
    ball_type = "heavyball"
    num_attempts = 100
    noise_level = 0.15

    pokemonName_list = ["snorlax", "jolteon", "caterpie", "onix", "mewtwo"]
    # The tab that contains the pokemon objects
    pokemons = []

    for pokemon_name in pokemonName_list:
        pokemon = factory.create(pokemon_name, 100, StatusEffect.NONE, 1)
        pokemons.append(pokemon)

    success_rates = []
    for pokemon in pokemons:
        success_count = 0
        for _ in range(num_attempts):
            attempt_result, capture_rate = attempt_catch(pokemon, ball_type, noise_level)
            if attempt_result:
                success_count += 1
        success_rate = success_count / num_attempts
        success_rates.append(success_rate)

    plt.bar(pokemonName_list, success_rates)
    plt.xlabel('Pokémon')
    plt.ylabel('Success Rate')
    plt.title('Success Rate of Catching Pokémon')
    plt.show()
