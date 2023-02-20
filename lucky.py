# import necessary modules 
import requests, sys, webbrowser, bs4

# request a page
print("Googling...") #Displays text while downloading the Google page
res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:])) 
res.raise_for_status()

# Retrieve top search result links
soup = bs4.BeautifulSoup(res.text, features='html.parser') 
linkElems = soup.select('.r a')

# Open a browser tab for each search result
numOpen = min(5, len(linkElems))
for i in range(numOpen): 
    webbrowser.open('http://google.com' + linkElems[i].get('href')) 
