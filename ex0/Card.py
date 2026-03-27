from abc import ABC, abstractmethod
from enum import Enum

class Rarity(Enum):
    type_1 = "Legendary"
    type_2 = "Rare"
    type_3 = "Common"


class Card(ABC):
    def __init__(self, name: str, cost: int, rarity: str) -> None:
        self.name = name
        if cost < 0: raise ValueError("Cost must be at least 0")
        self.cost = cost
        self.rarity = rarity
        self.type = "Unknown"

    @abstractmethod
    def play(self, game_state: dict) -> dict:
        pass

    def get_card_info(self) -> dict:
        return {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity
            }

    def is_playable(self, available_mana: int) -> bool:
        if not isinstance(available_mana, int):
            raise Exception("Unvalid data format")
        if available_mana >= self.cost:
            return True
        return False
