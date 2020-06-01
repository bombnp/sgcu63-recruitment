from bs4 import BeautifulSoup
import urllib
import json
from json2html import *

baans = json.load(open("Prob#1 - The Scraper\data.json"))["baans"]

tableData = []

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
	# additional idea: added description
	baanDescription = ""
	for content in soup.find("h3").next_sibling.next_sibling.contents:
		if str(content) == "<br/>":
			baanDescription += "\n"
		else:
			baanDescription += str(content)

	tableData.append({
		"name": baanName,
		"slogan": baanSlogan,
		"description": baanDescription
	})
	print(baan)


with open(r"Prob#1 - The Scraper\table.html", "w+", encoding="utf8") as htmlFile:
	htmlFile.write(json2html.convert(json=tableData).replace("\n", "<br/>"))
	