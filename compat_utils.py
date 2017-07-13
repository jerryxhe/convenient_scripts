import sys

def get_py_version(_version=None):
	if _version is None:
		#import sys
		_version = sys.version_info.major
	return _version
