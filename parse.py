import pickle
from pathlib import Path
from wiki import *
from nlp import *

def getData(path):
    if Path(path).is_file():
        print('Pickle file exists, opening')
        return pickle.load(open(path, 'rb'))
    else:
        print('Pickle file doesn\'t exist, creating')
        return {}   

def parseCompanies(er_client, language_client, data, companies):
    for company in companies:
        if company not in data:
            body = getWiki(er_client, company)
            entities = getEntities(language_client, body)
            keywords = getKeywords(language_client, entities, 50)
            data[company] = keywords
            print('Parsed', company)
            just_keys = [x[0] for x in keywords]
            print('  Keywords:', just_keys)
        else:
            print('Company', company, 'already in data')

    return data

def saveData(path, data):
    print('Saved data to pickle')
    pickle.dump(data, open(path, 'wb'))

def main():
    er_client = getERClient()
    language_client = getLanguageClient()

    companies = ['apple', 'microsoft','google','amazon',
        'facebook','samsung', 'verizon','at&t']
    data = getData('data.pickle')

    data = parseCompanies(er_client, language_client, data, companies)
    saveData('data.pickle', data)

if __name__=='__main__':
    main()
