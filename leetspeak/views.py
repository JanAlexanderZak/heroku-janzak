import re
from typing import Dict, Pattern
from django.shortcuts import render


class LeetspeekConverter:
    TEXT: str = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    LEET: str = "4bcd3f9h1jklmn0pqr57uvwxyz4bcd3f6h1jklmn0pqr57uvwxyz"

    def __init__(self) -> None:
        self.leet_dict: Dict[str, str] = dict(zip(self.TEXT, self.LEET))

    def convert_to_leet(self, text) -> str:
        """ Hack to implement multiple re.sub on the same string in one go
        https://stackoverflow.com/questions/35713540/replace-more-than-one-pattern-python
        """
        regex: Pattern[str] = re.compile(r"(%s)" % "|".join(map(re.escape, self.leet_dict.keys())))
        return regex.sub(lambda x: self.leet_dict[x.string[x.start():x.end()]], text)


def api(request, string):
    converter = LeetspeekConverter()
    converted = converter.convert_to_leet(string)
    return render(request, "leetspeak/api.html", {
        'leet_string': converted,
    })


def index(request):
    return render(request, 'leetspeak/index.html')


def examples(request):
    _examples = ['leet', 'code']
    converter = LeetspeekConverter()
    leet_examples = [converter.convert_to_leet(example) for example in _examples]
    field = {
        'headers': [u'id', u'string', u'leet_string'],
        'rows': [[u'1', u'leet', u'l33t'],
                 [u'2', u'me', u'm3'], ], }

    return render(request, 'leetspeak/examples.html', {
        'field': field,
    })
