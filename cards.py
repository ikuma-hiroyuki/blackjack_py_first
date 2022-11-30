from pathlib import Path

ART_DIR = Path(__file__).absolute().parent / "ascii_art"

with Path.open(ART_DIR / 'card_head.txt', "r", encoding="utf-8") as f:
    card_open = f.read()

with Path.open(ART_DIR / 'card_tail.txt', "r", encoding="utf-8") as f:
    card_close = f.read()


class Card:
    def __init__(self, suit, rank, param):
        self.suit = suit
        self.rank = rank
        self.score = param['score']
        self.is_ace = param['is_ace']

    def get_card_image(self, show_head=True):
        if show_head:
            return card_open.format(self.rank.ljust(2, " "), self.suit, self.rank.rjust(2, "_"))
        else:
            return card_close

    def show_card(self, show_head=True, show_score=False):
        result = self.get_card_image(show_head)
        if show_score:
            score = f'{self.score}' if not self.is_ace else f'{self.score} or {self.score - 10}'
            result += f' {score}'
        print(result)

    def __str__(self):
        return f'{self.suit.rjust(2, " ")}{self.rank.rjust(3, " ")}: {str(self.score).rjust(2, " ")}点'


def create_card_list() -> list[Card]:
    card_list = []
    suits = ['♠', '♣', '♥', '♦']
    rank_dict = {
        'A': {'score': 11, 'is_ace': True},
        '2': {'score': 2, 'is_ace': False},
        '3': {'score': 3, 'is_ace': False},
        '4': {'score': 4, 'is_ace': False},
        '5': {'score': 5, 'is_ace': False},
        '6': {'score': 6, 'is_ace': False},
        '7': {'score': 7, 'is_ace': False},
        '8': {'score': 8, 'is_ace': False},
        '9': {'score': 9, 'is_ace': False},
        '10': {'score': 10, 'is_ace': False},
        'J': {'score': 10, 'is_ace': False},
        'Q': {'score': 10, 'is_ace': False},
        'K': {'score': 10, 'is_ace': False},
    }
    for suit in suits:
        for rank, param in rank_dict.items():
            card_list.append(Card(suit, rank, param))
    return card_list


def show_all_cards(card_list):
    """複数のカードを横に羅列する"""

    line1_list = []
    line2_list = []
    line3_list = []
    line4_list = []

    for card in card_list:
        line1, line2, line3, line4 = card.get_card_image().splitlines()
        line1_list.append(line1.ljust(5, " "))
        line2_list.append(line1.ljust(5, " "))
        line3_list.append(line1.ljust(5, " "))
        line4_list.append(line1.ljust(5, " "))

    print("  ".join(line1_list))
    print("  ".join(line2_list))
    print("  ".join(line3_list))
    print("  ".join(line4_list))


if __name__ == "__main__":
    for card in create_card_list():
        card.show_card(show_head=True, show_score=True)
        print(card)
