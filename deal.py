from deal_helpers import DealResult, get_deal_result
from hand import Hand


# プレイヤーのターン
player = Hand()
player.hit()
# player.final()
player.show_hand()
print(f"あなたのスコア    : {player.score}点")

# ディーラーのターン
dealer = Hand()
dealer.final()
dealer.show_hand()
print(f"ディーラーのスコア: {dealer.score}点")

result = get_deal_result(player.score, dealer.score)

print()
if result == DealResult.win:
    print("プレイヤーの勝ち")
elif result == DealResult.draw:
    print("引き分け")
else:
    print("プレイヤーの負け")
