import ltk
import cards
from utils import *

CSS = 'card.css'


ltk.find('body').empty().append(card := cards.Card('skill').actioncost(cards.ACTR))
ltk.inject_css(CSS)


def create_pdf(evt):
    from js import Object as o, document, openPDF  # type: ignore

    card.name('Awesome Attack').atype('Feat 20').actioncost(cards.ACT3).reset_class()

    options = o(
        filename='cards.pdf',
        image=o(type='png'),
        jsPDF=o(orientation='landscape')
    )

    doc = document.implementation.createHTMLDocument()
    with open(CSS) as css:
        element('style').text(css.read()).appendTo(doc.head)
    div('cardbox').append(*[
        cards.Card('skill').actioncost(cards.ACT2) if i == 3 else
        cards.Card().name('Awesome Slide').atype('Feat 18').actioncost(cards.ACT0) if i == 1 else
        cards.Card() for i in range(5)
    ]).appendTo(doc.body)
    openPDF(doc.documentElement, options)


ltk.Button('Generate A PDF?', create_pdf).element.insertAfter(card.element)
