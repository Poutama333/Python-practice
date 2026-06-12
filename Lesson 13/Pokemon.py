# =====================================================================
# PROJECT: Pokemon
# Create a battle program where you battle a random pokemon
# =====================================================================
KEY_NAME = "name"
KEY_HEALTH = "health"
KEY_ATTACK = "attack"
# TODO Import random module
import random
# Wild Pokemon
pokemon_list = [
    {KEY_NAME:"Bulbasaur",KEY_HEALTH:21},
    {KEY_NAME:"Charmander",KEY_HEALTH:22},
    {KEY_NAME:"Squirtle",KEY_HEALTH:20},
    {KEY_NAME:"Pikachu",KEY_HEALTH:19}
]

# TODO Create a multidimensional list that holds 4 pokemon names and their max health (you choose)
# User Pokemon
# TODO Create a multidimensional list that holds 4 pokemon attacks and their different damage
pokemon_attacks = [
    {"1.Bite the curb",40},
    {"2.Chokeslam",60},
    {"3.Waterboard",80},
    {KEY_NAME:"4.Whip",KEY_ATTACK:10}
]
wild_pokemon = random.choice(pokemon_list)
# TODO Create a variable to hold a randomised wild pokemon
pokemon_health = int(wild_pokemon[KEY_HEALTH])
print("You have encountered a wild",wild_pokemon[KEY_NAME])
# TODO Create a current_health variable and set it to the max health of the random pokemon
# TODO Tell the user what pokemon they're facing
# TODO Create a while loop that continues until current health <= 0
while pokemon_health > 0:
    print(pokemon_attacks)
    attack = input("Which attack would you like to use? ").strip()
    int(attack)
    
    int(attack_damage = (pokemon_attacks[attack],[1]))
    print("Your",pokemon_attacks[attack],"does",attack_damage,"damage")
    print(pokemon_health - attack_damage)
    print("The opposing",wild_pokemon,"has",pokemon_health,"health")
    #except: 
        #print("Error, try typing a number from 1 to 4")
        #continue
print("Nice work, you have defeated the wild",wild_pokemon[0])
    # TODO Ask the user which attack they'd like to use (list all 4 options, numbered); save input
    # TODO Use try except to ensure the user has input a number; if they didn't tell them so and then use 'continue' to restart the loop
    # TODO Using the number, get the attack damage value and minus it from current health

# TODO Tell the user they defeated the pokemon

# ====================================================
# EXTENSION
# NOTE: Only do the extension once you have completed the project update (with dictionaries)

# TODO: Give your wild pokemon each an attack value as well, then allow it to attack the user back each turn (You'' need a player health)
# TODO: Change your 'user pokemon' to a list of different pokemon they can choose from. Each pokemon will have their own list of attacks.
# TODO: Give all pokemon a type. Create a new dictionary of types that each has a dictionary of strengths and weaknesses. Use this to change the damage.