from ex3.GameStrategy import GameStrategy
from ex3.CardFactory import CardFactory

class GameEngine:
    def __init__(self):
        self.factory: CardFactory = None
        self.strategy: GameStrategy = None
        self.turn: dict = {"turns_simulated": 0}

    def configure_engine(self, factory: CardFactory, strategy: GameStrategy) -> None:
        if not isinstance(factory, CardFactory):
            raise ValueError("The Factory Type is unknown")
        if not isinstance(strategy, GameStrategy):
            raise ValueError("The Strategy Type is unknown")
        self.factory = factory
        self.strategy = strategy

    def simulate_turn(self) -> dict:
        hand = self.factory.create_themed_deck(3)
        hand_on_list = []
        for cards in hand.values():
            hand_on_list.extend(cards)
        opponent_hand = [self.factory.create_creature()]
        strat = self.strategy.execute_turn(hand_on_list, opponent_hand)
        self.turn["turns_simulated"] += 1
        self.turn.update({"strategy_used": self.strategy.get_strategy_name()})
        self.turn.update({"cards_created": len(hand)})
        self.turn.update({"total_damage": strat["Damage_done"]})
        print(f"Hand: {[card.name for card in hand_on_list]}\n")
        print("Turn execution:")
        print(f"Strategy {self.turn["strategy_used"]}")
        return {
                "Cards_played": strat["Cards_played"],
                "mana_used": strat["Mana_used"],
                "targets_attacked": strat["Targets"],
                "damage_dealt": strat["Damage_done"],
                "Opponent_KO": strat["Targets_killed"],
                "Victory": strat["Game_win"]
                }

    def get_engine_status(self) -> dict:
        return self.turn