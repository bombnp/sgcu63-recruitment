from bs4 import BeautifulSoup
import urllib
import json
from json2html import *

data = json.load(open("Prob#1 - The Scraper\data.json"))
baans = data["baans"]

tableData = {}

for baan in baans:
	url = "https://rubnongkaomai.com/baan/" + baan
	html = urllib.request.urlopen(url).read()

	soup = BeautifulSoup(html, "html.parser")
	baanName = str(soup.find("h1").next)
	baanSlogan = ""
	for content in soup.find("h3").contents:
		if str(content) == "<br/>":
			baanSlogan += "\n"
		else:
			baanSlogan += str(content)

	tableData[baanName] = baanSlogan
	print(baan)


with open(r"Prob#1 - The Scraper\table.html", "w+", encoding="utf8") as htmlFile:
	htmlFile.write(json2html.convert(json=tableData).replace("\n", "<br/>"))
	