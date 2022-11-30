class Player:
    game_count = 0

    def __init__(self, is_dealer=False):
        self.is_dealer = is_dealer
        self.hand = []
        self.hand_score = 0
        self.win_count = 0

    @property
    def score(self):
        self.hand_score = 0
        ace_count = 0
        for card in self.hand:
            if card[1] == 'A':
                ace_count += 1
                self.hand_score += 1
            elif card[1] in 'JQK':
                self.hand_score += 10
            else:
                self.hand_score += int(card[1])

        for ace in range(ace_count):
            if self.hand_score + 10 <= 21:
                self.hand_score += 10

        return self.hand_score

    def replay(self):
        """もう一回勝負するときにリセット"""
        self.hand = []
        self.hand_score = 0

    def display_hand(self, show_dealer_hand=False):
        """手札を表示"""

        rows = ['', '', '', '', '']

        def front_side():
            rows[1] += f'|{rank.ljust(2)} | '
            rows[2] += f'| {suit} | '
            rows[3] += f'|_{rank.rjust(2, "_")}| '

        def back_side():
            rows[1] += '|## | '
            rows[2] += '|###| '
            rows[3] += '|_##| '

        back_flag = False  # ディーラーのときは決着するまで2枚目以降のカードは裏面を表示
        for suit, rank in self.hand:
            rows[0] += ' ___  '
            if not self.is_dealer or (self.is_dealer and show_dealer_hand):
                front_side()
            else:
                if not back_flag:
                    front_side()
                    back_flag = True
                else:
                    back_side()

        # 手札の得点を表示
        if self.is_dealer:
            print(f"DEALER: {self.score if show_dealer_hand else '???'}")
        else:
            print(f"YOU: {self.score}")

        for row in rows:
            print(row)
