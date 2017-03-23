#!/usr/bin/env python
# -- clipboard.py
# for Mac OS X only!!

import subprocess 
def get(): 
	p = subprocess.Popen(['pbpaste'], stdout=subprocess.PIPE) 
	# retcode = p.wait() 
	data = p.stdout.read()
	return data
	
def set(data): 
	p = subprocess.Popen(['pbcopy'], stdin=subprocess.PIPE)
	p.stdin.write(data) 
	p.stdin.close() 
	retcode = p.wait()
	return retcode
