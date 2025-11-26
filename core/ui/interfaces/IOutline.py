from abc import ABCMeta, abstractmethod

class IOutline(metaclass=ABCMeta):
    
    @abstractmethod
    def setBorderColor(self, color: tuple[int, int, int]):
        pass

    @abstractmethod
    def setBorderWidth(self, width: int):
        pass

    @abstractmethod
    def getBorderColor(self) -> tuple[int, int, int]:
        pass

    @abstractmethod
    def getBorderWidth(self) -> int:
        pass

    
class Outlined(IOutline):
    def __init__(self, *args, **kwargs):
        self.__borderColor: tuple[int, int, int] = (255, 255, 255)
        self.__borderWidth: int = 2
        self.__borderEnabled: bool = False
    
    def setBorderColor(self, color: tuple[int, int, int]):
        self.__borderColor = color
        self.__borderEnabled = True
        return self

    def setBorderWidth(self, width: int):
        self.__borderWidth = width
        return self
    
    def isOutlineEnabled(self) -> bool:
        return self.__borderEnabled
    
    def getBorderColor(self) -> tuple[int, int, int]:
        return self.__borderColor
    
    def getBorderWidth(self) -> int:
        return self.__borderWidth