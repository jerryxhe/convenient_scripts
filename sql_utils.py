#!/usr/bin/env python

def psql_create_syntax(tablename, dbname):
    import subprocess
    output = subprocess.check_output("pg_dump -t \"public.{}\" --schema-only {}".format(tablename,dbname), shell=True)
    st = output.index("CREATE TABLE")
    return output[st:]
  
