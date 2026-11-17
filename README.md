# Tic-Tac-Toe

A two-player tic-tac-toe game for the terminal. Players take turns placing **X** and **O** on a 3×3 board. The first to get three in a row (horizontally, vertically, or diagonally) wins. If the board fills with no winner, the game is a draw.

## Requirements

- Python 3.10 or later (uses `str | None` type hints)

## How to run

From the project directory:

```bash
python3 tictactoe.py
```

## How to play

1. Empty squares are labeled **1–9**:

   ```
    1 | 2 | 3
   ---+---+---
    4 | 5 | 6
   ---+---+---
    7 | 8 | 9
   ```

2. **X** always goes first.
3. On your turn, type the number of an empty square and press Enter.
4. After a win or draw, choose whether to play again (`y` / `n`).

Invalid input (non-numeric values, numbers outside 1–9, or taken squares) is rejected and you are asked again.
