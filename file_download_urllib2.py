# Let's create a function that downloads a file, and saves it locally.
   
# Info needed:
# file name
# base url
# program_name
# topic_name
# file_number
# extension (default = ".mp3")
def download(base_url, program_name, topic_name, file_name, file_number, extension = ".mp3"):
        from urllib2 import Request, urlopen, URLError, HTTPError
	import os
	# Upgrade it: if there is no directory exists create one and cont...
	# directory_location =  "C:\Users\Pc-41\Desktop\H.E\ " + program_name + "\ "+ topic_name
        directory_location = "C:\Users\Pc-41\downloads\Sorular ve Cevaplar"

        os.chdir(directory_location)
        
        
	url = base_url + "%252F" + program_name + "%252F" + topic_name + "%252F" + file_name + file_number + extension
	# Makes the request.
	req = Request(url)
	
	# Open the url
	try:
		f = urlopen(req)
		print "downloading " + url
		save_name = file_name + file_number + extension
		# Open our local file for writing
		local_file = open(save_name, "w" + "b")
		
		#Write to our local file
		local_file.write(f.read())
		local_file.close()
		
	#handle errors
	except HTTPError, e:
		print "HTTP Error:",e.code , url
	except URLError, e:
		print "URL Error:",e.reason , url

# Checks the existency of a url...
# There is a bug or website that I test has a problem.
"""def exists(path):
    import requests
    r = requests.head(path)
    return r.status_code == requests.codes.ok
"""
number_list = ["%.2d" % i for i in range(62)]
for j in range(len(number_list) - 1):
    string_number = str(number_list[j])
    if string_number == "00":
        continue
    else:
        download('http://www.radyocihan.com/download/mp3/%252Fuploads%252Faudio', 'sorular-ve-cevaplar', 'birlestirilmis-s-c',
    'sorular-ve-cevaplar-', string_number, '.mp3')
print "All done!"
    
# Adding zero
str(3).zfill(2)

# Precise numbering

#Example URL:
#    http://www.radyocihan.com/download/mp3/%252Fuploads%252Faudio%252Fsorular-ve-cevaplar%252Fbirlestirilmis-s-c%252Fsorular-ve-cevaplar-41.mp3

# Example URL:
#    http://www.radyocihan.com/download/mp3/%252Fuploads%252Faudio%252Fminberden-yukselen-ses
#     %252Fmys-ahlaki-mulahazalar%252Fahlaki-mulahazalar-izmir-bornova-01.mp3
# base_url = 'http://www.radyocihan.com/download/mp3/%252Fuploads%252Faudio'
# file_name =  str(index) + ".mp3"
# download(file_name,"b",base_url)

