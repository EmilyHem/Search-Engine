def get_page(url):							 #gets html source of a webpage
	try: 
		from urllib.request import urlopen
		f = urlopen(url)
		myfile = f.read()
		return (myfile)
	except: 
		return " "

def get_links(page): 							#gets the links on a given page 
	start_link = page.find('<a href=')
	if start_link == -1:						#if there are no links
		url = None
		end_quote = 0
		return url, end_quote
	start_quote = page.find('"', start_link)
	end_quote = page.find('"', start_quote+1)
	url = page[start_quote+1 : end_quote]
	return url, end_quote

def print_links(page):							#prints the links on a given page
	while True:
		url, endpos = get_links(page)
		if url:
			print (url)
			page = page [endpos:]
		else:
			break 

index = []

def add_to_index (index, keyword, url): 				#adds url to index corresponding to a keyword	
	for entry in index:						#if there is an existing keyword entry add as an additional url 
		if entry[0]==keyword:
			entry[1].append(url)
			return
	index.append([keyword,[url]])					#if no matching entry found; create new entry

def lookup(index, keyword):						#look ups keyword in index and returns corresponding urls 
	for entry in index:
		if entry[0]==keyword:
			return entry[1]
	return []							#if no url is found return an empty array

def add_page_to_index (index, url, content):				#splits content into an array of words
	words = content.split()
	for word in words:
		add_to_index(index, word, url)				

def crawl(seed):							#crawls the web given a seed webpage
	tocrawl =[seed]
	crawled=[]
	index=[]
	while tocrawl:
		page =tocrawl.pop()
		if page not in crawled:
			content=get_page(page)
			add_page_to_index(index, page, content)
			union(tocrawl, get_links(context))
			crawled.append(page)
	return index
	
print_links(str(get_page('url')))

