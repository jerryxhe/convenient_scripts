# migration script, source CouchDB must be publicly readable, this is to make the download faster if you have large attachments. 

from couchdb import Server
from couchdb.http import ResourceNotFound
from datetime import datetime
from couchdb import mapping
import requests
import os

local_tmp_dir = "/Users/me/Documents/backup/" # you must change this
dbname = 'file_backup'                        # you must change this

if not os.path.exists(local_tmp_dir):
    os.makedirs(local_tmp_dir)

def download_file(url):
	print url
	urlcomponents = url.split('/')
	local_filename = urlcomponents[-1]
	doc_id=urlcomponents[-2]
	# NOTE the stream=True parameter
	r = requests.get(url, stream=True)
	if not os.path.exists(local_tmp_dir+doc_id):
		os.makedirs(local_tmp_dir+doc_id)
	local_path = local_tmp_dir+doc_id+"/"+local_filename
	with open(local_path, 'wb') as f:
		for chunk in r.iter_content(chunk_size=1024):
			if chunk: # filter out keep-alive new chunks
				f.write(chunk)
				f.flush()
	return local_path


server2 = Server("https://{{username}}:{{password}}@xxxxxxx.cloudant.com") # you must change this
db2 = server2[dbname]

all_docs = db.view("_all_docs")

docs = [row for row in all_docs]

for doc in docs:
	doc_id = doc["id"]
	doc_content =db[doc_id]
	print doc_content
	attachments = db[doc_id]["_attachments"].items();
	db2[doc_id]={}
	for k,v in attachments:
		local_handle = download_file("https://{{source_endpoint}}.cloudant.com/"+dbname+"/"+doc_id+"/"+k) # you must change this
		db2.put_attachment(db2[doc_id], file(local_handle), filename=None, content_type=None)
	
