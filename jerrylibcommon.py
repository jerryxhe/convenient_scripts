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
