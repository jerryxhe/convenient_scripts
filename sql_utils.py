#!/usr/bin/env python

def psql_create_syntax_py2(tablename, dbname):
    import subprocess
    output = subprocess.check_output("pg_dump -t \"public.{}\" --schema-only {}".format(tablename,dbname), shell=True)
    st = output.index("CREATE TABLE")
    return output[st:].replace('\\n', '\n')
  
def psql_create_syntax_py3(tablename, dbname='intellect'):
    import subprocess
    output = str(subprocess.check_output("pg_dump -t \"public.{}\" --schema-only {}".format(tablename,dbname), shell=True))
    st = output.index("CREATE TABLE")
    return output[st:].replace('\\n', '\n')

def camelcase_2_underscore(name):
    """PostgreSQL does not like upper case"""
    return "".join(c.isupper() and ("_"+c.lower()) or c
           for c in name)   

class CaseConversion:
    import re
    def __init__(self):
        self._pattern = re.compile(r'\_(?P<char>.)',re.I)
    
    def camelcase_2_underscore(self, name):
        """PostgreSQL does not like upper case"""
        return "".join(c.isupper() and ("_"+c.lower()) or c
               for c in name)

    def underscore_2_camelcase(self, name):
        return self._pattern.sub(lambda mat:mat.groupdict()['char'].upper(),name)
