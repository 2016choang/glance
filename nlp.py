import sys
from google.cloud import language

def getLanguageClient():
    print("Created language client")
    return language.LanguageServiceClient()

def getEntities(client, text):
    document = language.types.Document(
        content=text,
        language='en',
        type='PLAIN_TEXT'
    )

    resp = client.analyze_entities(
        document=document,
        encoding_type='UTF32'
    )
    print("Obtained entities")
    return resp.entities
    
def getKeywords(client, entities, count):
    keywords = [entity.name for entity in entities[:count]]
    print("Obtained keywords")
    return keywords
    
def main():
    text = sys.stdin.read()
    client = getLanguageClient()
    entities = getEntities(client, text)
    keywords = getKeywords(client, entities, 40)
    print(keywords)
 
if __name__=='__main__':
    main()