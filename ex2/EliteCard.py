from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical
from ex1.SpellCard import SpellCard

class EliteCard(Card, Combatable, Magical):
    def __init__(self, name: str, cost: int, rarity: str, damage: int, health,combat_type: str, defense: int):
        super().__init__(name, cost, rarity)
        self.type = "Elite Card"
        self.damage = damage
        self.health = health
        self.combat_type = combat_type
        self.defense = defense
        self.spells = []

    def play(self, game_state: dict) -> dict:
        if game_state['mana'] < self.cost:
            raise ValueError("Not enough mana")
        game_state["mana"] -= self.cost
        game_state["board"].append(self.name)
        return {"card_played": self.name,
                "mana_used": self.cost,
                "effect": "Elite Card has been played."
                }

    def attack(self, target) -> dict:
        if not isinstance(target, Card):
            raise ValueError("Invalid type of card")
        return {"attacker": self.name,
                "target": target.name,
                "damage": self.damage,
                "combat_type": self.combat_type
                }

    def defend(self, incoming_damage: int) -> dict:
        if not isinstance(incoming_damage, int):
            raise ValueError("Invalid data damage received.")
        blocked = min(incoming_damage, self.defense)
        damage_received = incoming_damage - self.defense
        if damage_received <= 0:
            damage_received = 0
        self.health -= damage_received
        alive = True
        if self.health <= 0:
            alive = False
        return {'defender': self.name,
                'damage_taken': damage_received,
                'damage_blocked': self.defense,
                'still_alive': alive
                }

    def get_combat_stats(self) -> dict:
        return {"Card played": self.name,
                "health": self.health,
                "Attack": self.damage,
                "Defense": self.defense,
                "Style": self.combat_type
                }
    
    def channel_mana(self, amount: int) -> dict:
        return {"channeled": amount,
                "total_mana": amount + self.cost
                }

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        self.spells.append(spell_name)
        return {"caster": self.name,
                'spell': spell_name,
                "targets": [target.name for target in targets if isinstance(target, Card)],
                "mana_used": self.cost
                }
    
    def get_magic_stats(self) -> dict:
        return {"Cost": self.cost,
                "Type": self.type
                }