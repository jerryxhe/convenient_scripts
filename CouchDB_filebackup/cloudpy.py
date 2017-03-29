#!/usr/bin/env python
# -- stores files into CouchDB server, which is great because CouchDB stores every version
import os
from couchdb import Server
from couchdb.http import ResourceNotFound

server = Server("https://{{username}}:{{password}}@xxxxxxx.cloudant.com")
db = server['file_backup']

def storeFile(filepath):
	filehandle=open(filepath,'r')
	filename = filehandle.name
	doc = {"_id":filename, "modified":os.path.getmtime(filepath), "path":os.getcwd()+filepath}
	try:
		doc['_rev']=db[filename]['_rev']
	except ResourceNotFound as e:
		pass
	db.save(doc)
	db.put_attachment(doc, filehandle)	
	
def getFile(filename):
	f=db.get_attachment(filename, filename)
	file(filename, 'w').write(f.read())
	
def storeDir(dir_name):
	zip(dir_name)
	storeFile(dir_name+'.zip')
	
def getDir(dir_name):
	getFile(dir_name+'.zip')
	unzip(dir_name+'.zip')
	os.remove(dir_name+'.zip')
	
if __name__=="__main__":
	storeFile('cloudpy.py')
