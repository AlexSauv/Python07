from ex0.Card import Card


class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, effect_type: str):
       super().__init__(name, cost, rarity)
       valid_types = ["damage", "heal", "buff", "debuff"]
       if effect_type not in valid_types:
          raise ValueError("Unknown effect type")
       self.effect_type = effect_type
       self.effect = ""
       self.type = "Spell"

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
        if self.effect_type == "damage":
            self.effect = "Deal 3 damage to target"
        elif self.effect_type == "heal":
            self.effect = "Health buff +3"
        elif self.effect_type == "buff":
            self.effect = "Attack Debuff +2"
        elif self.effect_type == "debuff":
            self.effect = "Attack Debuff -2"
        else:
           raise ValueError("The effect type is unknown")
        return {"card_played": self.name,
                "mana_used": self.cost,
                "effect": self.effect
                }

    def resolve_effect(self, targets: list) -> dict:
        effect: str = None
        if self.effect_type == "damage":
          effect = "Deal 3 damage to target"
          for target in targets:
             target.health -= 3
        elif self.effect_type == "heal":
          effect = "Health Debuff +3"
          for target in targets:
             target.health += 3
        elif self.effect_type == "buff":
          effect = "Attack Debuff +2"
          for target in targets:
             target.attack += 2
        elif self.effect_type == "debuff":
          effect = "Attack Debuff -2"
          for target in targets:
             target.attack -= 2
        else:
          raise ValueError("Unknown type effect")
        return {"card_played": self.name,
                "targets": [target.name for target in targets],
                "Effect": effect
                }