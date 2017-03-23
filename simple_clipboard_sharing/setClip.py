#!/usr/bin/env python
import clipboard
import requests
r = requests.post('https://script.google.com/macros/s/{{your end point}}/exec', data = {'k':'{{your very own very strong password}}', 'cp':clipboard.get()})
print r
