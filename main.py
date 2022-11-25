import os
import random
from pathlib import Path

from player import Player

suits = ['♠', '♣', '♥', '♦']
ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

ART_DIR = Path(__file__).absolute().parent / "ascii_art"
pause_message = "(何かキーを押してください)\n"


def get_ascii_art(file_name):
    os.system('clear')
    with Path.open(ART_DIR / file_name, "r", encoding="utf-8") as f:
        return f.read()


def hand_of_cards():
    for _ in range(2):
        dealer.hand.append(deck.pop())
        player.hand.append(deck.pop())


def display_hand(show_deler_hand=False):
    dealer.display_hand(show_deler_hand)
    player.display_hand()


if __name__ == '__main__':
    print(get_ascii_art("title.txt"))
    input(pause_message)

    dealer = Player(is_dealer=True)
    player = Player()

    is_play = True
    while is_play:
        Player.game_count += 1

        deck = [(suit, rank) for suit in suits for rank in ranks]
        random.shuffle(deck)

        hand_of_cards()
        display_hand()

        # 最初の手札の確認
        if player.score == 21 and dealer.score == 21:
            print(get_ascii_art("draw.txt"))
        elif player.score == 21:
            print(get_ascii_art("blackjack.txt"))
            player.win_count += 1
        elif dealer.score == 21:
            print(get_ascii_art("lose.txt"))
            dealer.win_count += 1
        else:
            # プレイヤーのターン
            while input('\nもう一枚カードを引きますか？ [y]\n').lower() == 'y':
                os.system('clear')
                player.hand.append(deck.pop())
                display_hand()
                if player.score > 21:
                    break

            if player.score > 21 or player.score < dealer.score:
                print(get_ascii_art("lose.txt"))
                dealer.win_count += 1
            else:
                # ディーラーのターン
                while dealer.score < player.score:
                    os.system('clear')
                    print("ディーラーのターンです")
                    dealer.hand.append(deck.pop())
                    display_hand()
                    input(pause_message)

                # 手札を開示して勝負
                if player.score == dealer.score:
                    print(get_ascii_art("draw.txt"))
                elif dealer.score > 21 or player.score > dealer.score:
                    print(get_ascii_art("win.txt"))
                    player.win_count += 1
                else:
                    print(get_ascii_art("lose.txt"))
                    dealer.win_count += 1

        display_hand(show_deler_hand=True)

        is_play = input('\nもう一度勝負しますか？ [y]\n').lower() == 'y'
        if is_play:
            os.system('clear')
            dealer.replay()
            player.replay()

    draw = Player.game_count - player.win_count - dealer.win_count
    print(f'{player.win_count} 勝 : {dealer.win_count} 敗 : {draw}分け')
