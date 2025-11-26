

from typing import Self
import pygame
from core.ui.interfaces.IOutline import Outlined
from core.ui.widgets.Component import Component


class OutlinedComponent(Component, Outlined):
    def __init__(self, *a, **k):
        Component.__init__(self, *a, **k)
        Outlined.__init__(self)

    def __apply(self):
        surface = self.get()
        if surface is None or not self.isOutlineEnabled():
            return 

        pygame.draw.rect(surface, self.getBorderColor(), surface.get_rect(), self.getBorderWidth())
        print("applied outline")

    def setSurface(self, surface):
        super().setSurface(surface)
        self.__apply()

    def setBorderColor(self, color: tuple[int, int, int]) -> Self:
        super().setBorderColor(color)
        self.__apply()
        return self

    def setBorderWidth(self, width: int) -> Self:
        super().setBorderWidth(width)
        self.__apply()
        return self

