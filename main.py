import ltk

CSS = 'card.css'


def element(tag, cls=''):
    return ltk.create(f'<{tag}>').addClass(cls)


def div(cls=''):
    return element('div', cls)


def span(cls=''):
    return element('span', cls)


class Card(ltk.Widget):
    classes = ['card']

    def __init__(self, cls=''):
        super().__init__(
            element('h1').append(
                span('cardname').text('Card Name'),
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

    def reset_class(self):
        self.element.removeClass()
        self.addClass(*self.classes)
        return self


class Trait(ltk.Widget):
    classes = ['trait']
    tag = 'span'


ltk.find('#loading').remove()
ltk.find('.ltk-built-with').remove()
ltk.inject_css(CSS)

(card := Card('skill')).appendTo(ltk.find('body'))

import js  # type: ignore


def test_func():
    print('Test Success!')


js.testFunc = test_func

ltk.inject_script('testFunc()')


# from pyscript import document
# import js
# from js import Object as o
#
# options = o(
#     filename='cards.pdf',
#     image=o(type='png'),
#     jsPDF=o(orientation='landscape')
# )
# js.html2pdf(document.body, options)


def create_pdf(evt):
    from js import Object as o, document, openPDF  # type: ignore

    card.name('Awesome Attack').atype('Feat 20').reset_class()

    options = o(
        filename='cards.pdf',
        image=o(type='png'),
        jsPDF=o(orientation='landscape')
    )

    doc = document.implementation.createHTMLDocument()
    with open(CSS) as css:
        element('style').text(css.read()).appendTo(doc.head)
    div('cardbox').append(*[
        Card('skill') if i == 3 else
        Card().name('Awesome Slide').atype('Feat 18') if i == 1 else
        Card() for i in range(5)
    ]).appendTo(doc.body)
    openPDF(doc.documentElement, options)


ltk.Button('Generate A PDF?', create_pdf).appendTo(ltk.window.document.body)
