# coding: utf-8
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

class NameStemmer:
	def __init__(self):
		_replacements = {'Pharmaceutical':'Pharma', 
		              'Biopharmaceutical':'Biopharma',
		              'Therapeutic':'Therap',
		              'Corporation':'Corp',
                'Technologie':'Techno',
                'Technology':'Techno',
                'Lab':'Lab',
                'Laboratorie':'Lab',
                'Laboratory':"Lab"}
		_patterns = {}
		import re
		for k,v in _replacements.items():
			_patterns[re.compile('.*?\\b'+k+'s?'+'\\b.*?', re.I)]=v
		self.patterns = _patterns
	def stem(self, companyname):
		name = companyname
		name = name.split(",")[0].strip()
		name = name.split("(")[0].strip()
		for pat,v in self.patterns.items():
				name = "\\W+".join([pat.sub(v, subname) for subname in name.split(" ")])
		return name
