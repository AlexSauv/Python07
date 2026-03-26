#!/usr/bin/env python3
from ex0.Card import Rarity
from ex0.CreatureCard import CreatureCard
import random


def main() -> None:
    print("\n=== DataDeck Card Foundation ===\n")
    try:
        rarity: list = random.choice(list(Rarity))
        dragon = CreatureCard("Fire Dragon", 5, rarity.value, 7, 5)
        goblin = CreatureCard("Goblin Warrior", 1, "common", 3, 4)
        print("Testing Abstract Base Class Design:\n")
        print("CreatureCard Info:")
        print(dragon.get_card_info())
        game: dict = {
            "mana": 8
            }
        playable: bool = dragon.is_playable(game['mana'])
        print(f"\nPlaying {dragon.name} with {game['mana']} mana available:")
        print(f"Playable: {playable}")
        print(f"Play result: {dragon.play(game)}")
        print(f"\n{dragon.name} attacks {goblin.name}:")
        print(f"\nAttack result: {dragon.attack_target(goblin)}")
        print(f"\nTesting insufficient mana ({game['mana']} available):")
        print(f"Playable: {dragon.is_playable(game['mana'])}")
        print("\nAbstract pattern successfully demonstrated!")
    except Exception as err:
        print(f"\nGame System Error: {err}")


if __name__ == "__main__":
    main()
