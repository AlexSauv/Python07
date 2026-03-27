from ex0.Card import Card
from ex0.CreatureCard import CreatureCard


class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, effect_type: str):
       super().__init__(name, cost, rarity)
       valid_types = ["damage", "heal", "buff", "debuff"]
       if effect_type not in valid_types:
          raise ValueError("Spell: Unknown effect type")
       self.effect_type = effect_type
       self.effect = ""
       self.type = "Spell"
       self.active = False

    def get_card_info(self):
        infos: dict = super().get_card_info()
        infos.update({"effect_type": self.effect_type,
                      "type": self.type
                      })
        return infos

    def play(self, game_state: dict) -> dict:
        if game_state['mana'] < self.cost:
          raise ValueError("Not enough mana")
        game_state['mana'] -= self.cost
        if "player_side" not in game_state:
            game_state.update({"player_side": []})
        game_state["player_side"].append(self)
        if self.active == True:
            if self.name in game_state["player_side"]:
                game_state["player_side"].remove(self)
        if self.effect_type == "damage":
            self.effect = "Deal 3 damage to target"
        elif self.effect_type == "heal":
            self.effect = "Add +3 to the target health"
        elif self.effect_type == "buff":
            self.effect = "Add +2 to the target attacks"
        elif self.effect_type == "debuff":
            self.effect = "Minus 2 on targets attack"
        else:
           raise ValueError("The effect type is unknown")
        return {"card_played": self.name,
                "mana_used": self.cost,
                "effect": self.effect
                }

    def resolve_effect(self, targets: list) -> dict:
        from ex2.EliteCard import EliteCard
        if not isinstance(targets, list):
             raise ValueError("(Spell) Targets must be given as a list.")
        damage_done: int = 0
        for target in targets:
            if not isinstance(target, (CreatureCard, EliteCard)):
              raise ValueError("Each target must be Creature or Elite type.")
            if self.effect_type == "damage":
               target.health -= 3
               damage_done += 3
               if target.health <= 0:
                   target.health = 0
                   target.dead = True
            elif self.effect_type == "heal":
               target.health += 3
            elif self.effect_type == "buff":
               target.attack += 2
            elif self.effect_type == "debuff":
                target.attack -= 2
                if target.attack < 1:
                    target.attack = 1
            else:
                raise ValueError("Unknown type effect")
        self.active = True
        return {"card_played": self.name,
                "targets": [target.name for target in targets],
                "damage": damage_done,
                "Effect": self.effect
                }