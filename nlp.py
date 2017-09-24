import sys
from google.cloud import language

def get_language_client():
    print("Created language client")
    return language.LanguageServiceClient()

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
    print("Obtained entities")
    return resp.entities
    
def get_keywords(client, entities):
    keywords = [entity.name for entity in entities[:20]]
    print("Obtained keywords")
    return keywords
    
def main():
    text = sys.stdin.read()
    client = get_language_client()
    entities = get_entities(client, text)
    keywords = get_keywords(client, entities)
    print(keywords)
 
if __name__=='__main__':
    main()