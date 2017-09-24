from eventregistry import *
import sys
import requests
import json

def wiki(client, company):
    uri = client.getConceptUri(company)


    print(uri)

    wiki_param = uri.split('/')[-1]

    print(wiki_param)


    request ='''https://en.wikipedia.org/w/api.php?action=query&titles={}&prop=revisions&rvprop=content&format=json'''.format(wiki_param)

    r = requests.get(request)

    with open('data.json', 'w') as fp:
        json.dump(r.json(), fp, indent=4)

def main():
    er = EventRegistry(apiKey="4c927d75-f35a-4646-910a-9f071768c8b1")
    wiki(er, "delta")

if __name__ == "__main__":
    main()