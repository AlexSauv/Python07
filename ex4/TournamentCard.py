from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable
import random


class TournamentCard(Card, Combatable, Rankable):
    def __init__(self, name: str, cost: int, rarity: str,
                 attack: int, health: int, card_id: str):
        super().__init__(name, cost, rarity)
        if health < 0:
            raise ValueError("Health stats must be at least 0")
        if attack < 0:
            raise ValueError("Attack stats must be above 0")
        self.card_id: str = card_id
        self.damage = attack
        self.health = health
        self.sheild: int = random.randint(1, 4)
        self.wins: int = 0
        self.losses: int = 0
        self.rating: int = 1200
        self.dead: bool = False

    def play(self, game_state: dict) -> dict:
        if game_state['mana'] < self.cost:
            raise ValueError("Not enough mana")
        game_state["mana"] -= self.cost
        return {"card_played": self.name,
                "mana_used": self.cost,
                "Effect": f"{self.name} is entering in the battlefield"
                }

    def attack(self, target) -> dict:
        if not isinstance(target, (TournamentCard)):
            raise ValueError("The card type must be: Tournament.")
        defense_state = target.defend(self.damage)
        damage_done = defense_state["damage_taken"]
        if target.health <= 0:
            target.health = 0
            target.dead = True
        return {"attacker": self.name,
                "target": target.name,
                "damage": damage_done,
                "target_dead": target.dead
                }

    def defend(self, incoming_damage: int) -> dict:
        if not isinstance(incoming_damage, int):
            raise ValueError("Invalid data damage received.")
        damage_received = incoming_damage - self.sheild
        if damage_received <= 0:
            damage_received = 0
        self.health -= damage_received
        if self.health <= 0:
            self.dead = True
        return {'defender': self.name,
                'damage_taken': damage_received,
                'damage_blocked': self.sheild,
                'still_alive': not self.dead
                }

    def calculate_rating(self) -> int:
        self.rating = 1200 + (self.wins * 16) - (self.losses * 66)
        return self.rating

    def get_combat_stats(self) -> dict:
        return {"name": self.name,
                "health": self.health,
                "Attack": self.damage,
                "Defense": self.sheild,
                }

    def update_wins(self, wins: int) -> None:
        self.wins += wins

    def update_losses(self, losses: int) -> None:
        self.losses += losses

    def get_rank_info(self) -> dict:
        return {"Name": self.name,
                "Card_id": self.card_id,
                "Interfaces": ["Card", "Combatable", "Rankable"],
                "Rating": self.rating,
                "Record": f"{self.wins}-{self.losses}"
                }
