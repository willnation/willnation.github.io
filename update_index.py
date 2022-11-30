import bs4
import glob
import json

def main():
	# load the file
	site_map = json.load(open('site_map.json'))
	with open("index.html") as inf:
	    txt = inf.read()
	    soup = bs4.BeautifulSoup(txt,features="html.parser")
	glob_list = glob.glob('*.html')
	# create new link
	for g in glob_list:
		print(soup.p.string)
		if g not in list(site_map.keys()):
			tag = soup.new_tag("a", href='./' + g)
			tag.string = g.replace('.html',' ‰ ')
			soup.a.insert_before(tag)
			site_map[g] = "post"
	# insert it into the document

	# save the file again
	with open("site_map.json", "w") as fp:
		json.dump(site_map, fp) 
	with open("index.html", "w") as outf:
		outf.write(str(soup))

if __name__ == '__main__':
	main()