from ex0.Card import Card


class ArtifactCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 durability: int, effect: str):
        super().__init__(name, cost, rarity)
        self.durability = durability
        self.effect = effect

    def get_card_info(self):
        infos: dict = super().get_card_info()
        infos.update({'card_played': self.name,
                      'mana_used': self.cost,
                      'effect': self.effect,
                      'type': 'artifacts'
                      })
        return infos

    def play(self, game_state: dict) -> dict:
        pass

    def activate_ability(self) -> dict:
        pass
