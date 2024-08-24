import ltk

def element(tag, cls=''):
    return ltk.create(f'<{tag}>').addClass(cls)


def div(cls=''):
    return element('div', cls)


def span(cls=''):
    return element('span', cls)