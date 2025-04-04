import tkinter as tk
import time
import cv2
import numpy as np
import os
from PIL import Image
os.environ["PATH"] += os.pathsep + "/usr/local/bin"


def create_chessboard(root, piece_positions):
    """
    Creates a chessboard with pieces placed based on the given piece_positions.
    """
    board_size = 8
    cell_size = 80

    # Create a canvas to draw the chessboard
    canvas = tk.Canvas(root, width=board_size * cell_size, height=board_size * cell_size)
    canvas.pack()

    light_color = "#F0D9B5"
    dark_color = "#B58863"

    for row in range(board_size):
        for col in range(board_size):
            x1 = col * cell_size
            y1 = row * cell_size
            x2 = x1 + cell_size
            y2 = y1 + cell_size

            color = light_color if (row + col) % 2 == 0 else dark_color
            canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="")


    piece_objects = {}

    for piece, details in piece_positions.items():
        pos, unicode_char = details
        col = ord(pos[0].upper()) - ord('A')
        row = board_size - int(pos[1])

        x = col * cell_size + cell_size // 2
        y = row * cell_size + cell_size // 2

        piece_objects[piece] = canvas.create_text(x, y, text=unicode_char, font=("Arial", cell_size // 1), fill="black")

    return canvas, piece_objects

def animate_moves(canvas, piece_objects, piece_positions, new_piece_positions):
    """
    Animates the movement of chess pieces from the current positions to new positions.
    """
    cell_size = 80

    # Reverse dictionary for easy lookup of piece by position
    current_positions = {details[0]: piece for piece, details in piece_positions.items()}

    for piece, details in new_piece_positions.items():
        new_pos, unicode_char = details
        if piece in piece_positions:
            old_pos = piece_positions[piece][0]

            if old_pos and old_pos != new_pos:
                col_start = ord(old_pos[0].upper()) - ord('A')
                row_start = 8 - int(old_pos[1])
                col_end = ord(new_pos[0].upper()) - ord('A')
                row_end = 8 - int(new_pos[1])

                x_start = col_start * cell_size + cell_size // 2
                y_start = row_start * cell_size + cell_size // 2
                x_end = col_end * cell_size + cell_size // 2
                y_end = row_end * cell_size + cell_size // 2

                # Animate movement
                for step in range(20):
                    dx = (x_end - x_start) / 20
                    dy = (y_end - y_start) / 20
                    canvas.move(piece_objects[piece], dx, dy)
                    canvas.update()
                    time.sleep(0.01)

                # Update final position
                canvas.coords(piece_objects[piece], x_end, y_end)

    for piece, details in new_piece_positions.items():
        new_pos, unicode_char = details
        if piece not in piece_objects:
            col = ord(new_pos[0].upper()) - ord('A')
            row = 8 - int(new_pos[1])
            x = col * cell_size + cell_size // 2
            y = row * cell_size + cell_size // 2
            piece_objects[piece] = canvas.create_text(x, y, text=unicode_char, font=("Arial", cell_size // 1), fill="black")

def update_board(canvas, piece_objects, current_positions):
    """
    Updates the board to reflect the state at a specific move index.
    """

    cell_size = 80 

    for piece, details in piece_objects.items():
        if piece in current_positions:
            pos, _ = current_positions[piece]
            col = ord(pos[0].upper()) - ord('A')
            row = 8 - int(pos[1])

            x_coord = col * cell_size + cell_size // 2
            y_coord = row * cell_size + cell_size // 2

            canvas.coords(piece_objects[piece], x_coord, y_coord)
        else:
            # Hide the piece if it's not in the current state
            canvas.coords(piece_objects[piece], -100, -100)

def next_move():
    root.after(
        0, animate_moves, canvas, piece_objects, piece_positions, new_piece_positions
    )

def prev_move():
    root.after(
        0, animate_moves, canvas, piece_objects, new_piece_positions, piece_positions
    )

def play():
    update_board(canvas, piece_objects, piece_positions)
    root.after(
        0, animate_moves, canvas, piece_objects, piece_positions, new_piece_positions
    )

def reset():
    update_board(canvas, piece_objects, piece_positions)

if __name__ == "__main__":
    # Initial positions: 'K' for white king, 'k' for black king, etc.
    piece_positions = {
        "K": ["E1", "\u2654"],
        "Q": ["D1", "\u2655"],
        "R1": ["A1", "\u2656"],
        "R2": ["H1", "\u2656"],
        "B1": ["C1", "\u2657"],
        "B2": ["F1", "\u2657"],
        "N1": ["B1", "\u2658"],
        "N2": ["G1", "\u2658"],
        "P1": ["A2", "\u2659"],
        "P2": ["B2", "\u2659"],
        "P3": ["C2", "\u2659"],
        "P4": ["D2", "\u2659"],
        "P5": ["E2", "\u2659"],
        "P6": ["F2", "\u2659"],
        "P7": ["G2", "\u2659"],
        "P8": ["H2", "\u2659"],
        "k": ["E8", "\u265A"],
        "q": ["D8", "\u265B"],
        "r1": ["A8", "\u265C"],
        "r2": ["H8", "\u265C"],
        "b1": ["C8", "\u265D"],
        "b2": ["F8", "\u265D"],
        "n1": ["B8", "\u265E"],
        "n2": ["G8", "\u265E"],
        "p1": ["A7", "\u265F"],
        "p2": ["B7", "\u265F"],
        "p3": ["C7", "\u265F"],
        "p4": ["D7", "\u265F"],
        "p5": ["E7", "\u265F"],
        "p6": ["F7", "\u265F"],
        "p7": ["G7", "\u265F"],
        "p8": ["H7", "\u265F"],
    }

    # New positions after a move
    new_piece_positions = {
      "K": ["E1", "\u2654"],
        "Q": ["D1", "\u2655"],
        "R1": ["A1", "\u2656"],
        "R2": ["H1", "\u2656"],
        "B1": ["C1", "\u2657"],
        "B2": ["F1", "\u2657"],
        "N1": ["B1", "\u2658"],
        "N2": ["G1", "\u2658"],
        "P1": ["A2", "\u2659"],
        "P2": ["B2", "\u2659"],
        "P3": ["C2", "\u2659"],
        "P4": ["D2", "\u2659"],
        "P5": ["E2", "\u2659"],
        "P6": ["F2", "\u2659"],
        "P7": ["G4", "\u2659"],
        "P8": ["H2", "\u2659"],
        "k": ["E8", "\u265A"],
        "q": ["D8", "\u265B"],
        "r1": ["A8", "\u265C"],
        "r2": ["H8", "\u265C"],
        "b1": ["C8", "\u265D"],
        "b2": ["F8", "\u265D"],
        "n1": ["B8", "\u265E"],
        "n2": ["G8", "\u265E"],
        "p1": ["A7", "\u265F"],
        "p2": ["B7", "\u265F"],
        "p3": ["C7", "\u265F"],
        "p4": ["D7", "\u265F"],
        "p5": ["E7", "\u265F"],
        "p6": ["F7", "\u265F"],
        "p7": ["G7", "\u265F"],
        "p8": ["H7", "\u265F"],
}

    root = tk.Tk()
    root.title("Chessboard with Animated Moves")

    canvas, piece_objects = create_chessboard(root, piece_positions)

    # Add buttons for navigation
    btn_next = tk.Button(root, text="Next Move", command=next_move)
    btn_next.pack(side=tk.RIGHT, padx=10)

    btn_prev = tk.Button(root, text="Previous Move", command=prev_move)
    btn_prev.pack(side=tk.LEFT, padx=10)
    
    btn_save = tk.Button(root, text="Reset Board", command=reset)
    btn_save.pack(side=tk.RIGHT, pady=10)

    btn_play = tk.Button(root, text="Play Match", command=play)
    btn_play.pack(side=tk.LEFT, padx=10)

    root.mainloop()
