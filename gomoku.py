# -*- coding: utf-8 -*-


class Gomoku(object):
    """
    Gomoku Zeroしたい
    """
    def __init__(self):
        # 盤の初期化
        self.ban = [[0 for _ in range(9)]
                    for _ in range(9)]
        self.history_dict = {1: [],
                             2: []}
        self.current_player = 1

    def check_renzoku(self, x, y):
        def check_renzoku_row(i):
            count = 0
            length = len(self.ban) - x if i == 1 else x + 1
            cx = x + i
            for _ in range(length):
                if self.ban[cx][y] != value:
                    break
                
            return count
        def check_renzoku_col(i):
            length = len(self.ban) - y if i == 1 else y + 1
            count = 0
            return count
        def check_renzoku_cross(i):
            x, y
            count = 0
            return count
        value = self.ban[x][y]

        for i in range():


    def do_coma(self, x, y):
        """
        駒を置く

        Parameters
        ----------
        x: int
        y: int

        Returns
        -------
        win_player: int
        """
        self.ban[x][y] = self.current_player
        self.history_dict[self.current_player].append([x, y])
        if self.judg_winner() == -1:
            self.current_player = 2 if self.current_player == 1 else 1
        return self.judg_winner()

    def check_win(self):
        """
        勝負が終ったかの判定
        Returns
        -------
        exit_flg: bool
        """
        # x, y = self.history_dict[self.current_player]
        exit_flg = False
        return exit_flg

    def judg_winner(self):
        """
        勝者は返す

        Returns
        -------

        """
        if self.check_win():
            return self.current_player
        return -1

    def view_ban(self):
        """
        盤の表示
        Returns
        -------

        """
        # print(self.ban)
        # return
        print('-' * 37)
        for row in self.ban:
            print('|', end='')
            for col in row:
                print('', col, '|', end='')
                # print('|', end='')
            print('')
            print('-' * 37)

    def run(self):
        """
        ゲームの開始
        """
        player_input_text = '{c_player}(例: 0,2): '
        while True:
            hoge = input(player_input_text.format(c_player=self.current_player))
            winner = self.do_coma(*[int(i) for i in hoge.split(',')])
            self.view_ban()
            if winner != -1:
                break

if __name__ == u'__main__':
    test = gomoku()
    test.run()