syntaxnet_root_dir = "/Users/jerryhe/dev/models/syntaxnet/syntaxnet/models/parsey_universal"

import subprocess
def tag(sent, _cmd = '{0}/syntaxnet/models/parsey_universal/parse.sh {0}/Danish'.format(syntaxnet_root_dir)):
    read, write = os.pipe()
    os.write(write, sent)
    os.close(write)
    _ans = str(subprocess.check_output(_cmd, shell=True,stdin=read))
    os.close(read)
    return _ans
