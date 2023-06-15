import random

class MCTSNode:
    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent
        self.children = []
        self.wins = 0
        self.visits = 0

    def select(self, c=1):
        return max(self.children, key=lambda child: child.wins / child.visits + c * (child.parent.visits / child.visits) ** 0.5)

    def expand(self, move):
        child = MCTSNode(move, parent=self)
        self.children.append(child)
        return child

    def backpropagate(self, result):
        self.visits += 1
        self.wins += result
        if self.parent:
            self.parent.backpropagate(1 - result)


class MCTSAIStrategy:
    def __init__(self, gomoku, player='O', iterations=1000):
        self.gomoku = gomoku
        self.player = player
        self.iterations = iterations

    def get_move(self):
        root = MCTSNode(self.gomoku)

        for _ in range(self.iterations):
            node = root
            state = self.gomoku.clone()

            while node.children:
                node = node.select()
                state.make_move(*node.state, self.player)

            if not state.is_full():
                move = random.choice(state.get_legal_moves())
                child = node.expand(move)
                state.make_move(*move, self.player)

                winner = state.check_win(*move, self.player)
                if winner:
                    result = 1 if state.board[move[0]][move[1]] == self.player else 0
                else:
                    result = 0.5

                child.backpropagate(result)

        best_child = max(root.children, key=lambda child: child.visits)
        return best_child.state

class Gomoku:
    def __init__(self, size=15):
        self.size = size
        self.board = [['-' for _ in range(size)] for _ in range(size)]

    def clone(self):
        new_gomoku = Gomoku(self.size)
        new_gomoku.board = [row.copy() for row in self.board]
        return new_gomoku

    def is_full(self):
        return all(self.board[x][y] != '-' for x in range(self.size) for y in range(self.size))

    def get_legal_moves(self):
        return [(x, y) for x in range(self.size) for y in range(self.size) if self.is_valid_move(x, y)]    

    def display(self):
        for row in self.board:
            print(" ".join(row))
        print()

    def is_valid_move(self, x, y):
        return 0 <= x < self.size and 0 <= y < self.size and self.board[x][y] == '-'

    def make_move(self, x, y, player):
        if self.is_valid_move(x, y):
            self.board[x][y] = player
            return True
        return False

    def check_win(self, x, y, player):
        directions = [(1, 0), (0, 1), (1, 1), (1, -1)]
        for dx, dy in directions:
            count = 1
            for i in range(1, 5):
                nx, ny = x + i * dx, y + i * dy
                if 0 <= nx < self.size and 0 <= ny < self.size and self.board[nx][ny] == player:
                    count += 1
                else:
                    break

            for i in range(1, 5):
                nx, ny = x - i * dx, y - i * dy
                if 0 <= nx < self.size and 0 <= ny < self.size and self.board[nx][ny] == player:
                    count += 1
                else:
                    break

            if count >= 5:
                return True
        return False

    def ai_move(self,strategy):
        x, y = strategy.get_move()
        self.make_move(x, y, 'O')
        return x, y

def main():
    gomoku = Gomoku()
    ai_strategy = MCTSAIStrategy(gomoku)
    gomoku.display()

    while True:
        x, y = map(int, input("请输入你的下棋位置(用逗号分隔，如: 7,7): ").strip().split(","))
        if gomoku.make_move(x, y, 'X'):
            gomoku.display()
            if gomoku.check_win(x, y, 'X'):
                print("恭喜你赢了！")
                break
        else:
            print("无效的位置，请重新输入！")
            continue
        print("AI正在思考中...")
        x, y = gomoku.ai_move(ai_strategy)
        gomoku.display()
        if gomoku.check_win(x, y, 'O'):
            print("很遗憾，AI赢了！")
            break


if __name__ == "__main__":
    main()