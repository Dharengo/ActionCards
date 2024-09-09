from pyscript.web import ContainerElement, document  # type: ignore


#Experimental metaclass, to be used just for improved syntax, as it simply applies the decorator to the class
#To be implemented later
# class _WidgetMeta(type):
#     def __new__(cls, *args, tag=None, classes=None, classoverride=False, **kwargs):
#         cls = super().__new__(cls, *args, **kwargs)
#         return widgetsettings(tag, classes, classoverride)(cls)

#decorator applies the metaclass if pyodide, otherwise it doesn't
# def _widgetmeta(cls):
#     if check_pyodide()  # Implement this first
#         return _WidgetMeta(cls.__name__, cls.__bases__, cls.__dict__.copy())
#     return cls


def _listify(classes):
    return classes.split(' ') if isinstance(classes, str) else list(classes)

def widgetsettings(tag=None, classes=None, classoverride=False):  # Does exactly what the metaclass did
    def deco(cls):
        if not issubclass(cls, Widget):
            raise TypeError(f'{cls} is not a subclass of {Widget}.')
        if tag:
            cls._tag = tag
        if classes is not None:
            if classoverride:
                cls._defaultclasses = _listify(classes)
            else:
                cls._defaultclasses = cls._defaultclasses.copy()
                cls._defaultclasses.extend(_listify(classes))
        return cls
    return deco

# @_widgetmeta
class Widget(ContainerElement):
    def __init__(self, *args, dom_element=None, classes=(), **kwargs):
        if dom_element is None:
            dom_element = document.createElement(self._tag)
        classes = self._defaultclasses + _listify(classes)
        super().__init__(*args, dom_element=dom_element, classes=classes, **kwargs)

    def reset_class(self):
        self.classes.remove(*self.classes)
        self.classes.add(*self._defaultclasses)
        return self
widgetsettings(tag='div', classes=(), classoverride=True)(Widget)  #must apply after the fact to avoid error
