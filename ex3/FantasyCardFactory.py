from ex3.CardFactory import CardFactory
from ex0.CreatureCard import CreatureCard
from ex0.Card import Rarity
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from enum import Enum
import random


class Effect(Enum):
    type_1 = "damage"
    type_2 = "heal"
    type_3 = "buff"
    type_4 = "debuff"


class FantasyCardFactory(CardFactory):
    def __init__(self):
        self.creatures = [["Dragon", 5, "Legendary", 6, 12],
                          ["Goblin", 3, "Common", 3, 3],
                          ["Troll", 2, "Common", 2, 4],
                          ["Human King", 4, "Rare", 5, 9]
                          ]
        self.spells = [["Thunder Storm", 3, "Rare", "damage"],
                       ["Regeneration", 2, "Common", "heal"],
                       ["Fireball", 3, "Rare", "damage"],
                       ["Demon Slasher", 4, "Legendary", "damage"]
                       ]
        self.artifacts = [["Diamond Hammer", 3, "Rare", 4,
                           "+3 attack per turn"],
                          ["Mana Ring", 4, "Legendary", 6,
                           "Permanent: +1 mana per turn"],
                          ["Potion of health", 1, "Common", 2,
                           "+2 health per turn"],
                          ["Mana Potion", 2, "Common", 2,
                           "+2 mana per turn"]
                          ]

    def create_creature(self, name_or_power=None):
        if isinstance(name_or_power, str):
            name = name_or_power
            cost = random.randint(1, 7)
            rare_data = random.choice(list(Rarity))
            rare = rare_data.value
            attack = random.randint(2, 8)
            health = random.randint(3, 12)
            return CreatureCard(name, cost, rare, attack, health)
        elif isinstance(name_or_power, int):
            if 0 <= name_or_power < 4:
                return CreatureCard(*self.creatures[name_or_power])
            else:
                raise ValueError("Choose a number between 0 and 4")
        else:
            choice = random.randint(0, 3)
            return CreatureCard(*self.creatures[choice])

    def create_spell(self, name_or_power=None):
        if isinstance(name_or_power, str):
            name = name_or_power
            cost = random.randint(1, 4)
            rare_data = random.choice(list(Rarity))
            rare = rare_data.value
            effect_data = random.choice(list(Effect))
            effect = effect_data.value
            return SpellCard(name, cost, rare, effect)
        elif isinstance(name_or_power, int):
            if 0 <= name_or_power < 4:
                return SpellCard(*self.spells[name_or_power])
            else:
                raise ValueError("Choose a number between 0 and 4")
        else:
            choice = random.randint(0, 3)
            return SpellCard(*self.spells[choice])

    def create_artifact(self, name_or_power=None):
        if isinstance(name_or_power, str):
            name = name_or_power
            cost = random.randint(1, 5)
            rare_data = random.choice(list(Rarity))
            rare = rare_data.value
            durability = random.randint(1, 4)
            effect_data = random.choice(list(Effect))
            effect = effect_data.value
            return ArtifactCard(name, cost, rare, durability, effect)
        elif isinstance(name_or_power, int):
            if 0 <= name_or_power < 4:
                return ArtifactCard(*self.artifacts[name_or_power])
            else:
                raise ValueError("Choose a number between 0 and 4")
        else:
            choice = random.randint(0, 3)
            return ArtifactCard(*self.artifacts[choice])

    def create_themed_deck(self, size):
        deck = {"Creatures": [],
                "Spells": [],
                "Artifacts": []
                }
        for _ in range(size):
            choice = random.choice(["creature", "spell", "artifact"])
            if choice == "creature":
                deck["Creatures"].append(self.create_creature())
            elif choice == "spell":
                deck["Spells"].append(self.create_spell())
            else:
                deck["Artifacts"].append(self.create_artifact())
        return deck

    def get_supported_types(self):
        return {"Creatures": self.creatures,
                "Spells": self.spells,
                "Artifacts": self.artifacts
                }
