from eventregistry import *
import sys
import requests
import json
from lxml import html

def getWiki(client, company):
    #uri = client.getConceptUri(company)
    concepts = client.suggestConcepts(company, ["org"])
    if concepts:
        wiki_param = concepts[0]["uri"].split("/")[-1]

    request ='''https://en.wikipedia.org/w/api.php?action=parse&page={}&prop=text&format=json'''.format(wiki_param)

    r = requests.get(request)
    body_html = r.json()["parse"]["text"]["*"]
    body = html.document_fromstring(body_html).text_content()

    return body

def main():
    er = EventRegistry(apiKey="4c927d75-f35a-4646-910a-9f071768c8b1")
    print(getWiki(er, "apple"))

if __name__ == "__main__":
    main()