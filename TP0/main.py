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
######################### Question 1 ######################################################
    factory = PokemonFactory("pokemon.json")
    num_attempts = 100
    noise_level = 0.15

    pokemonName_list = ["snorlax", "jolteon", "caterpie", "onix", "mewtwo"]
    ball_types = ['pokeball', 'ultraball', 'fastball' , 'heavyball']
    # The tab that contains the pokemon objects
    pokemons = []

    for pokemon_name in pokemonName_list:
        pokemon = factory.create(pokemon_name, 100, StatusEffect.NONE, 1)
        pokemons.append(pokemon)

    success_rates = []
    for pokemon in pokemons:
        success_count = 0
        for _ in range(num_attempts):
            attempt_result, capture_rate = attempt_catch(pokemon, 'heavyball', noise_level)
            if attempt_result:
                success_count += 1
        success_rate = success_count / num_attempts
        success_rates.append(success_rate)

    plt.bar(pokemonName_list, success_rates)
    plt.xlabel('Pokémon')
    plt.ylabel('Success Rate')
    plt.title('Success Rate of Catching Pokémon')
    plt.show()
    ############################################### Question 2 ##########################################################"
    tab_succes_rates = {}
    success_rates_dict = {}
    for pokemon in pokemons:
        for ball_type in ball_types:
            success_count = 0
            for _ in range(num_attempts):
                attempt_result , attempt_probability = attempt_catch(pokemon, ball_type, noise_level)
                if attempt_result:
                    success_count += 1
            success_rate = success_count / num_attempts
            success_rates_dict[ball_type] = success_rate
        tab_succes_rates[pokemon.name] = success_rates_dict
    print(tab_succes_rates)

    dict_pokestats = {'pokeball' : 0.0 , 'fastball' : 0.0 , 'ultraball' : 0.0 , 'heavyball' : 0}
    for pokestat in tab_succes_rates.values():
        dict_pokestats['heavyball']+= pokestat['heavyball']
        dict_pokestats['fastball']+=pokestat['fastball']
        dict_pokestats['ultraball']+=pokestat['ultraball']
        dict_pokestats['pokeball'] += pokestat['pokeball']


    dict_pokestats['heavyball'] = dict_pokestats['heavyball'] / 5
    dict_pokestats['fastball'] = dict_pokestats['fastball'] / 5
    dict_pokestats['ultraball'] = dict_pokestats['ultraball'] / 5
    dict_pokestats['pokeball'] = dict_pokestats['pokeball'] /5
    print(dict_pokestats)

    plt.bar(dict_pokestats.keys(), dict_pokestats.values())
    plt.xlabel('Ball Type')
    plt.ylabel('Success Rate')
    plt.title('Success'
              ' Rates for Different Ball Types')
    plt.show()

    for pokemon, rates in tab_succes_rates.items():
        plt.figure()
        plt.bar(rates.keys(), rates.values())
        plt.xlabel('Ball Type')
        plt.ylabel('Success Rate')
        plt.title(f'Success Rate of Catching {pokemon.capitalize()} with Different Ball Types')
        plt.show()


