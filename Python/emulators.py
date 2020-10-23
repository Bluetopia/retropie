'''
    emulators.py - Default button light configurations for emulators.

    Player 1 (values turn OFF light because I don't feel like re-wiring all the buttons):

        (128)   (64)

            (4)
    (1)     (8)     (16)
    (2)             (32)

    Player 2 (values turn OFF light, same as above)

        (128)   (64)
        
            (4)
    (16)    (8)     (1)
    (32)            (2)

'''

emulators = {
    "atari2600" : (247, 247),   # Fire
    "nes" : (23, 53),           # A, B, Select, Start
    "mastersystem" : (23, 53),  # A, B, Select, Start
    "gb": (23, 53),             # A, B, Select, Start
    "gba": (5, 20),             # A, B, L, R, Select, Start
    "gamegear": (151, 181),     # A, B, Start
    "megadrive": (149, 149),    # A, B, C, Start
    "neogeo": (40, 10),         # A, B, C, D, Coin, Start
    "pcengine": (151, 181),     # A, B, Select, Start
    "snes" : (0, 0),            # A, B, X, Y, L, R, Select, Start
    "psx" : (0, 0),             # Square, X, Circle, Triangle, L, R
    "emulationstation" : (3, 48)
}


