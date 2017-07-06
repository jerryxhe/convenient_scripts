__author__ = "Jerry He"
import zlib,sys

def crc32_hash_py2(st):
    return zlib.crc32(unicode(st)) & 0xffffffff
    
def crc32_hash_py3(st):
    return zlib.crc32(str(st).encode("utf-8")) & 0xffffffff
    
crc32_hash = crc32_hash_py2 if sys.version[0]=='2' else crc32_hash_py3

def iter_xls_cols():
    """yields a-z then aa ab ... aaa aab ..."""
    from itertools import product,count
    from string import ascii_lowercase
    for size in count(1):
        for let in product(ascii_lowercase, repeat=size):
            yield "".join(let)

__all__ = ['crc32_hash','iter_xls_cols']
