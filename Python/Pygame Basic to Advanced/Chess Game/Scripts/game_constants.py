""" All constants related to game is present in ths file. """

import os

ROOT_DIR = "Python/Pygame Basic to Advanced/Chess Game/"

OBJECT_SIZE_RATIO = 6.52174  # Constant term to change the objects size
colors = ["white", "black"]
tokens = ["pawn", "rock", "knight", "bishop", "queen", "king"]
layers = {"white": [7, 6], "black": [0, 1]}


object_locations = {"chess board": os.path.join(ROOT_DIR, "Assets/board.jpg")}
# Coping Token Locations in the object_locations dict
for color in colors:
    for token in tokens:
        object_locations[f"{color} {token}"] = os.path.join(
            ROOT_DIR, f"Assets/{color} tokens/{token}.png"
        )

object_sizes = {
    "pawn": (9, 24.9),
    "rock": (9.1, 23.1),
    "knight": (9.7, 24.8),
    "bishop": (9.7, 22),
    "queen": (9.9, 19.4),
    "king": (9.7, 18.8),
    "chess board": (115, 115),
}

tokens_ofset = {
    "pawn": (12, -95),
    "rock": (9, -85),
    "knight": (10, -95),
    "bishop": (10, -77),
    "queen": (10, -60),
    "king": (10, -56),
}

block_locations = [67.5, 151, 235.5, 317, 401.5, 484, 567.5, 651, 734.5]
board_positions = [[(x, y) for y in block_locations] for x in block_locations]

# Creating Game Constant Variables...
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
FPS_VALUE = 10

BOX_SIZE = 80
BOX_WIDTH = 3
BOX_OFSET = -23

DOT_RADIUS = 7
DOT_WIDTH = 0
DOT_OFSET = 15


# Adding Some Colors...
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
background = (255, 191, 141)
pos_marker = (75, 155, 15)
