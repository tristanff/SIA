# Author : Tristan Flechard ---- 07/03/2024

import matplotlib.pyplot as plt
from pokemon import PokemonFactory, StatusEffect
from catching import attempt_catch

factory = PokemonFactory("pokemon.json")
num_attempts = 100
noise_level = 0.15

pokemonName_list = ["snorlax", "jolteon", "caterpie", "onix", "mewtwo"]
ball_types = ['pokeball', 'ultraball', 'fastball' , 'heavyball']

# Create a nested dictionary to store success rates for all pokemon and all ball types
success_rates_dict = {pokemon: {ball_type: [] for ball_type in ball_types} for pokemon in pokemonName_list}

# Loop for each pokemon
for pokemon_name in pokemonName_list:
    pokemon = factory.create(pokemon_name, 100, StatusEffect.NONE, 1)
    for ball_type in ball_types:
        success_count = 0
        for _ in range(num_attempts):
            attempt_result, capture_rate = attempt_catch(pokemon, ball_type, noise_level)
            if attempt_result:
                success_count += 1
        success_rate = success_count / num_attempts
        # Append the success rate to the appropriate list in the nested dictionary
        success_rates_dict[pokemon_name][ball_type].append(success_rate)


# Calculate the average success rate for each pokemon and each ball type
average_success_rates = {pokemon: {ball_type: sum(success_rates) / len(success_rates) for ball_type, success_rates in rates.items()} for pokemon, rates in success_rates_dict.items()}

# Plot the average success rates for each pokemon and each ball type
for pokemon, rates in average_success_rates.items():
    plt.figure()
    plt.bar(rates.keys(), rates.values())
    plt.xlabel('Ball Type')
    plt.ylabel('Success Rate')
    plt.title(f'Success Rate of Catching {pokemon.capitalize()} with Different Ball Types')
    plt.show()


# Calculate the average success rate for all pokemons for each ball type
average_success_rates_all_pokemon = {ball_type: sum([rates[ball_type] for pokemon, rates in average_success_rates.items()])/len(pokemonName_list) for ball_type in ball_types}

plt.figure()
plt.bar(average_success_rates_all_pokemon.keys(), average_success_rates_all_pokemon.values())
plt.xlabel('Ball Type')
plt.ylabel('Average Success Rate for All Pokemon')
plt.title('Average Success Rate for All Pokemon with Different Ball Types')
plt.show()
