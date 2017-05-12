# a collection of useful functions

def flatten_dict_iter(dic):
    for k,v in dic.iteritems():
        if isinstance(v, int):
            yield k,v
        elif isinstance(v,basestring):
            v = v.replace("-","")
            yield k+" "+v, 1
        elif isinstance(v,dict):
            for u, w in flatten_dict(v):
                yield (k+" "+u).replace("-",""), w
        elif isinstance(v, bool):
                yield k, int(v)
    
def condense_attributes(dic):
    return dict(flatten_dict_iter(dic))


from time import sleep
from datetime import datetime, timedelta
def smart_sleep(nseconds):
    """a sleep function that guards against computer falling asleep and rewaking and a later time"""
    terminal_time = datetime.now() + timedelta(seconds=(nseconds+10))
    while(datetimenow() < terminal_time):
        sleep(120)
