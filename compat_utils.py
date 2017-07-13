import sys

def get_py_version(_version=None):
	if _version is None:
		#import sys
		_version = sys.version_info.major
	return _version

def first_exist(*args):
    for o in args:
        try:
            return o
        except NameError:
            pass
          
import html
char2html = {'&':'&amp;'} if get_py_version()==2 else {}

import string,re
def regex_escape(char,_unicode=first_exist(unicode, str)):
    if char.isspace():
        return u"(\\s+|\\&nbsp\\;)?"
    if char in ['&']:
        return u"".join([u"(\\W+)?",u"(\\",char,u"|",char2html[char],u")",u"(\\W+)?"])
    if char=="*":
        return u".*"
    if char==".":
        return u"(.?)"
    if char=="'":
        return u"\\'"
    return _unicode(char).decode("utf-8")

def insentence(w, sentence,_unicode=first_exist(unicode, str)):
    w = w.strip().strip("'") # get rid of unnecessary quotes
    try:
        fin = w.index("(")
        w = w[:fin]
    except Exception as e:
        pass
    w= _unicode(u"".join(map(regex_escape, w.replace(")",""))))
    return len(re.findall(u"\\b%s\\b" % w, _unicode(sentence),
                      re.UNICODE | re.IGNORECASE | re.MULTILINE))>0
