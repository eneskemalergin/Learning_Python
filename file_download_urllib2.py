# Let's create a function that downloads a file, and saves it locally.
# Info needed:
# file name
# read/write mode
# base url

def download(file_name,file_mode,base_url):
        import os
        os.chdir("C:\Users\Pc-41\Downloads\Minberden Yukselen Ses")
        
	from urllib2 import Request, urlopen, URLError, HTTPError
	
	#create the url and the request
	url = base_url + file_name
	
	# Makes the request.
	req = Request(url)
	
	# Open the url
	try:
		f = urlopen(req)
		print "downloading " + url
		
		# Open our local file for writing
		local_file = open(file_name, "w" + file_mode)
		
		#Write to our local file
		local_file.write(f.read())
		local_file.close()
		
	#handle errors
	except HTTPError, e:
		print "HTTP Error:",e.code , url
	except URLError, e:
		print "URL Error:",e.reason , url


# Set the range of images to 1-50.It says 51 because the 
# range function never gets to the endpoint.
image_range = range(1,51)

# Iterate over image range
for index in image_range:
	
	base_url = 'http://www.radyocihan.com/archive/list/minberden-yuekselen-ses-9'
	#create file name based on known pattern 
	file_name =  str(index) + ".mp3"
	# Now download the image. If these were text files, 
	# or other ascii types, just pass an empty string 
	# for the second param ala download(file_name,'',base_url)
	download(file_name,"b",base_url)