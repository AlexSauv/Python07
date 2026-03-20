from ex0.Card import Card


class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, effect_type: str):
       super().__init__(name, cost, rarity)
       if effect_type is not "damage" "heal" "buff" "debuff":
          raise ValueError("Unknown effect type")
       self.effect_type = effect_type

    def get_card_info(self):
        infos: dict = super().get_card_info()
        infos.update({"effect_type": self.effect_type,
                      "type": "spell"
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
       
       