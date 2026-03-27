from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform
import random


def main():
    try:
        print("\n=== DataDeck Tournament Platform ===\n")
        dragon = TournamentCard("Fire Dragon", 6, "Legendary",
                                random.randint(3, 7),
                                random.randint(6, 10), "dragon_001")
        wizard = TournamentCard("Ice Wizard", 6, "Rare",
                                random.randint(3, 7),
                                random.randint(6, 9), "wizard_001")
        tournament = TournamentPlatform()
        print("Registering Tournament Cards...\n")
        print(tournament.register_card(dragon))
        print(tournament.register_card(wizard))
        dragon.get_rank_info()
        wizard.get_rank_info()
        print("Creating tournament match...")
        result = tournament.create_match("dragon_001", "wizard_001")
        print(f"Match result: {result}\n")
        print("Tournament Leaderboard:")
        leadeboard = tournament.get_leaderboard()
        i = 1
        for rank in leadeboard:
            print(f"{i}. {rank.name} - Rating: {rank.rating} "
                  f"({rank.wins}-{rank.losses})")
            i += 1
        print("\nPlatform Report:")
        print(tournament.generate_tournament_report())
        print("\n=== Tournament Platform Successfully Deployed! ===")
        print("All abstract patterns working together harmoniously!")
    except Exception as err:
        print(f"Tournament Error: {err}")


if __name__ == "__main__":
    main()
