!/usr/bin/env python3
import html

def html_remove(text):
    for ent,repla in html.entities.html5.items():
        if ent in text:
            text=text.replace('&'+ent+';', repla)
    return text.replace('&#39;', "'")

import string
def remove_punct(word, _punkts=string.punctuation):
    return "".join(c for c in word if c not in _punkts)

from bs4 import BeautifulSoup
def remove_html(_text):
    return BeautifulSoup(_text, "lxml").text
