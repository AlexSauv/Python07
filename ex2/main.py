from ex2.EliteCard import EliteCard
from ex0.CreatureCard import CreatureCard

def main():
    print("\n=== DataDeck Ability System ===\n")
    elite_card = EliteCard("Arcane Warrior", 4, "Legendary", 5, 6, 'melee', 3)
    enemy = CreatureCard("Enemy", 2, "commun", 5, 6)
    enemy_1 = CreatureCard("Enemy1", 2, "commun", 5, 6)
    enemy_2 = CreatureCard("Enemy2", 2, "commun", 5, 6)
    opposant = [enemy_1, enemy_2]
    print("EliteCard capabilities:")
    print("- Card: ['play', 'get_card_info', 'is_playable']")
    print("- ombatable: ['attack', 'defend', 'get_combat_stats']")
    print("- Magical: ['cast_spell', 'channel_mana', 'get_magic_stats']\n")
    print(f"Playing {elite_card.name} ({elite_card.type}):\n")
    print("Combat Phase:")
    print(f"Attack result: {elite_card.attack(enemy)}")
    print(f"Defense result: {elite_card.defend(5)}")
    print("\nMagic Phase:")
    print(f"Spell cast: {elite_card.cast_spell("Fireball", opposant)}")
    print(f"Mana Channel: {elite_card.channel_mana(3)}")
    print("\nMultiple interface implementation successful!")


if __name__ == "__main__":
    main()