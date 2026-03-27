from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex2.EliteCard import EliteCard
from ex3.GameStrategy import GameStrategy
from ex1.Deck import Deck


class AggressiveStrategy(GameStrategy):
    def __init__(self):
        self.deck = Deck()
        self.game = {"Player_side": [],
                     "opponent_health": 15,
                     "Game_win": False}

    def execute_turn(self, hand: list, battlefield: list) -> dict:
        self.game.update({"mana": 12})
        damage_done: int = 0
        spell_used = []
        target_killed = []
        if isinstance(battlefield, list):
            for target in battlefield:
                if not isinstance(target, (CreatureCard, EliteCard)):
                    raise ValueError("The battlefield is corrupted, must"
                                     " be filled with Creature and Elite type")
        if not isinstance(hand, list):
            raise ValueError("Hand must be given as a list")
        hand.sort(key=lambda card: card.cost)
        targets = self.prioritize_targets(battlefield)
        targets_attacked = self.prioritize_targets(battlefield)
        self.game.update({"opponent_side": targets})
        for card in hand:
            self.deck.add_card(card)
        for card in self.deck.cards:
            if not isinstance(card, Card):
                raise ValueError("The hand must be a card type")
            if card.is_playable(self.game["mana"]):
                if card not in self.game["Player_side"]:
                    card.play(self.game)
                    self.deck.draw_card()
                    self.game["Player_side"].append(card)
                if isinstance(card, CreatureCard):
                    if len(targets) == 0:
                        self.game["opponent_health"] -= card.attack
                    else:
                        damage_data = card.attack_target(targets[0])
                        damage_done += damage_data["damage_dealt"]
                        if targets[0].dead is True:
                            target_killed.append(targets[0].name)
                            targets.pop(0)
                elif isinstance(card, EliteCard):
                    if len(targets) == 0:
                        self.game["opponent_health"] -= card.damage
                    else:
                        damage_data = card.attack(targets[0])
                        damage_done += damage_data["damage"]
                        if targets[0].dead is True:
                            target_killed.append(targets[0].name)
                            targets.pop(0)
                elif isinstance(card, SpellCard):
                    if len(targets) == 0:
                        if card.effect_type == "damage":
                            self.game["opponent_health"] -= 3
                    else:
                        damage_data = card.resolve_effect(targets)
                        damage_done += damage_data["damage"]
                        for target in targets:
                            if target.dead is True:
                                target_killed.append(target.name)
                                targets.remove(target)
                elif isinstance(card, ArtifactCard):
                    card.activate_ability()
                else:
                    raise ValueError("This type of card is not playable.")
        mana_used: int = 12 - self.game["mana"]
        if len(target_killed) == 0:
            target_killed.append("No enemy died.")
        if self.game["opponent_health"] <= 0:
            self.game["Game_win"] = True
        return {"Strategy": self.get_strategy_name(),
                "Cards_played": [card.name for card
                                 in self.game["Player_side"]] + spell_used,
                "Targets": [target.name for target in targets_attacked],
                "Mana_used": mana_used,
                "Damage_done": damage_done,
                "Targets_killed": target_killed,
                "Game_win": self.game["Game_win"]
                }

    def get_strategy_name(self) -> str:
        return "AgressiveStrategy"

    def prioritize_targets(self, available_targets: list) -> list:
        available_targets.sort(key=lambda card: card.health)
        return available_targets
