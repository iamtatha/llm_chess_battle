import tkinter as tk

def create_chessboard(root, positions):
    """
    Creates a chessboard with pieces placed based on the given positions.

    Args:
        root (tk.Tk): The main Tkinter window.
        positions (dict): A dictionary mapping positions (e.g., 'A1') to piece unicode (e.g., '\u265F').
    """
    # Define the size of the chessboard
    board_size = 8
    cell_size = 60

    # Create a canvas to draw the chessboard
    canvas = tk.Canvas(root, width=board_size * cell_size, height=board_size * cell_size)
    canvas.pack()

    # Colors for the chessboard
    light_color = "#F0D9B5"
    dark_color = "#B58863"

    # Unicode for chess pieces (Black and White)
    piece_unicode = {
        'K': '\u2654', 'Q': '\u2655', 'R': '\u2656', 'B': '\u2657', 'N': '\u2658', 'P': '\u2659',
        'k': '\u265A', 'q': '\u265B', 'r': '\u265C', 'b': '\u265D', 'n': '\u265E', 'p': '\u265F'
    }

    # Draw the chessboard
    for row in range(board_size):
        for col in range(board_size):
            x1 = col * cell_size
            y1 = row * cell_size
            x2 = x1 + cell_size
            y2 = y1 + cell_size

            color = light_color if (row + col) % 2 == 0 else dark_color
            canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="")

    # Place the pieces on the board
    for pos, piece in positions.items():
        col = ord(pos[0].upper()) - ord('A')
        row = board_size - int(pos[1])

        x = col * cell_size + cell_size // 2
        y = row * cell_size + cell_size // 2

        canvas.create_text(x, y, text=piece_unicode[piece], font=("Arial", cell_size // 1), fill="black")

if __name__ == "__main__":
    # Example positions: 'K' for white king, 'k' for black king, etc.
    positions = {
        'E1': 'K', 'D1': 'Q', 'A1': 'R', 'H1': 'R', 'C1': 'B', 'F1': 'B', 'G1': 'N', 'B1': 'N', 'A2': 'P',
        'H2': 'P', 'E8': 'k', 'D8': 'q', 'A8': 'r', 'H8': 'r', 'C8': 'b', 'F8': 'b', 'G8': 'n', 'B8': 'n',
        'A7': 'p', 'H7': 'p'
    }

    # Create the main Tkinter window
    root = tk.Tk()
    root.title("Chessboard with Pieces")

    create_chessboard(root, positions)

    root.mainloop()
