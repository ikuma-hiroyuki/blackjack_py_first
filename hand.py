from cards import create_card_list, show_all_cards
from deal_helpers import hit, get_dealer_current_score, get_default_dealer_cards, set_dealer_final_card_list

card_list = create_card_list()


class Hand:
    """手札を管理(保持、追加、表示)するクラス"""

    def __init__(self):
        self.cards = []
        self._score = 0
        self._default()

    @property
    def score(self):
        """スコアを返す"""
        ace_count = len(list(filter(lambda x: x.is_ace, self.cards)))  # A の枚数
        return get_dealer_current_score(self._score, ace_count)

    def _default(self):
        """最初の2枚のカードを決定する"""
        self.cards = get_default_dealer_cards(card_list)

    def hit(self):
        """カードを1枚引く"""
        self.cards.append(hit(card_list))

    def final(self):
        """最終的なカードのリストとスコアを決定する"""
        self._score = self.score
        self.cards, self._score = set_dealer_final_card_list(self.cards, card_list)

    def show_hand(self):
        """手札を表示する"""
        show_all_cards(self.cards)
