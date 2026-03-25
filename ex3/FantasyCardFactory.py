from ex3.CardFactory import CardFactory
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck
import random

class FantasyCardFactory(CardFactory):
    def __init__(self):
        self.creatures = ["Dragon", "Goblin", "Troll", "Human King"]
        self.spells = ["Thunder Storm", "Regeneration", "Fireball"]
        self.artifacts = ["Diamond Hammer", "Mana Ring", "Potion of health", "Demon Slasher"]
        self.rarity = ["Commun", "Legendary", "Rare"]
        self.effect_type = ["damage", "heal", "debuff", "buff"]

    def create_creature(self, name_or_power = None):
        if isinstance(name_or_power, str):
            name = name_or_power
        else:
            name = random.choice(self.creatures)
        cost = random.randint(1, 6)
        rare = random.choice(self.rarity)
        attack = random.randint(1, 7)
        health = random.randint(3, 12)
        return CreatureCard(name, cost, rare, attack, health)
    
    def create_spell(self, name_or_power = None):
        if isinstance(name_or_power, str):
            name = name_or_power
        else:
            name = random.choice(self.spells)
        cost = random.randint(1, 4)
        rare = random.choice(self.rarity)
        effect= random.choice(self.effect_type)
        return SpellCard(name, cost, rare, effect)
    
    def create_artifact(self, name_or_power = None):
        if isinstance(name_or_power, str):
            name = name_or_power
        else:
            name = random.choice(self.artifacts)
        cost = random.randint(1, 4)
        rare = random.choice(self.rarity)
        durability = random.randint(1, 3)
        effect = random.choice(self.effect_type)
        return ArtifactCard(name, cost, rare, durability, effect)
    
    def create_themed_deck(self, size):
        deck = { "Creatures": [],
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