## Trying to wright an snippets to download automatically all files from 
##  selected series...

# Target Url: http://www.radyocihan.com/archive/list/minberden-yuekselen-ses-9

import urllib2 # Library to control urls.

response = urllib2.urlopen("http://www.radyocihan.com")

print response.info()
# Date: Mon, 09 Feb 2015 00:10:52 GMT
# Server: Apache/2.2.22 (Ubuntu)
# X-Powered-By: PHP/5.3.10-1ubuntu3.15
# Set-Cookie: radyocihan=8v8ugv96rl2tcs7hf2i885tve0; path=/
# Expires: Thu, 19 Nov 1981 08:52:00 GMT
# Cache-Control: no-store, no-cache, must-revalidate, post-check=0, pre-check=0
# Pragma: no-cache
# Set-Cookie: radyocihan=n9q8ssjf9v3pvgptqrm93ecps5; path=/
# Vary: Accept-Encoding
# Connection: close
# Transfer-Encoding: chunked
# Content-Type: text/html

  