import pygame
from core.loggers import engineInfo, engineLog

class EngineSpriteGroup(pygame.sprite.Group):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__EngineBind__()

    def __EngineBind__(self):
        for attr_name in dir(self):
            attr = getattr(self, attr_name)
            if callable(attr):
                if getattr(attr, "__EngineEventFunction__", False):
                    bind = getattr(attr, "__EngineEventFunctionBind__", None)
                    engineLog(f"[✓] Método '{attr_name}' está marcado como __EngineEventFunction__")
                    engineInfo(f"\t --> Binding function {bind}")
                    bind(self)
                    