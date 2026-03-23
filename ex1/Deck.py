from ex0.Card import Card
import random

class Deck:
    def __init__(self):
        self.cards: list[Card] = []
    
    def add_card(self, card: Card) -> None:
        if not isinstance(card, Card):
            raise ValueError("The data given is not a card")
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        for card in self.cards:
            if card_name == card.name:
                self.cards.remove(card)
                return True
        return False
    
    def shuffle(self) -> None:
        if len(self.cards) > 1:
            random.shuffle(self.cards)

    def draw_card(self) -> Card:
        pass

    def get_deck_stats(self) -> dict:
        total = len(self.cards)
        creature = len(1 for card in self.cards if card.type == "creature")
        spells = len(1 for card in self.cards if card.type == "spell")
        artifact = len(1 for card in self.cards if card.type == "artifact")
        avg_cost = sum(card.cost for card in self.cards) / total
        return {"total_cards": total,
                "creatures": creature,
                "spells": spells,
                "artifacts": artifact,
                "avg_cost": avg_cost
                }
