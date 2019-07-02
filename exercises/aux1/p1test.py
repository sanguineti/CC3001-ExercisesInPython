from aux1.p1 import Pokemon


def pokemon_info(pokemon):
    print("Imprimiendo Información sobre ", pokemon.name, ":")
    print("ID de la Pokedex: ", pokemon.id_number)
    print("HP Inicial: ", pokemon.initial_hp)
    print("HP Actual: ", pokemon.hp)
    print("Daño recibido: ", pokemon.initial_hp - pokemon.hp)
    if pokemon.is_alive():
        print("Estado: Vivo\n")
    else:
        print("Estado: Muerto\n")


if __name__ == "__main__":
    charizard = Pokemon("Charizard", 47, 6)
    gyarados = Pokemon("Gyarados", 113, 130)

    pokemon_info(gyarados)
    pokemon_info(charizard)

    print("Comienza la Batalla!\n")
    print("Ronda 1\n")
    print("Charizard ataca a Gyarados!\n")

    charizard.attack_another_pokemon(gyarados)

    print("Gyarados ataca a Charizard!\n")

    gyarados.attack_another_pokemon(charizard)

    print("Resumen de la ronda 1: \n")
    pokemon_info(gyarados)
    pokemon_info(charizard)

    print("Ronda 2\n")

    print("Charizard ataca a Gyarados!\n")

    charizard.attack_another_pokemon(gyarados)

    print("Gyarados ataca a Charizard!\n")

    gyarados.attack_another_pokemon(charizard)

    print("Resumen de la ronda 2: \n")
    pokemon_info(gyarados)
    pokemon_info(charizard)

    print("Charizard ha sido derrotado\n")
    print("Gyarados gana la partida!!!")
