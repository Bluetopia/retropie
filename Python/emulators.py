'''
    emulators.py - Default button light configurations for emulators.

    Player 1:

        (128)   (64)

            (16)
    (32)     (2)     (8)
    (4)              (1)

    Player 2:

        (128)   (64)

            (16)
    (32)     (2)     (8)
    (4)              (1)

'''

emulators = {
    "atari2600" : (194, 194),        # Fire
    "atarilynx" : (118, 118),        # A, B, Start, L, R
    "nes" : (195, 195),              # A, B, Select, Start
    "mastersystem" : (3, 3),         # A, B
    "gb": (195, 195),                # A, B, Select, Start
    "gbc": (195, 195),               # A, B, Select, Start
#    "gba": (5, 20),             # A, B, L, R, Select, Start
    "gamegear": (67, 67),            # A, B, Start
    "megadrive": (71, 71),           # A, B, C, Start
#    "neogeo": (40, 10),         # A, B, C, D, Coin, Start
    "pcengine": (195, 195),          # A, B, Select, Start
    "snes" : (255, 255),             # A, B, X, Y, L, R, Select, Start
#    "psx" : (0, 0),             # Square, X, Circle, Triangle, L, R
    "emulationstation" : (219, 219)  # X, Y, A, B, Select, Start
}


