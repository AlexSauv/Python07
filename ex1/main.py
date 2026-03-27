from ex0.Card import Rarity
from ex0.CreatureCard import CreatureCard
from ex1.Deck import Deck
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
import random


def main():
    try:
        print("\n=== DataDeck Deck Builder ===\n")
        game: dict = {
            "mana": 30
            }
        deck = Deck()
        rare_type: list = random.choice(list(Rarity))
        deck.add_card(CreatureCard("Fire Dragon", 5,
                                   rare_type.value, 7, 5))
        rare_type: list = random.choice(list(Rarity))
        deck.add_card(SpellCard("Lightning Bolt", 3,
                                rare_type.value, "damage"))
        rare_type: list = random.choice(list(Rarity))
        deck.add_card(ArtifactCard("Mana Crystal", 2,
                                   rare_type.value, 3,
                                   "Permanent: +1 mana per turn"))
        deck.shuffle()
        deck_stats = deck.get_deck_stats()
        print("Building deck with different card types...")
        print(f"Deck stats: {deck_stats}\n")
        print("Drawing and playing cards:\n")
        card = deck.draw_card()
        print(f"Drew: {card.name} ({card.type})")
        print(f"Play result: {card.play(game)}\n")
        card = deck.draw_card()
        print(f"Drew: {card.name} ({card.type})")
        print(f"Play result: {card.play(game)}\n")
        card = deck.draw_card()
        print(f"Drew: {card.name} ({card.type})")
        print(f"Play result: {card.play(game)}\n")
        print("Polymorphism in action: Same interface, "
              "different card behaviors!")
    except Exception as err:
        print(f"\nGame System Error: {err}")


if __name__ == "__main__":
    main()
