def get_page(url): 
	try: 
		from urllib.request import urlopen
		f = urlopen(url)
		myfile = f.read()
		return (myfile)
	except: 
		return " "

def get_links(page):
	start_link = page.find('<a href=')
	if start_link == -1:	 #if there are no links
		url = None
		end_quote = 0
		return url, end_quote
	start_quote = page.find('"', start_link)
	end_quote = page.find('"', start_quote+1)
	url = page[start_quote+1 : end_quote]
	return url, end_quote

def print_links(page):
	while True:
		url, endpos = get_links(page)
		if url:
			print (url)
			page = page [endpos:]
		else:
			break 


print_links(str(get_page('https://xkcd.com/')))
