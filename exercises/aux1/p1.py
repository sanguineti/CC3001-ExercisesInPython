__author__ = "F. Giovanni Sanguineti"
__email__ = "franco.sanguineti@ug.uchile.cl"

# Ejercicio para repasar clases en Python. Si la encapsulación fuera una persona, tendría  mucha pena.

import math


class Pokemon:

    def __init__(self, name, hp, id_number):
        self.name = name
        self.hp = hp
        self.initial_hp = hp
        self.id_number = id_number

    def attack_another_pokemon(self, other):
        damage = math.ceil((self.hp / 3))
        other.let_another_pokemon_attacks_me(damage)

    def let_another_pokemon_attacks_me(self, damage):
        self.hp -= damage

    def is_alive(self):
        return self.hp > 0
