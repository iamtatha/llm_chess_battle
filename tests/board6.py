import tkinter as tk
import time
import cv2
import numpy as np

def create_chessboard(root, piece_positions):
    """
    Creates a chessboard with pieces placed based on the given piece_positions.

    Args:
        root (tk.Tk): The main Tkinter window.
        piece_positions (dict): A dictionary mapping pieces to their positions and Unicode characters.
    """
    board_size = 8
    cell_size = 60

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
        row = 8 - int(pos[1])

        x = col * cell_size + cell_size // 2
        y = row * cell_size + cell_size // 2

        piece_objects[piece] = canvas.create_text(x, y, text=unicode_char, font=("Arial", cell_size // 2), fill="black")

    return canvas, piece_objects

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
    global move_index
    if move_index < len(piece_positions) - 1:
        move_index += 1
        update_board(canvas, piece_objects, piece_positions, move_index)

def prev_move():
    global move_index
    if move_index > 0:
        move_index -= 1
        update_board(canvas, piece_objects, piece_positions, move_index)

def save_as_video():
    """
    Saves the game moves as a video file.
    """
    board_size = 8
    cell_size = 60
    frame_width = board_size * cell_size
    frame_height = board_size * cell_size
    fps = 2  # Frames per second for the video

    # Define the video writer
    out = cv2.VideoWriter("chess_game.mp4", cv2.VideoWriter_fourcc(*'mp4v'), fps, (frame_width, frame_height))

    for move_index in range(len(piece_positions)):
        update_board(canvas, piece_objects, piece_positions, move_index)

        # Save current board as an image
        canvas.update()
        canvas_image = canvas_to_image(canvas, frame_width, frame_height)

        # Add the frame to the video
        out.write(canvas_image)

    out.release()
    print("Game saved as chess_game.mp4")

def canvas_to_image(canvas, width, height):
    """
    Converts a Tkinter canvas to an OpenCV image using Pillow (PIL).

    Args:
        canvas (tk.Canvas): The canvas object.
        width (int): The width of the image.
        height (int): The height of the image.

    Returns:
        np.array: The image in OpenCV format.
    """
    # Save the canvas as a PostScript file
    ps_file = "temp_canvas.ps"
    canvas.postscript(file=ps_file, colormode='color')

    # Convert PostScript to an image using Pillow
    from PIL import Image
    img = Image.open(ps_file)
    img = img.resize((width, height), Image.Resampling.LANCZOS)  # Resize to fit the video frame

    # Convert the image to OpenCV format (BGR)
    open_cv_image = np.array(img)
    open_cv_image = cv2.cvtColor(open_cv_image, cv2.COLOR_RGB2BGR)

    # Delete the temporary PostScript file
    import os
    os.remove(ps_file)

    return open_cv_image


def play_match():
    # root.after(
    #     2000, update_board, canvas, piece_objects, piece_positions, piece_positions[1]
    # )
    pass

# Update the main GUI to add the new "Play the Match" button
if __name__ == "__main__":
    import io
    from PIL import Image, ImageOps

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
        # Add more moves here
    ]

    root = tk.Tk()
    root.title("Chessboard with Save Feature")

    move_index = 0
    canvas, piece_objects = create_chessboard(root, piece_positions[move_index])

    # Navigation buttons
    btn_next = tk.Button(root, text="Next Move", command=next_move)
    btn_next.pack(side=tk.RIGHT, padx=10)

    btn_prev = tk.Button(root, text="Previous Move", command=prev_move)
    btn_prev.pack(side=tk.LEFT, padx=10)

    # Save button
    btn_save = tk.Button(root, text="Save as Video", command=save_as_video)
    btn_save.pack(side=tk.BOTTOM, pady=10)

    # Play Match button
    btn_play = tk.Button(root, text="Play the Match", command=play_match)
    btn_play.pack(side=tk.BOTTOM, pady=10)

    root.mainloop()
