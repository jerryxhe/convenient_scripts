# a collection of useful functions

def get_py_version(_version=None):
    if _version is None:
        import sys
        _version=sys.version_info.major
    return _version

def first_of(iterator_, condition_):
    for item in iterator_:
        try:
            if condition_(item):
                return item
        except Exception as e:
            pass

def batch_iter(my_iter, num_per_batch=20, limit=None):
    from itertools import islice
    start_index =0
    while start_index<limit:
        try:
            yield [row for row in islice(my_iter,num_per_batch)]
            start_index += num_per_batch
        except StopIteration as e:
            return []

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
    while(datetime.now() < terminal_time):
        sleep(120) # check every 2 minutes

def do_shell(args): # convenience function to do run commandline stuff
    """automatic retries"""
    from subprocess import check_output,CalledProcessError
    if isinstance(args, str):
        args = args.split(" ")
    n_failed = 0
    while n_failed < 20:
        try:
            return check_output(args)
        except CalledProcessError as e:
            sleep(4)
             n_failed +=1
            print("Shell cmd failed with ",args)
