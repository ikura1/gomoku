# -*- coding: utf-8 -*-

def get_lines(pos, angle):
    spos = pos % angle
    # spos = angle if spos < angle else spos
    line = [spos + i * angle for i in range(3)]
    if max(line) > 8:
        return []
    return line


def get_win_pattern(pos):
    """
    指定番号での勝利パターンを返す
    :param pos:
    :return:
    """
    patterns = [
        0, 1, 2,
        3, 4, 5,
        6, 7, 8,
        0, 3, 6,
        1, 4, 7,
        2, 5, 8,
        0, 4, 8,
        2, 4, 6
    ]
    # TODO: ななめの判定が難しい
    # 5目とか違い盤面が狭いため、ななめでは値の振れ幅が小さく誤動作する。
    # 5目も動いているか怪しい
    # angles = [2, 3, 4]
    angles = [3]
    spos = pos // 3 * 3
    patterns = [[spos + i for i in range(3)]]
    for angle in angles:
        pattern = get_lines(pos, angle)
        if pattern:
            patterns.append(pattern)
    return patterns

def get_all_win_pattern():
    """
    3*3の全ての勝利パターンを返す
    :return:
    """
    # TODO: 0-8の勝利判定用に作成中
    len_line = 9
    pattern = []

    for pos in range(len_line):
        pattern.extend(get_win_pattern(pos))
    return pattern


def is_end(game_bord):
    """
    ゲームが終了したのかの判定
    :param game_bord:
    :return:
    """
    win_pattern = [
        [[0, 0], [0, 1], [0, 2]],
        [[1, 0], [1, 1], [1, 2]],
        [[2, 0], [2, 1], [2, 2]],
        [[0, 0], [1, 0], [2, 0]],
        [[0, 1], [1, 1], [2, 1]],
        [[0, 2], [1, 2], [2, 2]],
        [[0, 0], [1, 1], [2, 2]],
        [[0, 2], [1, 1], [2, 0]]
    ]
    for a, b, c in win_pattern:
        sum_ = game_bord[a[0]][a[1]]
        sum_ += game_bord[b[0]][b[1]]
        sum_ += game_bord[c[0]][c[1]]
        if abs(sum_) == 3:
            return True
    return False


def is_draw(game_bord):
    """
    全てのマスの絶対値の合計が9の場合
    引き分けと判断する
    :param game_bord: ゲーム盤
    :return:
    """
    sum_ = 0
    for i in game_bord:
        for j in i:
            sum_ += abs(j)
    return sum_ == 9


def main():
    bord = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]

    player = 1
    while True:
        view_player = player if player == 1 else 2
        index = input(f'P{view_player}>')
        # 以下の方法で文字列の埋め込みが可能である
        # f'P{player}>'
        # 'P{player}>'.format(player=player)
        # 'P%s>' % player

        # x, y = [1, 2]
        # x = 1, y = 2が入力される
        x, y = [int(i) - 1 for i in index.split(',')]
        if bord[x][y] != 0:
            # 0以外が入っている場合、上に戻る
            print('Already occupied.')
            continue
        bord[x][y] = player
        # print(bord)
        if is_end(bord):
            print(f'P{view_player}', 'win')
            break
        if is_draw(bord):
            print('DRAW')
            break
        # player交代
        player = -player


if __name__ == '__main__':
    # main()
    hoge = []
    # print(hoge)
    for p in get_all_win_pattern():
        if p not in hoge:
            hoge.append(p)
    print(hoge)

