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




# Calculate the average success rate for all pokemons for each ball type
average_success_rates_all_pokemon = {ball_type: sum([rates[ball_type] for pokemon, rates in average_success_rates.items()])/len(pokemonName_list) for ball_type in ball_types}

plt.figure()
plt.bar(average_success_rates_all_pokemon.keys(), average_success_rates_all_pokemon.values())
plt.xlabel('Ball Type')
plt.ylabel('Average Success Rate for All Pokemon')
plt.title('Average Success Rate for All Pokemon with Different Ball Types')
plt.show()

# Plot the average success rates for each pokemon and each ball type
for pokemon, rates in average_success_rates.items():
    plt.figure()
    plt.bar(rates.keys(), rates.values())
    plt.xlabel('Ball Type')
    plt.ylabel('Success Rate')
    plt.title(f'Success Rate of Catching {pokemon.capitalize()} with Different Ball Types')
    plt.show()


for pokemon_name in pokemonName_list:
    for ball_type in ball_types:
        # Initialize lists to store HP and success rate data for this pokemon and ball type
        hp_list = []
        success_rate_list = []

        # Loop over HP values from 10 to 100 with step size 10
        for hp in range(10, 101, 10):
            pokemon = factory.create(pokemon_name, hp, StatusEffect.NONE, 1)
            success_count = 0
            for _ in range(num_attempts):
                attempt_result, capture_rate = attempt_catch(pokemon, ball_type, noise_level)
                if attempt_result:
                    success_count += 1
            success_rate = success_count / num_attempts
            hp_list.append(hp)
            success_rate_list.append(success_rate)

        # Plot the success rates for this pokemon and ball type
        plt.plot(hp_list, success_rate_list, label=pokemon_name)
        plt.xlabel('HP')
        plt.ylabel('Success Rate')
        plt.title(f'Success Rate for {ball_type}')
        plt.legend()
        plt.show()
