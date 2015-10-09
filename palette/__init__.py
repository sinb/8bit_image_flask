import numpy as np
import os
class Palette:
    def __init__(self):
        dir = os.path.dirname(os.path.realpath(__file__))
        self.preset = {}
        self.preset['AppleII'] = np.load(os.path.join(dir, 'AppleII.npy'))
        self.preset['Atari2600'] = np.load(os.path.join(dir, 'Atari2600.npy'))
        self.preset['Commodore64'] = np.load(os.path.join(dir, 'Commodore64.npy'))
        self.preset['Contra'] = np.load(os.path.join(dir, 'Contra.npy'))
        self.preset['FlashMan'] = np.load(os.path.join(dir, 'FlashMan.npy'))
        self.preset['Gameboy'] = np.load(os.path.join(dir, 'Gameboy.npy'))
        self.preset['Grayscale'] = np.load(os.path.join(dir, 'Grayscale.npy'))
        self.preset['Hyrule'] = np.load(os.path.join(dir, 'Hyrule.npy'))
        self.preset['Intellivision'] = np.load(os.path.join(dir, 'Intellivision.npy'))
        self.preset['KungFu'] = np.load(os.path.join(dir, 'KungFu.npy'))
        self.preset['NES'] = np.load(os.path.join(dir, 'NES.npy'))
        self.preset['SegaMasterSystem'] = np.load(os.path.join(dir, 'SegaMasterSystem.npy'))
        self.preset['SuperMarioBros'] = np.load(os.path.join(dir, 'SuperMarioBros.npy'))
        self.preset['Tetris'] = np.load(os.path.join(dir, 'Tetris.npy'))
    def __call__(self, key):
        try:
            return self.preset[key]
        except KeyError, k:
            return None