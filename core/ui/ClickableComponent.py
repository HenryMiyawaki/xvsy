
from typing import Self
from core.ui.interfaces.IClickable import Clickable
from core.ui.widgets import Component
from core.events.EngineClick import EngineClick

class ClickableComponent(Component, Clickable):
    def __init__(self, *a, **k):
        Component.__init__(self, *a, **k)
        Clickable.__init__(self)
    
    def __apply(self):
        decorator = EngineClick()
        decorator(self.getAction())

    def onClick(self, action: callable) -> Self:
        Clickable.onClick(self, action)
        self.__apply()
        return self