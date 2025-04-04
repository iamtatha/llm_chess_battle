import tkinter as tk
import time

def create_chessboard(root, piece_positions):
    """
    Creates a chessboard with pieces placed based on the given piece_positions.

    Args:
        root (tk.Tk): The main Tkinter window.
        piece_positions (dict): A dictionary mapping pieces to their positions and Unicode characters.
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

    # Draw the chessboard
    for row in range(board_size):
        for col in range(board_size):
            x1 = col * cell_size
            y1 = row * cell_size
            x2 = x1 + cell_size
            y2 = y1 + cell_size

            color = light_color if (row + col) % 2 == 0 else dark_color
            canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="")

    # Dictionary to hold piece objects
    piece_objects = {}

    # Place the pieces on the board
    for piece, details in piece_positions.items():
        pos, unicode_char = details
        col = ord(pos[0].upper()) - ord('A')
        row = board_size - int(pos[1])

        x = col * cell_size + cell_size // 2
        y = row * cell_size + cell_size // 2

        piece_objects[piece] = canvas.create_text(x, y, text=unicode_char, font=("Arial", cell_size // 2), fill="black")

    return canvas, piece_objects

def move_piece(canvas, piece_objects, piece, old_pos, new_pos):
    """
    Moves a piece from old_pos to new_pos on the canvas.

    Args:
        canvas (tk.Canvas): The canvas object containing the chessboard.
        piece_objects (dict): A dictionary of canvas objects for the pieces.
        piece (str): The piece to move.
        old_pos (str): The current position of the piece.
        new_pos (str): The target position of the piece.
    """
    cell_size = 60

    col_start = ord(old_pos[0].upper()) - ord('A')
    row_start = 8 - int(old_pos[1])
    col_end = ord(new_pos[0].upper()) - ord('A')
    row_end = 8 - int(new_pos[1])

    x_start = col_start * cell_size + cell_size // 2
    y_start = row_start * cell_size + cell_size // 2
    x_end = col_end * cell_size + cell_size // 2
    y_end = row_end * cell_size + cell_size // 2

    # Move the piece
    canvas.coords(piece_objects[piece], x_end, y_end)

def update_board(canvas, piece_objects, piece_positions, move_index):
    """
    Updates the board to reflect the state at move_index.

    Args:
        canvas (tk.Canvas): The canvas object containing the chessboard.
        piece_objects (dict): A dictionary of canvas objects for the pieces.
        piece_positions (list of dict): A list of piece positions at each step.
        move_index (int): The index of the move to display.
    """
    current_positions = piece_positions[move_index]
    for piece, details in current_positions.items():
        pos, unicode_char = details
        x = ord(pos[0].upper()) - ord('A')
        y = 8 - int(pos[1])
        cell_size = 60
        x_coord = x * cell_size + cell_size // 2
        y_coord = y * cell_size + cell_size // 2
        canvas.coords(piece_objects[piece], x_coord, y_coord)

def next_move():
    """
    Moves to the next move in the sequence.
    """
    global move_index
    if move_index < len(piece_positions) - 1:
        move_index += 1
        update_board(canvas, piece_objects, piece_positions, move_index)

def prev_move():
    """
    Moves to the previous move in the sequence.
    """
    global move_index
    if move_index > 0:
        move_index -= 1
        update_board(canvas, piece_objects, piece_positions, move_index)

if __name__ == "__main__":
    # List of piece positions at each move
    piece_positions = [
        {  # Initial position
            'K': ['E1', '\u2654'], 
            'Q': ['D1', '\u2655'], 
            'R1': ['A1', '\u2656'], 
            'R2': ['H1', '\u2656'], 
            'P1': ['A2', '\u2659']
        },
        {  # Move 1
            'K': ['E2', '\u2654'], 
            'Q': ['D2', '\u2655'], 
            'R1': ['A2', '\u2656'], 
            'R2': ['H2', '\u2656'], 
            'P1': ['A3', '\u2659']
        }
    ]

    # Create the main Tkinter window
    root = tk.Tk()
    root.title("Chessboard with Move Control")

    # Global move index
    move_index = 0

    # Create the chessboard
    canvas, piece_objects = create_chessboard(root, piece_positions[move_index])

    # Add buttons for navigation
    btn_next = tk.Button(root, text="Next Move", command=next_move)
    btn_next.pack(side=tk.RIGHT, padx=10)

    btn_prev = tk.Button(root, text="Previous Move", command=prev_move)
    btn_prev.pack(side=tk.LEFT, padx=10)

    # Start the Tkinter main loop
    root.mainloop()
