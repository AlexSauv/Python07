from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.GameEngine import GameEngine


def main():
    try:
        print("\n=== DataDeck Game Engine ===\n")
        print("Configuring Fantasy Card Game...")
        print("Factory: FantasyCardFactory")
        fantasy = FantasyCardFactory()
        strategy = AggressiveStrategy()
        print(f"Strategy: {strategy.get_strategy_name()}")
        stats = fantasy.get_supported_types()
        print(f"Available types: {list(stats.keys())}")
        print("\nSimulating aggressive turn...")
        game = GameEngine()
        game.configure_engine(FantasyCardFactory(), AggressiveStrategy())
        turn = game.simulate_turn()
        print(f"Actions: {turn}\n")
        report = game.get_engine_status()
        print("Game Report:")
        print(report)
        print("\nAbstract Factory + Strategy Pattern: Maximum flexibility achieved!")
    except ValueError as err:
        print(f"Game System Error: {err}")

if __name__ == "__main__":
    main()