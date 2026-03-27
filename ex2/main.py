from ex0.Card import Rarity
from ex0.CreatureCard import CreatureCard
from ex1.Deck import Deck
from ex2.EliteCard import EliteCard
import random


def main():
    try:
        print("\n=== DataDeck Ability System ===\n")
        rare_type: list = random.choice(list(Rarity))
        game: dict = {
            "mana": 30
            }
        deck = Deck()
        opponent_deck = Deck()
        elite_card = EliteCard("Arcane Warrior", 4, rare_type.value, 6, 6, 2)
        deck.add_card(elite_card)
        deck.draw_card()
        elite_card.play(game)
        enemy = EliteCard("Enemy", 4, rare_type.value, 5, 6, 1)
        enemy_1 = CreatureCard("Enemy1", 2, rare_type.value, 5, 6)
        enemy_2 = CreatureCard("Enemy2", 2, rare_type.value, 5, 6)
        opponent_deck.add_card(enemy)
        opponent_deck.add_card(enemy_1)
        opponent_deck.add_card(enemy_2)
        enemy.play(game)
        enemy_1.play(game)
        enemy_2.play(game)
        opponent = [card for card in opponent_deck.cards]
        opponent_deck.draw_card()
        opponent_deck.draw_card()
        opponent_deck.draw_card()
        print("EliteCard capabilities:")
        print("- Card: ['play', 'get_card_info', 'is_playable']")
        print("- ombatable: ['attack', 'defend', 'get_combat_stats']")
        print("- Magical: ['cast_spell', 'channel_mana', 'get_magic_stats']\n")
        print(f"Playing {elite_card.name} ({elite_card.type}):\n")
        print("Combat Phase:")
        print(f"Attack result: {elite_card.attack(enemy)}")
        print(f"Defense result: {elite_card.defend(enemy.damage)}")
        print("\nMagic Phase:")
        print(f"Spell cast: {elite_card.cast_spell("FireBall", opponent)}")
        print(f"Mana Channel: {elite_card.channel_mana(4)}")
        print("\nMultiple interface implementation successful!")
    except Exception as err:
        print(f"\nGame System Error: {err}")


if __name__ == "__main__":
    main()
