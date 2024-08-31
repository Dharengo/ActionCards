from pyscript.web import ContainerElement, document  # type: ignore

def _listify(classes):
    return classes.split(' ') if isinstance(classes, str) else list(classes)

class _WidgetMeta(type):
    def __new__(cls, *args, tag=None, classes=None, classoverride=False, **kwargs):
        cls = super().__new__(cls, *args, **kwargs)
        if tag:
            cls._tag = tag
        if classes is not None:
            if classoverride:
                cls._defaultclasses = _listify(classes)
            else:
                cls._defaultclasses = cls._defaultclasses.copy()
                cls._defaultclasses.extend(_listify(classes))
        return cls

class Widget(ContainerElement, metaclass=_WidgetMeta, tag='div', classes=(), classoverride=True):
    def __init__(self, *args, dom_element=None, classes=(), **kwargs):
        if dom_element is None:
            dom_element = document.createElement(self._tag)
        classes = self._defaultclasses + _listify(classes)
        super().__init__(*args, dom_element=dom_element, classes=classes, **kwargs)

    def reset_class(self):
        self.classes.remove(*self.classes)
        self.classes.add(*self._defaultclasses)
        return self