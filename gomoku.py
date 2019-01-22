import numpy as np


class Gomoku:
    """
    Gomoku Zeroしたい
    """
    def __init__(self):
        # 盤の初期化
        self.current_player = 1
        self.stats = GomokuStats(np.zeros(81, dtype=np.int),
                                 self.current_player)
        self.history_dict = {1: [],
                             2: []}


    def reset(self):
        """
        ゲームをリセットします
        :return:
        """
        self.current_player = 1
        self.stats = GomokuStats(np.zeros(81, dtype=np.int),
                                 self.current_player)

    def turn(self, position):
        """
        TODO: 場外のqエラー対応 (99, -1など)
        TODO: 既にコマがある場合対応
        :param position:
        :return:
        """
        self.stats, done = self.stats.take_action(position)
        self.current_player = -self.current_player
        return done

    def run(self):
        """
        ゲームの開始
        """
        player_input_text = '{c_player}(例: 1): '
        self.stats.render()
        while True:
            position = input(player_input_text.format(c_player=self.current_player))
            done = self.turn(int(position))
            self.stats.render()
            if done:
                print('WINNER: {0}'.format(-self.current_player))
                break


class GomokuStats:
    """
    ゲームの状況
    """
    def __init__(self, board, player, position=0):
        self.board = board
        self.player = player
        self.is_end = self._check_end_game(position)

    def _check_end_game(self, position):
        """
        ゲームが終了したか確認します
        :param position: 置いた駒の位置
        :return: ゲームが終了したかどうか
        """
        win_patterns = self._create_win_patterns(position)
        for pattern in win_patterns:
            if sum(self.board[pattern]) == 5 * -self.player:
                return 1
        return 0

    def _create_win_patterns(self, position):
        """
        置いた駒を含む勝利パターンを返します
        :param position: 置いた駒の位置
        :return: 勝利パターンのリスト
        """
        sposition = position // 9 * 9
        lines = [[sposition + i for i in range(9)]]
        angles = [8, 9, 10]
        lines.extend([self._get_line_numbers(position, angle)
                      for angle in angles])
        patterns = [line[i: i + 5]
                    for line in lines
                    for i in range(len(line))
                    if i < 5]
        return filter(lambda x: position in x, patterns)

    def _get_line_numbers(self, position, angle):
        """
        指定したラインの数字リストを返します
        :param position: 取得するラインの起点
        :param angle: 取得するラインの方向
        :return: ラインの数字リスト
        """
        i = position % angle
        numbers = []
        while i < len(self.board):
            numbers.append(i)
            i += angle
        return numbers

    def take_action(self, position):
        """
        ターンのアクション
        :param position: 駒を置いた位置
        :return: 次の盤面、ゲームが終了したか
        """
        new_board = np.array(self.board)
        new_board[position] = self.player
        new_stats = GomokuStats(new_board, -self.player, position)
        done = new_stats.is_end
        return new_stats, done

    def render(self):
        """
        ゲーム盤を表示します
        """
        # print(self.board)
        # return
        print('-' * 46)
        for i in range(9):
            row = self.board[i * 9: (i + 1) * 9]
            print('|', end=' ')
            for col in row:
                print('{0:02d}'.format(col), '| ', end='')
                # print('|', end='')
            print('')
            print('-' * 46)


if __name__ == '__main__':
    test = Gomoku()
    test.run()