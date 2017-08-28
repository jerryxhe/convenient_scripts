def wget(url):
	import urllib
	return urllib.urlopen(url).read()

import re,string
def replace_amp(text,ampersand = re.compile(r'&(\s+)?amp(\s+)?;?', re.I | re.U)):
    arr = filter(lambda st: st!='', map(string.strip, filter(None, ampersand.split(text, 0))))
    return '&'.join(arr)

class NameStemmer:
	def __init__(self):
		self.redundant_suffixes = ['Group', 'International','plc', "Ltd", "AG", "Limited", "Ltd", "Inc"]
		_replacements = {'Pharmaceutical':'(Ph|F)arma', 
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
			_patterns[re.compile('.*?\\b'+k+'(s|\.)?'+'\\b.*?', re.I|re.U)]=v
		self.patterns = _patterns
		self.split_regex = re.compile(r'\W+')
	def stem(self, companyname):
		name = companyname
		name = name.split(",")[0].strip()
		name = name.split("(")[0].strip()
		name_arr = self.split_regex.split(name)
		for i in range(len(name_arr)):
			for pat,v in self.patterns.items():
				if pat.match(name_arr[i]):
						name_arr[i]=pat.sub(v, name_arr[i])
		print name_arr
		return "\\W+".join(filter(lambda st:len(st.strip())>0, name_arr))
