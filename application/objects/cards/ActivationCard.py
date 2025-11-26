
from __future__ import annotations
from enum import Enum
from config.Configuration import Configuration


class ActivationCard:
    class Type(Enum):
        C_ACTIVATE_NATURAL = ("card-activate-natural", "N")
        C_ACTIVATE_INTEGER = ("card-activate-integer", "Z")
        C_ACTIVATE_RATIONAL = ("card-activate-rational", "Q")
        C_ACTIVATE_REAL = ("card-activate-real", "R")
        C_ACTIVATE_COMPLEX = ("card-activate-complex", "C")
    
    def __init__(self, type: ActivationCard.Type, *args, **kwargs):
        self.__type = type
        super().__init__(Configuration.engine_assets_dir / 'images' / 'cards' / f'{type.value[0]}.png', *args, **kwargs)

    def getType(self) -> ActivationCard.Type:
        return self.__type