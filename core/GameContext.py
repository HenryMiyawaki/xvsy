
import pygame
from abc import ABC, abstractmethod
from config.Configuration import Configuration
from core.ui.widgets.Component import IComponent
from collections import deque

class IGameContext(ABC):

    @abstractmethod
    def update(self, screen: pygame.Surface):
        pass

    @abstractmethod
    def add(self, component: IComponent, position: tuple[int, int]):
        pass

    @abstractmethod
    def getRenderQueue(self) -> deque[IComponent]:
        pass

class GameContext(IGameContext):

    def __init__(self):
        super().__init__()
        self.__background: pygame.Surface = pygame.Surface(Configuration.engine_resolution)
        self.__renderQueue = deque()

    def update(self, screen: pygame.Surface):
        screen.blit(self.__background, (0, 0))
        for component in self.getRenderQueue():
            screen.blit(component.get(), component.getPosition())

    def setBackground(self, background: pygame.Surface):
        self.__background = background

    def getBackground(self) -> pygame.Surface:
        return self.__background
    
    def add(self, component: IComponent):
        self.__renderQueue.append(component)
    

    def getRenderQueue(self) -> deque[IComponent]:
        return self.__renderQueue

