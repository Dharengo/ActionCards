import cards
from pyscript.web import page, when, div, link, button, wrap_dom_element as wrap  # type: ignore

def _card_css():
    return link(rel='stylesheet', href='card.css')


def create_pdf():
    from js import Object as o, document, openPDF  # type: ignore


    options = o(
        filename='cards.pdf',
        image=o(type='png'),
        jsPDF=o(orientation='landscape')
    )

    doc = document.implementation.createHTMLDocument()
    wrap(doc.head).append(_card_css())
    wrap(doc.body).append(
        div(*[
            cards.Card(classes='skill').actioncost(cards.ACT2) if i == 3 else
            cards.Card().name('Awesome Slide').atype('Feat 18').actioncost(cards.ACT0) if i == 1 else
            cards.Card() for i in range(5)],
            classes='cardbox'
        )
    )
    openPDF(doc.documentElement, options)

def _init():
    page.head.append(_card_css())
    page.body.innerHTML = ''
    page.append(card := cards.Card(classes='skill').actioncost(cards.ACTR),
                pdfbtn := button('Generate A PDF?'))

    @when('click', pdfbtn)
    def pdfbtn_click():
        card.name('Awesome Attack').atype('Feat 20').actioncost(cards.ACT3).reset_class()
        create_pdf()


if __name__ == '__main__':
    _init()
