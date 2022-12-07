import os

from deal_helpers import DealResult, get_deal_result
from get_aa import get_art
from hand import Hand


# 手札とスコアを表示する
def show_hand_and_score(hand, name):
    hand.show_hand()
    print(f'{name}のスコア: {hand.score}')


if __name__ == '__main__':
    dealer = Hand()

    # プレイヤーのターン
    player = Hand()

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        show_hand_and_score(dealer, 'ディーラー')
        show_hand_and_score(player, 'プレイヤー')
        if input('Hit? (y/n)') == 'y':
            player.hit()

            # バーストしたら負け
            if player.score > 21:
                player.show_hand()
                print(get_art('lose.txt'))
                print('バーストしました。負けです。')
                print(f'あなたのスコア: {player.score}')
                exit()
        else:
            break

    os.system('cls' if os.name == 'nt' else 'clear')
    show_hand_and_score(player, 'プレイヤー')

    # ディーラーのターン
    dealer.final()
    show_hand_and_score(dealer, 'ディーラー')

    result = get_deal_result(player.score, dealer.score)

    print()
    if result == DealResult.win:
        print(get_art('win.txt'))
        print("プレイヤーの勝ち")
    elif result == DealResult.draw:
        print(get_art('draw.txt'))
        print("引き分け")
    else:
        print(get_art('lose.txt'))
        print("プレイヤーの負け")
