import os
def file_size(fpath):
  return os.stat(fpath).st_size
