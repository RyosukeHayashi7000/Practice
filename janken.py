"""
じゃんけんゲーム。三回勝負で最後に勝敗表が表示される。
"""

import random

judge_list = [0, 0, 0]


class Hand:
    """
    PlayerとComputerのクラス。
    """
    def __init__(self, name='コンピューター'):
        self.name = name
        self.janken_list = ['グー', 'チョキ', 'パー']

    def player_hand(self):
        """
        Playerの出し手を決める関数。
        input関数で受けた数字で出し手をコメントに出力。リスト内の該当数字以外の文字が入力されると、再入力を求めるコメントを出す。
        数字は全角数字でも入力可。
        """

        while True:
            try:
                player_num = int(input('0:グー、1:チョキ、2:パー、数字を入力してください '))
                self.player_hand = self.janken_list[int(player_num)]
            except:
                print('正しい値を入力してください。')
            else:
                print(self.name, 'さんの手は', self.player_hand, 'です。', sep='')
                return self.player_hand

    def computer_hand(self):
        """
        Computerの出し手を決める関数。
        0から2のrandom関数で受けた数字で出し手を決めコメントに出力。
        """
        computer = random.randint(0, 2)
        self.computer_hand = self.janken_list[int(computer)]
        print(self.name, 'の手は', self.computer_hand, 'です。', sep='')
        return self.computer_hand


def judge(name, player_hand, computer_hand):
    """
    playerの出し手とコンピューターの出し手を比較して勝敗を決め、結果をコメントに出力。
    結果は勝敗表のリストjudge_listに追加される。

    :param name: input_name関数から受ける値
    :param player_hand: player_hand関数から受ける値
    :param computer_hand: computer_hand関数から受ける値
    """

    if (player_hand == 'グー' and computer_hand == 'チョキ') or (player_hand == 'パー' and computer_hand == 'グー') \
            or (player_hand == 'チョキ' and computer_hand == 'パー'):
        print(name, 'さんの勝ち', sep='')
        judge_list[0] += 1
    elif player_hand == computer_hand:
        print('引き分け')
        judge_list[2] += 1
    else:
        print(name, 'さんの負け', sep='')
        judge_list[1] += 1


def input_name():
    """
    名前の入力を求める関数。
    空白の場合は「名無しさん」として出力する。
    """

    name = input('名前を入力してください ')
    if name == '':
        name = '名無しさん'
    print(name, 'さんこんにちは。じゃんけんゲームを始めます。', sep='')
    return name


def judge_count():
    """
    judge_list内の勝敗表結果をコメントに出力する。
    """

    print(str(judge_list[0]) + '勝:' + str(judge_list[1]) + '敗:' + str(judge_list[2]) + '引き分け', sep='')


def main():
    """
    mainの関数。

    judge関数に以下の引数をあてる。
    player_name: はじめに求めた名前。
    player_time.player_hand(): playerをインスタンス化し、player_hand関数で出し手を決める。
    computer_time.computer_hand(): computerをインスタンス化し、computer_hand関数で出し手を決める。

    3回勝負なので、judge_list内の合計が3になった時に終了する。
    judge_count関数で最後に勝敗表を表示。
    """
    player_name = input_name()
    while True:
        player_time = Hand(name=player_name)
        computer_time = Hand()
        judge(player_name, player_time.player_hand(), computer_time.computer_hand())
        if sum(judge_list) == 3:
            break
    judge_count()


if __name__ == '__main__':
    main()
