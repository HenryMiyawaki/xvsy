import pygame

class IComponent:

    def setSurface(self, surface: pygame.Surface):
        pass

    def getPosition(self) -> tuple[int, int]:
        pass

    def get(self) -> pygame.Surface:
        pass
    

class Component(IComponent):
    def __init__(self, position: tuple[int, int], *a, **k):
        self.__surface: pygame.Surface = None
        self.__position: tuple[int, int] = position
        super().__init__(*a, **k)

    def get(self) -> pygame.Surface:
        return self.__surface
    
    def setSurface(self, surface: pygame.Surface):
        self.__surface = surface

    def getPosition(self):
        return self.__position
