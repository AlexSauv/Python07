from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy


def main():
    print("\n=== DataDeck Game Engine ===\n")
    print("Configuring Fantasy Card Game...")
    print("Factory: FantasyCardFactory")
    fantasy = FantasyCardFactory()
    strategy = AggressiveStrategy()
    print(f"Strategy: {strategy.get_strategy_name()}")
    stats = fantasy.get_supported_types()
    print(f"Available Types: {stats}")
    print("\nSimulating aggressive turn...")
    print("Hand: ")

if __name__ == "__main__":
    main()