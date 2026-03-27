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
        if not self.cards:
            raise ValueError("The Deck is empty")
        return self.cards.pop(0)

    def get_deck_stats(self) -> dict:
        total: int = len(self.cards)
        creature: int = sum(1 for crd in self.cards if crd.type == "Creature")
        spells: int = sum(1 for crd in self.cards if crd.type == "Spell")
        artifact: int = sum(1 for crd in self.cards if crd.type == "Artifact")
        if total != 0:
            avg_cost = round(sum(card.cost for card in self.cards) / total, 1)
        else:
            avg_cost = 0
        return {"total_cards": total,
                "creatures": creature,
                "spells": spells,
                "artifacts": artifact,
                "avg_cost": avg_cost
                }
