import pygame
from config.Configuration import Configuration
from core.GameContext import GameContext
from core.ui.widgets.Pixo import Pixo

class XvsyMenu(GameContext):

    def __init__(self):
        super().__init__() 
        self.getBackground().fill((30, 30, 30))
        self.add(Pixo("Jogar", position=(Configuration.engine_resolution[0]//2, 100), size=48).setBorderColor((255, 0, 0)))


