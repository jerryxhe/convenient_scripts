#!/usr/bin/env python
import clipboard
import urllib

cp = urllib.urlopen('https://script.google.com/macros/s/{{your end point}}/exec?k={{your very own very strong password}}').read()
print cp                                                                       
clipboard.set(cp)
