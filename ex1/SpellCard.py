from ex0.Card import Card


class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, effect_type: str):
       super().__init__(name, cost, rarity)
       if not "damage" in effect_type:
          raise ValueError("Unknown effect type")
       self.effect_type = effect_type
       self.effect = ""
       self.type = "spell"

    def get_card_info(self):
        infos: dict = super().get_card_info()
        infos.update({"effect_type": self.effect_type,
                      "type": "spells"
                      })
        return infos

    def play(self, game_state: dict) -> dict:
       if game_state['mana'] < self.cost:
          raise ValueError("Not enough mana")
       game_state['mana'] -= self.cost
       return {"card_played": self.name,
               "mana_used": self.cost,
               "effect": self.effect_type
               }

    def resolve_effect(self, targets: list) -> dict:
        effect: str = None
        if self.effect_type == "damage":
          effect = "Health Debuff -3"
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