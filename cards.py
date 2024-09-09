from pyscript.web import h1, span  # type: ignore
from webwidgets import Widget, widgetsettings

ACT0 = ' '
ACT1 = ' '
ACT2 = ' '
ACT3 = ' '
ACTR = ' '


@widgetsettings(classes='card')
class Card(Widget):
    def __init__(self, *args, **kwargs):
        super().__init__(
            h1(
                span(
                    span('Card Name', classes='cardname'),
                    span(ACT1, classes='actioncost'),
                    classes='fullname'),
                span('Feat 1', classes='actiontype')),
            'Describe The Action Here',
            *args, **kwargs
        )

    def field(self, selector, value=None):
        el = self.find(selector)[0]
        if value is None:
            return el.innerText
        else:
            el.innerText = value
            return self

    def name(self, value=None):
        return self.field('.cardname', value)

    def atype(self, value=None):
        return self.field('.actiontype', value)

    def actioncost(self, value=None):
        return self.field('.actioncost', value)

    def style(self, class_=None):
        if class_:
            self.reset_class()
            self.classes.add(class_)
            return self
        else:
            for class_ in self.classes:
                if class_ not in self._defaultclasses:
                    return class_


def trait():
    return span(classes='trait')
