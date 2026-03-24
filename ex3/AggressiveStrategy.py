from ex3.GameStrategy import GameStrategy

class AggressiveStrategy(GameStrategy):

    def execute_turn(self, hand: list, battlefield: list) -> dict:
        mana_available = 12
        cards_played = []
        hand.sort(key=lambda card: card.cost)
        for card in hand:
            if card.is_playable(mana_available):
                mana_available -= card.cost
                cards_played.append(card.name)
        mana_used = 12 - mana_available 
        target = self.prioritize_targets(battlefield)
        return {"Strategy": self.get_strategy_name(),
                "Cards_played": cards_played,
                "Targets": target,
                "Mana_used": mana_used
                }

    def get_strategy_name(self) -> str:
        return "Agressive Strategy"

    def prioritize_targets(self, available_targets: list) -> list:
        available_targets.sort(key=lambda card: card.health)
        return available_targets