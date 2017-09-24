import sys
from google.cloud import language

def get_entities(client, text):
    document = language.types.Document(
        content=text,
        language='en',
        type='PLAIN_TEXT'
    )

    resp = client.analyze_entities(
        document=document,
        encoding_type='UTF32'
    )

    return resp.entities
    
def get_keywords(client, entities):
    keywords = []
    for entity in entities[:20]:
        # print('---------')
        # print('name: {0}'.format(entity.name))
        # print('name: {0}'.format(entity.type))
        # print('name: {0}'.format(entity.metadata))
        # print('name: {0}'.format(entity.salience))
        keywords.append(entity.name)
    return keywords
    
def main():
    client = language.LanguageServiceClient()
    text = sys.stdin.read()
    entities = get_entities(client, text)
    keywords = get_keywords(client, entities)
    print(keywords)
 
if __name__=='__main__':
    main()