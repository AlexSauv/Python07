from ex0.Card import Card


class ArtifactCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 durability: int, effect: str):
        super().__init__(name, cost, rarity)
        self.durability = durability
        self.effect = effect
        self.type = "artifact"

    def get_card_info(self):
        infos: dict = super().get_card_info()
        infos.update({'card_played': self.name,
                      'mana_used': self.cost,
                      'effect': self.effect,
                      'type': self.type
                      })
        return infos

    def play(self, game_state: dict) -> dict:
       if game_state['mana'] < self.cost:
          raise ValueError("Not enough mana")
       game_state['mana'] -= self.cost
       return {"card_played": self.name,
               "mana_used": self.cost,
               "effect": self.effect
               }

    def activate_ability(self) -> dict:
        if self.durability <= 0:
            raise ValueError("The artifact doesn't exist anymore.")
        self.durability -= 1
        return {"artifact": self.name,
                "effect": self.effect,
                "durability_left": self.durability
                }
