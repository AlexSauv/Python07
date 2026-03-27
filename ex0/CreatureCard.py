from ex0.Card import Card


class CreatureCard(Card):
    def __init__(self, name: str, cost: int,
                 rarity: str, attack: int, health: int):
        super().__init__(name, cost, rarity)
        if attack <= 0: raise ValueError("Attack damage must be positive")
        self.attack = attack
        if health < 0: raise ValueError("Health must be positive")
        self.health = health
        self.type: str = "Creature"
        self.dead: bool = False

    def play(self, game_state: dict) -> dict:
        if not isinstance(game_state, dict):
            raise ValueError("Game state must be given as a dict.")
        if game_state['mana'] < self.cost:
            raise ValueError("Not enough mana")
        game_state["mana"] -= self.cost
        if "player_side" not in game_state:
            game_state.update({"player_side": []})
        game_state.setdefault("player_side", []).append(self)
        return {"card_played": self.name,
                "mana_used": self.cost,
                "effect": "Creature summoned to battlefield"
                }

    def attack_target(self, target) -> dict:
        from ex2.EliteCard import EliteCard
        if not isinstance(target, (CreatureCard, EliteCard)):
            raise ValueError("Make sure to give a Creature Card")
        target.health -= self.attack
        if target.health < 0:
            target.health = 0
            target.dead = True
        return {'attacker': self.name,
                'target': target.name,
                'damage_dealt': self.attack,
                'combat_resolved': target.dead
                }

    def get_card_info(self) -> dict:
        infos: dict = super().get_card_info()
        infos.update({"type": self.type,
                      "attack": self.attack,
                      "health": self.health})
        return infos
