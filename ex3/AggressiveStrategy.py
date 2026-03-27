from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex2.EliteCard import EliteCard
from ex3.GameStrategy import GameStrategy
from ex1.Deck import Deck

class AggressiveStrategy(GameStrategy):

    def execute_turn(self, hand: list, battlefield: list) -> dict:
        if isinstance(battlefield, list):
            for target in battlefield:
                if not isinstance(target, (CreatureCard, EliteCard)):
                    raise ValueError("The battlefield is corrupted, " 
                                     "must be filled with Creature and Elite type")
        if not isinstance(hand, list):
            raise ValueError("Hand must be given as a list")
        damage_done = 0
        deck = Deck()
        game = {"Player_side": [],
                "opponent_health": 15,
                "opponent": battlefield,
                "mana": 12
                }
        spell_used = []
        win = False
        hand.sort(key=lambda card: card.cost)
        targets = self.prioritize_targets(battlefield)
        for card in hand:
            deck.add_card(card)
        for card in deck.cards:
            if not isinstance(card, Card):
                raise ValueError("The hand must be a card type")
            if card.is_playable(game["mana"]):
                if card not in game["Player_side"]:
                    card.play(game)
                    deck.draw_card()
                    game["Player_side"].append(card)
                if isinstance(card, CreatureCard):
                    if len(targets) == 0:
                        game["opponent_health"] -= card.health
                    else:
                        damage_data = card.attack_target(targets[0])
                        damage_done += damage_data["damage_dealt"]
                elif isinstance(card, EliteCard):
                    if len(targets) == 0:
                        game["opponent_health"] -= card.damage
                    else:
                        damage_data = card.attack(targets[0])
                        damage_done += damage_data["damage"]
                elif isinstance(card, SpellCard):
                    game["mana"] -= card.cost
                    if len(targets) == 0:
                        if card.effect_type == "damage":
                            game["opponent_health"] -= 3
                    else:
                        damage_data = card.resolve_effect(targets)
                        damage_done += damage_data["damage"]
                elif isinstance(card, ArtifactCard):
                    card.activate_ability()
                else:
                    raise ValueError("This type of card is not playable.")
        mana_used: int = 12 - game["mana"]
        killed = [target.name for target in targets if target.dead == True]
        if len(killed) == 0:
            killed.append("No enemy died.")
        if game["opponent_health"] <= 0:
            win = True
        return {"Strategy": self.get_strategy_name(),
                "Cards_played": [card.name for card in game["Player_side"]] + spell_used,
                "Targets": [target.name for target in targets],
                "Mana_used": mana_used,
                "Damage_done": damage_done,
                "Targets_killed": killed,
                "Game_win": win
                }

    def get_strategy_name(self) -> str:
        return "AgressiveStrategy"

    def prioritize_targets(self, available_targets: list) -> list:
        available_targets.sort(key=lambda card: card.health)
        return available_targets
    