from ex0.Card import Card
from ex2.Combatable import Combatable
from Rankable import Rankable
import random

class TournamentCard(Card, Combatable, Rankable):
    def __init__(self, name: str, cost: int, rarity: str, attack: int, health: int):
        super().__init__(name, cost, rarity)
        self.damage = attack
        self.health = health
        self.sheild = random.randint(1,4)
        self.wins = 0
        self.losses = 0
        self.rating = 1200
        self.alive = True

    def play(self, game_state: dict) -> dict:
        if game_state['mana'] < self.cost:
            raise ValueError("Not enough mana")
        game_state["mana"] -= self.cost
        return {"card_played": self.name,
                "mana_used": self.cost,
                }

    def attack(self, target):
        if not isinstance(target, TournamentCard):
            raise ValueError("The opponent must be the same type. (TournamenCard)")
        res = target.defend(self.damage)
        return {"Attacker": self.name,
                "Target": target.name,
                "Total_damage": self.damage,
                "Opponent_KO": res["Alive"]
                }

    def defend(self, incoming_damage):
        damage_received = incoming_damage - self.sheild
        if damage_received < 0:
            damage_received = 0
        self.health -= damage_received
        if self.health <= 0:
            self.health = 0
            self.alive = False
        return {"Total_damage": damage_received,
                "Health": self.health,
                "Alive": self.alive
                }
    
    def get_combat_stats(self):
        return super().get_combat_stats()

    def calculate_rating(self):
        
    
    def get_tournament_stats(self) -> dict:
        return {""}