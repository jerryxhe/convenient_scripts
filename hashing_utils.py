__author__ = "Jerry He"
import zlib,sys

def crc32_hash_py2(st):
    return zlib.crc32(unicode(st)) & 0xffffffff
    
def crc32_hash_py3(st):
    return zlib.crc32(str(st).encode("utf-8")) & 0xffffffff
    
crc32_hash = crc32_hash_py2 if sys.version[0]=='2' else crc32_hash_py3

__all__ = ['crc32_hash']
