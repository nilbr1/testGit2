"""Two-player tic-tac-toe for the terminal."""

WINNING_LINES = (
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6),
)


def new_board() -> list[str]:
    return [" "] * 9


def render(board: list[str]) -> str:
    cells = [cell if cell != " " else str(i + 1) for i, cell in enumerate(board)]
    rows = [
        f" {cells[0]} | {cells[1]} | {cells[2]} ",
        "---+---+---",
        f" {cells[3]} | {cells[4]} | {cells[5]} ",
        "---+---+---",
        f" {cells[6]} | {cells[7]} | {cells[8]} ",
    ]
    return "\n".join(rows)


def winner(board: list[str]) -> str | None:
    for a, b, c in WINNING_LINES:
        if board[a] != " " and board[a] == board[b] == board[c]:
            return board[a]
    return None


def is_full(board: list[str]) -> bool:
    return all(cell != " " for cell in board)


def prompt_move(board: list[str], player: str) -> int:
    while True:
        raw = input(f"Player {player}, choose a square (1-9): ").strip()
        if not raw.isdigit():
            print("Please enter a number from 1 to 9.")
            continue
        choice = int(raw)
        if choice < 1 or choice > 9:
            print("Please enter a number from 1 to 9.")
            continue
        index = choice - 1
        if board[index] != " ":
            print("That square is already taken.")
            continue
        return index


def play_round() -> None:
    board = new_board()
    player = "X"
    print("\nSquares are numbered 1-9. X goes first.\n")

    while True:
        print(render(board))
        print()
        board[prompt_move(board, player)] = player

        won_by = winner(board)
        if won_by:
            print(render(board))
            print(f"\nPlayer {won_by} wins!")
            return
        if is_full(board):
            print(render(board))
            print("\nIt's a draw.")
            return

        player = "O" if player == "X" else "X"


def ask_play_again() -> bool:
    while True:
        answer = input("Play again? (y/n): ").strip().lower()
        if answer in {"y", "yes"}:
            return True
        if answer in {"n", "no"}:
            return False
        print("Please answer y or n.")


def main() -> None:
    print("Tic-Tac-Toe")
    while True:
        play_round()
        if not ask_play_again():
            print("Thanks for playing.")
            return


if __name__ == "__main__":
    main()
