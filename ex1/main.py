from ex0.CreatureCard import CreatureCard
from ex1.Deck import Deck
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard

def main():
    try:
        print("\n=== DataDeck Deck Builder ===\n")
        game: dict = {
            "board": [],
            "mana": 30
            }
        deck = Deck()
        deck.add_card(CreatureCard("Fire Dragon", 5, "Legendary", 7, 5))
        deck.add_card(SpellCard("Lightning Bolt", 3, "Commun", "damage"))
        deck.add_card(ArtifactCard("Mana Crystal", 2, "Commun", 3, "Permanent: +1 mana per turn"))
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
        print("Polymorphism in action: Same interface, different card behaviors!")    
    except Exception as err:
       print(f"Error: {err}")
       raise
if __name__ == "__main__":
    main()
