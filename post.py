import bs4
import datetime

from update_index import main as update_index

def main():

	# load the file
	with open("template.html") as inf:
	    txt = inf.read()
	    soup = bs4.BeautifulSoup(txt,features="html.parser")
	
	post = input()#This can be replaced with some 

	soup.p.string = post
	current_time = datetime.datetime.now(datetime.timezone.utc)
	current_time = current_time.strftime("%Y-%m-%d_%H%M%S")
	# insert it into the document
	soup.header.string = current_time
	soup.title.string = soup.title.string + ' ' + current_time

	# save the file again
	with open("_posts/" + current_time +".html", "w") as outf:
	    outf.write(str(soup))
	with open(current_time +".html", "w") as outf:
	    outf.write(str(soup))
	update_index()

if __name__ == '__main__':
	main()