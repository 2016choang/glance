from eventregistry import *
import requests
import json
from lxml import html

def getERClient():
    return EventRegistry(apiKey="57cdfe2e-ea66-42c1-a00d-83a1e0e6f9a6")

def getWiki(client, company):
    concepts = client.suggestConcepts(company, ["org"])
    if concepts:
        wiki_param = concepts[0]["uri"].split("/")[-1]
    print('Company wikipedia page:', wiki_param)
    request ='''https://en.wikipedia.org/w/api.php?action=parse&page={}&prop=text&format=json'''.format(wiki_param)

    r = requests.get(request)
    body_html = r.json()["parse"]["text"]["*"]
    body = html.document_fromstring(body_html).text_content()
    print('Parsed wikipedia page')
    return body

def main():
    er = getERClient()
    getWiki(er, "delta")

if __name__ == "__main__":
    main()