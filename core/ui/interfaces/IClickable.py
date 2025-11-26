from abc import ABCMeta, abstractmethod
from typing import Self

class IClickable(metaclass=ABCMeta):
    @abstractmethod
    def onClick(self, action: callable):
        pass
    
    @abstractmethod
    def getAction(self) -> callable:
        pass

class Clickable(IClickable):
    def __init__(self, *args, **kwargs):
        self.__onClickAction: callable = lambda: None
        super().__init__(*args, **kwargs)

    def onClick(self, action: callable) -> Self:
        self.__onClickAction = action
        return self

    def getAction(self) -> callable:
        return self.__onClickAction