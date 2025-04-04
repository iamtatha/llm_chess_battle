from PIL import Image, ImageDraw, ImageFont

# Chess pieces Unicode symbols
# Load images of chess pieces
piece_files = {
    'wK': u"\u265A\n",
    'wQ': u"\u265B\n",
    'wR': u"\u265C\n",
    'wB': u"\u265D\n",
    'wN': u"\u265E\n",
    'wP': u"\u265F\n",
    'bK': u"\u2654\n",
    'bQ': u"\u2655\n",
    'bR': u"\u2656\n",
    'bB': u"\u2657\n",
    'bN': u"\u2658\n",
    'bP': u"\u2659\n",
}

def draw_chessboard_with_pieces(positions, square_size=80, output_file="chessboard.png"):
    board_size = 8 * square_size
    board_img = Image.new("RGB", (board_size, board_size), "white")
    draw = ImageDraw.Draw(board_img)

    # Colors for squares
    light_color = (240, 217, 181)
    dark_color = (181, 136, 99)

    # Draw squares
    for row in range(8):
        for col in range(8):
            color = light_color if (row + col) % 2 == 0 else dark_color
            x0, y0 = col * square_size, row * square_size
            x1, y1 = x0 + square_size, y0 + square_size
            draw.rectangle([x0, y0, x1, y1], fill=color)

    # Add pieces to the board
    try:
        font = ImageFont.truetype("arial.ttf", int(square_size * 0.9))
    except IOError:
        font = ImageFont.load_default()

    for position, piece in positions.items():
        if piece not in piece_files:
            continue

        col = ord(position[0].lower()) - ord('a')
        row = 8 - int(position[1])

        x = col * square_size + square_size // 2
        y = row * square_size + square_size // 2
        draw.text((x, y), piece_files[piece], font=font, anchor="mm")

    # Save the image
    board_img.save(output_file)
    print(f"Chessboard saved as {output_file}")

# Example usage
positions = {
    "e4": "wK",  # White King
    "e5": "bk",  # Black King
    "a1": "wR",  # White Rook
    "h8": "bR",  # Black Rook
    "d2": "wP",  # White Pawn
    "g7": "bP"   # Black Pawn
}

draw_chessboard_with_pieces(positions)
