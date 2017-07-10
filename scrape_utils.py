!/usr/bin/env python3
import html

def html_remove(text):
    for ent,repla in html.entities.html5.items():
        if ent in text:
            text=text.replace('&'+ent+';', repla)
    return text.replace('&#39;', "'")
