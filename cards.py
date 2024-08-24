import ltk
from utils import *

ACT0 = ' '
ACT1 = ' '
ACT2 = ' '
ACT3 = ' '
ACTR = ' '

class Card(ltk.Widget):
    classes = ['card']

    def __init__(self, cls=''):
        super().__init__(
            element('h1').append(
                span('fullname').append(
                    span('cardname').text('Card Name'),
                    span('actioncost').text(ACT1)
                ),
                span('actiontype').text('Feat 1')
            ),
            'Describe The Action Here'
        )
        self.addClass(cls)

    def _getsetvalues(self, selector, value=None):
        el = self.find(selector)
        if value is None:
            return el.text()
        else:
            el.text(value)
            return self

    def name(self, value=None):
        return self._getsetvalues('.cardname', value)

    def atype(self, value=None):
        return self._getsetvalues('.actiontype', value)

    def actioncost(self, value=None):
        return self._getsetvalues('.actioncost', value)

    def reset_class(self):
        self.element.removeClass()
        self.addClass(*self.classes)
        return self


class Trait(ltk.Widget):
    classes = ['trait']
    tag = 'span'