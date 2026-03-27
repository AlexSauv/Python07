from ex0.Card import Card


class ArtifactCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 durability: int, effect: str):
        super().__init__(name, cost, rarity)
        if durability < 0: raise ValueError("Please make the durability is above zero")
        self.durability = durability
        self.effect = effect
        self.type = "Artifact"
        self.active = False

    def get_card_info(self):
        infos: dict = super().get_card_info()
        infos.update({'durability': self.durability,
                      'effect': self.effect,
                      'type': self.type
                      })
        return infos

    def play(self, game_state: dict) -> dict:
        if not isinstance(game_state, dict):
            raise ValueError("Game state must be given as a dict.")
        if game_state['mana'] < self.cost:
          raise ValueError("Not enough mana")
        game_state['mana'] -= self.cost
        if "player_side" not in game_state:
            game_state.update({"player_side": []})
        game_state.setdefault("player_side", []).append(self)
        return {"card_played": self.name,
               "mana_used": self.cost,
               "effect": self.effect
               }

    def activate_ability(self) -> dict:
        if self.active == False:
            self.active = True
        if self.durability == 0:
            print("The artifact doesn't exist anymore.")
        if "Permanent" not in self.effect:
            self.durability -= 1
        return {"artifact": self.name,
                "effect": self.effect,
                "durability_left": self.durability,
                "active": self.active
                }
