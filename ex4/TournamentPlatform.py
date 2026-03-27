from ex4.TournamentCard import TournamentCard


class TournamentPlatform:
    def __init__(self):
        self.cards = []
        self.matchs = 0

    def register_card(self, card: TournamentCard) -> str:
        if not isinstance(card, TournamentCard):
            raise ValueError("(Tournament) Unknown Type")
        self.cards.append(card)
        rank = card.get_rank_info()
        return (f"{rank['Name']} (ID: {rank['Card_id']}):\n"
                f"- Interfaces: {rank['Interfaces']}\n"
                f"- Rating: {rank['Rating']}\n"
                f"- Record: {rank['Record']}\n")

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        p1 = next((c for c in self.cards if c.card_id == card1_id), None)
        p2 = next((c for c in self.cards if c.card_id == card2_id), None)
        if p1 is None or p2 is None:
            raise ValueError("Player not found")
        player_1: TournamentCard = p1
        player_2: TournamentCard = p2
        player_1.attack(player_2)
        player_2.attack(player_1)
        self.matchs += 0
        winner: str
        loser: str
        winner_rating: int
        loser_rating: int
        if player_1.health >= player_2.health:
            winner = player_1.card_id
            loser = player_2.card_id
            player_1.update_wins(1)
            player_2.update_losses(1)
            winner_rating = player_1.calculate_rating()
            loser_rating = player_2.calculate_rating()
        else:
            winner = player_2.card_id
            loser = player_1.card_id
            player_2.update_wins(1)
            player_1.update_losses(1)
            winner_rating = player_2.calculate_rating()
            loser_rating = player_1.calculate_rating()
        return {'winner': winner,
                'loser': loser,
                'winner_rating': winner_rating,
                'loser_rating': loser_rating}

    def get_leaderboard(self) -> list:
        self.cards.sort(key=lambda card: card.rating, reverse=True)
        return self.cards

    def generate_tournament_report(self) -> dict:
        return {'total_cards': len(self.cards),
                'matches_played': self.matchs,
                'avg_rating': round(sum(card.rating for card in self.cards)
                                    / len(self.cards)),
                'platform_status': 'active'
                }
