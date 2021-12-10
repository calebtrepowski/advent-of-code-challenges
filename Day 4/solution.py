GRID_SIZE: int = 5


class Board:
    def __init__(self, lines: list[str]):
        self.grid = self._generate_grid(lines)
        self.won = False

    def _generate_grid(self, lines: str) -> list[list[int]]:
        grid = []
        for i in lines:
            grid.append(i.rstrip().split())
        return grid

    def __str__(self) -> str:
        ret: str = "-------------- Board --------------\n"
        ret += repr(self)
        ret += "\n-----------------------------------\n"
        return ret

    def __repr__(self) -> str:
        ret = '\n'.join(
            ['\t'.join([str(cell) for cell in row])
             for row in self.grid])
        return ret

    def mark_number(self, n: int) -> None:
        for i, v in enumerate(self.grid):
            for j, w in enumerate(v):
                if w == n:
                    self.grid[i][j] = "X"
                    return

    def check_victory(self) -> bool:
        return self._check_rows() or self._check_columns()

    def _check_rows(self) -> bool:
        """Returns True if a row is full of Xs,
        returns False if no row is full of Xs"""
        X_qtty: int = 0
        for row in self.grid:
            X_qtty = 0
            for cell in row:
                if cell != "X":
                    break
                X_qtty += 1
            if X_qtty == GRID_SIZE:
                return True
        return False

    def _check_columns(self) -> bool:
        """Returns True if a column is full of Xs,
        returns False if no column is full of Xs"""
        X_qtty: int = 0

        for i in range(0, GRID_SIZE):
            X_qtty: int = 0
            for j in range(0, GRID_SIZE):
                if self.grid[j][i] != "X":
                    break
                X_qtty += 1
            if X_qtty == GRID_SIZE:
                return True
        return False

    def sum_not_marked(self) -> int:
        sum: int = 0
        for row in self.grid:
            for cell in row:
                if cell == "X":
                    continue
                sum += int(cell)

        return sum


def load_numbers_and_boards(filename: str) -> tuple[list[str],
                                                    list[Board]]:
    # tuple[0] -> numbers to call
    # tuple[1] -> boards
    with open(filename) as f:
        numbers: list[str] = f.readline().rstrip().split(",")

        boards: list[Board] = []
        stop: bool = False
        while not stop:
            board_lines: list[str] = []
            f.readline()
            for i in range(GRID_SIZE):
                line = f.readline()
                if line == "":
                    stop = True
                    break
                board_lines.append(line)
            if len(board_lines) >= GRID_SIZE:
                boards.append(Board(board_lines))
        return numbers, boards


def get_first_winner_board_score(
        numbers: list[str],
        boards: list[Board]) -> int:
    """ Only Part One Solution """
    stop: bool = False
    winner_board: Board = None
    last_number_marked: int = None
    for i, n in enumerate(numbers):
        for b in boards:
            b.mark_number(n)

            if i < 4:
                continue

            if b.check_victory():
                stop = True
                winner_board = b
                last_number_marked = int(n)
                break
        if stop:
            break

    return winner_board.sum_not_marked()*last_number_marked


def get_first_and_last_winner_score(
        numbers: list[str],
        boards: list[Board]) -> tuple[int]:
    """ Part One and Two Solution together """
    # tuple[0] -> first_winner_score
    # tuple[1] -> last_winner_score
    first_winner_score: int = None

    last_winner_score: int = None
    lw_last_number_marked: int = None

    boards_to_delete_indexes: list[int] = []

    stop: bool = False
    for i, n in enumerate(numbers):
        print(f"number to mark = {n}")
        for j, b in enumerate(boards):
            b.mark_number(n)

            if i < 4:
                # there can't be winners with less than 5
                # numbers and checking victory is very consuming
                continue

            if first_winner_score is None:
                if b.check_victory():
                    first_winner_score = b.sum_not_marked()*int(n)
                    boards_to_delete_indexes.append(j)
                    # b.won = True
                continue
            if last_winner_score is None:
                if len(boards) > 1 and b.check_victory():
                    boards_to_delete_indexes.append(j)
                    continue
                if b.check_victory():
                    stop = True
                    lw_last_number_marked = int(n)
                    break

        if first_winner_score is not None and len(
                boards_to_delete_indexes) > 0:
            for k in reversed(boards_to_delete_indexes):
                boards.pop(k)
            boards_to_delete_indexes.clear()
        if stop:
            break
    last_winner_score = boards[0].sum_not_marked(
    )*lw_last_number_marked

    return first_winner_score, last_winner_score


def main():
    # numbers, boards = load_numbers_and_boards(
    #     "sample_puzzle.txt")
    numbers, boards = load_numbers_and_boards(
        "input_puzzle.txt")
    first_winner_score, last_winner_score = get_first_and_last_winner_score(
        numbers, boards)
    print(f"{first_winner_score = }")
    print(f"{last_winner_score = }")


main()
