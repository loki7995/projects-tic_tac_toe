import tkinter as tk
from tkinter import font
from itertools import cycle
from typing import NamedTuple
import random


class Player(NamedTuple):
    label: str
    color: str


class Move(NamedTuple):
    row: int
    col: int
    label: str = ""


BOARD_SIZE = 3
HUMAN = Player("X", "cyan")
AI    = Player("O", "yellow")
PVP_PLAYERS = (Player("X", "cyan"), Player("O", "orange"))


class TicTacToeGame:
    def __init__(self, board_size=BOARD_SIZE):
        self.board_size = board_size
        self._current_moves = []
        self._winning_combos = []
        self._has_winner = False
        self.winner_combo = []

        # mode flags
        self.is_ai_mode = False
        self.human_player = HUMAN
        self.ai_player = AI

        # default: two-player
        self._players = cycle(PVP_PLAYERS)
        self.current_player = next(self._players)

        self._setup_board()

    def _setup_board(self):
        self._current_moves = [
            [Move(row, col) for col in range(self.board_size)]
            for row in range(self.board_size)
        ]
        self._winning_combos = self._get_winning_combos()

    def _get_winning_combos(self):
        rows = [
            [(move.row, move.col) for move in row]
            for row in self._current_moves
        ]
        columns = [list(col) for col in zip(*rows)]
        first_diagonal = [row[i] for i, row in enumerate(rows)]
        second_diagonal = [col[j] for j, col in enumerate(reversed(columns))]
        return rows + columns + [first_diagonal, second_diagonal]

    def set_two_player(self):
        self.is_ai_mode = False
        self._players = cycle(PVP_PLAYERS)
        self.current_player = next(self._players)

    def set_ai_mode(self):
        self.is_ai_mode = True
        self.human_player = HUMAN
        self.ai_player = AI
        self._players = cycle([self.human_player, self.ai_player])
        self.current_player = next(self._players)

    def toggle_player(self):
        self.current_player = next(self._players)

    def is_valid_move(self, move: Move) -> bool:
        row, col = move.row, move.col
        move_was_not_played = self._current_moves[row][col].label == ""
        no_winner = not self._has_winner
        return no_winner and move_was_not_played

    def process_move(self, move: Move):
        row, col = move.row, move.col
        self._current_moves[row][col] = move
        for combo in self._winning_combos:
            results = set(
                self._current_moves[n][m].label
                for n, m in combo
            )
            is_win = (len(results) == 1) and ("" not in results)
            if is_win:
                self._has_winner = True
                self.winner_combo = combo
                break

    def has_winner(self) -> bool:
        return self._has_winner

    def is_tied(self) -> bool:
        no_winner = not self._has_winner
        played_moves = (
            move.label for row in self._current_moves for move in row
        )
        return no_winner and all(played_moves)

    def reset_game(self):
        self._has_winner = False
        self.winner_combo = []
        self._setup_board()

    # ===== Helpers for minimax AI =====

    def empty_cells(self):
        cells = []
        for r in range(self.board_size):
            for c in range(self.board_size):
                if self._current_moves[r][c].label == "":
                    cells.append((r, c))
        return cells

    def check_winner_label(self):
        for combo in self._winning_combos:
            values = {self._current_moves[r][c].label for r, c in combo}
            if len(values) == 1 and "" not in values:
                return values.pop()
        return None

    def board_full(self):
        return all(
            move.label != ""
            for row in self._current_moves for move in row
        )

    def minimax(self, is_maximizing: bool) -> int:
        winner = self.check_winner_label()
        if winner == self.ai_player.label:
            return 1      # AI wins
        elif winner == self.human_player.label:
            return -1     # human wins
        elif self.board_full():
            return 0      # draw

        if is_maximizing:
            best_score = -999
            for r, c in self.empty_cells():
                self._current_moves[r][c] = Move(r, c, self.ai_player.label)
                score = self.minimax(False)
                self._current_moves[r][c] = Move(r, c, "")
                best_score = max(best_score, score)
            return best_score
        else:
            best_score = 999
            for r, c in self.empty_cells():
                self._current_moves[r][c] = Move(r, c, self.human_player.label)
                score = self.minimax(True)
                self._current_moves[r][c] = Move(r, c, "")
                best_score = min(best_score, score)
            return best_score

    def get_ai_move(self):
        best_score = -999
        best_move = None
        for r, c in self.empty_cells():
            self._current_moves[r][c] = Move(r, c, self.ai_player.label)
            score = self.minimax(False)   # next is human
            self._current_moves[r][c] = Move(r, c, "")
            if score > best_score:
                best_score = score
                best_move = Move(r, c, self.ai_player.label)
        return best_move


class TicTacToeBoard(tk.Tk):
    def __init__(self, game: TicTacToeGame):
        super().__init__()
        self.title("Tic-Tac-Toe Game")
        self.geometry("420x460")
        self.resizable(False, False)
        self.configure(bg="#2b225a")  # dark purple background

        self._game = game
        self._cells: dict[tuple[int, int], tk.Button] = {}

        self._create_menu()

        self._mode_frame = tk.Frame(self, bg="#2b225a")
        self._mode_frame.pack(pady=10)
        self._create_mode_buttons()

        self._board_frame = tk.Frame(self, bg="#2b225a")
        self._board_frame.pack(fill="both", expand=True)
        self._create_board_display()
        self._create_board_grid()

    def _create_mode_buttons(self):
        tk.Button(
            self._mode_frame,
            text="Two Player",
            command=self.two_player_mode,
            font=font.Font(size=12, weight="bold"),
            width=12,
            bg="#7b5bbf",
            fg="white",
            activebackground="#9b7de0",
            activeforeground="white",
            bd=3
        ).pack(side=tk.LEFT, padx=5)

        tk.Button(
            self._mode_frame,
            text="vs AI",
            command=self.ai_mode,
            font=font.Font(size=12, weight="bold"),
            width=12,
            bg="#ff66c4",
            fg="white",
            activebackground="#ff8cd3",
            activeforeground="white",
            bd=3
        ).pack(side=tk.LEFT, padx=5)

    def two_player_mode(self):
        self._game.set_two_player()
        self.reset_board()
        self._update_display("Two Player: X's turn", "cyan")

    def ai_mode(self):
        self._game.set_ai_mode()
        self.reset_board()
        self._update_display("vs AI: Your turn (X)", "cyan")

    def _create_menu(self):
        menu_bar = tk.Menu(master=self)
        self.config(menu=menu_bar)
        file_menu = tk.Menu(master=menu_bar, tearoff=0)
        file_menu.add_command(label="Play Again", command=self.reset_board)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.destroy)
        menu_bar.add_cascade(label="File", menu=file_menu)

    def _create_board_display(self):
        self.display = tk.Label(
            master=self._board_frame,
            text="Choose mode: Two Player or vs AI",
            font=font.Font(size=16, weight="bold"),
            bg="#2b225a",
            fg="white",
        )
        self.display.pack(pady=10)

    def _create_board_grid(self):
        grid_frame = tk.Frame(master=self._board_frame, bg="#2b225a")
        grid_frame.pack()

        for row in range(self._game.board_size):
            grid_frame.rowconfigure(row, weight=1, minsize=100)
            for col in range(self._game.board_size):
                grid_frame.columnconfigure(col, weight=1, minsize=100)

                btn = tk.Button(
                    master=grid_frame,
                    text="",
                    font=font.Font(size=36, weight="bold"),
                    fg="white",
                    width=3,
                    height=2,
                    bg="#5e3c99",             # purple cell
                    activebackground="#7b5bbf",
                    activeforeground="white",
                    relief="raised",
                    bd=5,
                    command=lambda r=row, c=col: self.play_cell(r, c)
                )
                btn.grid(row=row, column=col, sticky="nsew", padx=3, pady=3)
                self._cells[(row, col)] = btn

    def play_cell(self, row: int, col: int):
        if self._game.is_ai_mode and self._game.current_player == self._game.ai_player:
            return

        move = Move(row, col, self._game.current_player.label)
        if not self._game.is_valid_move(move):
            return

        btn = self._cells[(row, col)]
        self._update_button(btn)
        self._game.process_move(move)
        self._check_game_status()

        if self._game.has_winner() or self._game.is_tied():
            return

        self._game.toggle_player()

        if self._game.is_ai_mode and self._game.current_player == self._game.ai_player:
            self.after(400, self.ai_play)
        else:
            self._update_turn_text()

    def ai_play(self):
        ai_move = self._game.get_ai_move()
        if not ai_move:
            return

        row, col = ai_move.row, ai_move.col
        btn = self._cells[(row, col)]

        self._game.current_player = self._game.ai_player
        self._update_button(btn)
        self._game.process_move(ai_move)
        self._check_game_status()

        if self._game.has_winner() or self._game.is_tied():
            return

        self._game.toggle_player()
        self._update_turn_text()

    def _update_button(self, clicked_btn: tk.Button):
        clicked_btn.config(text=self._game.current_player.label)
        clicked_btn.config(fg=self._game.current_player.color)

    def _update_display(self, msg: str, color: str = "white"):
        self.display["text"] = msg
        self.display["fg"] = color

    def _highlight_cells(self):
        for (row, col), button in self._cells.items():
            if (row, col) in self._game.winner_combo:
                button.config(bg="#ff4c7b")  # pink highlight

    def _check_game_status(self):
        if self._game.is_tied():
            self._update_display("Tied game!", "gold")
        elif self._game.has_winner():
            self._highlight_cells()
            msg = f'Player "{self._game.current_player.label}" won!'
            color = self._game.current_player.color
            self._update_display(msg, color)

    def _update_turn_text(self):
        if self._game.is_ai_mode:
            if self._game.current_player == self._game.ai_player:
                msg = "AI (O) thinking..."
                color = self._game.ai_player.color
            else:
                msg = "Your turn (X)"
                color = self._game.human_player.color
        else:
            msg = f"{self._game.current_player.label}'s turn"
            color = self._game.current_player.color
        self._update_display(msg, color)

    def reset_board(self):
        self._game.reset_game()
        if self._game.is_ai_mode:
            self._game.set_ai_mode()
            self._update_display("vs AI: Your turn (X)", "cyan")
        else:
            self._game.set_two_player()
            self._update_display("Two Player: X's turn", "cyan")

        for btn in self._cells.values():
            btn.config(bg="#5e3c99", text="", fg="white")


def main():
    game = TicTacToeGame()
    board = TicTacToeBoard(game)
    try:
        board.mainloop()
    except KeyboardInterrupt:
        print("Game interrupted. Goodbye!")
    finally:
        try:
            board.destroy()
        except tk.TclError:
            pass


if __name__ == "__main__":
    main()
