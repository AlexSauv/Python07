from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex2.Combatable import Combatable
from ex2.Magical import Magical
from ex1.SpellCard import SpellCard
from enum import Enum
import random

class Combat_Style(Enum):
    type_1 = "Melee"
    type_2 = "Mid-Distance"
    type_3 = "Long-Distance"


class EliteCard(Card, Combatable, Magical):
    def __init__(self, name: str, cost: int, rarity: str, damage: int, health: int , defense: int):
        super().__init__(name, cost, rarity)
        self.type = "Elite Card"
        if health < 0: raise ValueError("Health stats must be at least 0")
        if damage < 0: raise ValueError("Attack stats must be above 0")
        if defense < 0: raise ValueError("Defense stats must be at least 0")
        self.health = health
        self.damage = damage
        self.defense = defense
        self.combat: int = random.choice(list(Combat_Style))
        self.combat_type: str = self.combat.value
        self.mana_spell: int = 4
        self.spells = [SpellCard("FireBall", 1, "Common", "damage"),
                           SpellCard("EarthStrike", 2, "Common", "damage"),
                           SpellCard("DemonSlasher", 4, "Legendary", "damage"),
                           SpellCard("FireBlast", 1, "Common", "damage"),
                           SpellCard("Meteor", 3, "rare", "damage"),
                           SpellCard("Magic Dart", 1, "Common", "damage")
                           ]
        self.dead: bool = False

    def play(self, game_state: dict) -> dict:
        if game_state['mana'] < self.cost:
            raise ValueError("Not enough mana")
        game_state["mana"] -= self.cost
        if "player_side" not in game_state:
            game_state.update({"player_side": []})
        game_state.setdefault("player_side", []).append(self)
        return {"card_played": self.name,
                "mana_used": self.cost,
                "effect": f"{self.name} has been played."
                }

    def attack(self, target) -> dict:
        if not isinstance(target, (CreatureCard, EliteCard)):
            raise ValueError("The card type must be: Creature or Elite.")
        if isinstance(target, EliteCard):
            defense_state = target.defend(self.damage)
            damage_done = defense_state["damage_blocked"]
        if isinstance(target, CreatureCard):
            target.health -= self.damage
            damage_done = self.damage
        if target.health <= 0:
               target.dead = True        
        return {"attacker": self.name,
                "target": target.name,
                "damage": damage_done,
                "combat_type": self.combat_type,
                "target_dead": target.dead 
                }

    def defend(self, incoming_damage: int) -> dict:
        if not isinstance(incoming_damage, int):
            raise ValueError("Invalid data damage received.")
        damage_received = incoming_damage - self.defense
        if damage_received <= 0:
            damage_received = 0
        self.health -= damage_received
        if self.health <= 0:
            self.dead = True
        return {'defender': self.name,
                'damage_taken': damage_received,
                'damage_blocked': self.defense,
                'still_alive': self.dead
                }

    def get_combat_stats(self) -> dict:
        return {"Card played": self.name,
                "health": self.health,
                "Attack": self.damage,
                "Defense": self.defense,
                "Style": self.combat_type
                }
    
    def channel_mana(self, amount: int) -> dict:
        if not isinstance(amount, int):
            raise ValueError("Mana received must be on integer.")
        self.mana_spell += amount
        return {"channeled": amount,
                "total_mana": self.mana_spell
                }

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        if not isinstance(targets, list):
            raise ValueError("Cast Spell: Targets must be given as a list")
        for target in targets:
            if not isinstance(target, (CreatureCard,EliteCard)):
                raise ValueError("Each target type must be either Creature or Elite")
        spell = next((spell for spell in self.spells if spell.name == spell_name), None)
        if not spell:
            raise ValueError("Give a valid spell name e.g: FireBlast, Meteor, Magic Dart")
        spell.resolve_effect(targets)
        self.mana_spell -= spell.cost
        return {"caster": self.name,
                'spell': spell_name,
                "targets": [target.name for target in targets if isinstance(target, (CreatureCard, ))],
                "targets_health": [target.health for target in targets],
                "mana_used": spell.cost
                }
    
    def get_magic_stats(self) -> dict:
        return {
                "Spells": [spell.name for spell in self.spells],
                "Cost": [spell.cost for spell in self.spells],
                "Rarity": [spell.rarity for spell in self.spells],
                "Types effect": [spell.effect_type for spell in self.spells]
                }