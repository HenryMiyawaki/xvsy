import pygame
from core.ui.OutlinedComponent import OutlinedComponent
from core.ui.interfaces.IOutline import Outlined
from core.ui.widgets.Component import Component

class IPixo:
    pass

class Pixo(OutlinedComponent, IPixo):
    def __init__(self, text: str, fontName: str = "arial", size=16,*a, **k):
        super().__init__(*a, **k)
        self.__text = text
        self.__font = pygame.font.SysFont(fontName, size)
        self.setSurface(self.__font.render(self.__text, True, (255,255,255)).convert_alpha())
