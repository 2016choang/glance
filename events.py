from eventregistry import *
from datetime import datetime, timedelta

def queryKeywords(client, keywords):
	timeNow = datetime.utcnow()
	timeRange = timedelta(days=1)
	timeStart = timeNow - timeRange

	uriList = []
	for keyword in keywords:
		uri = client.getConceptUri(keyword)
		uriList.append(uri)


	q = QueryArticlesIter( 
						dateStart=timeStart,
						lang="eng",
						conceptUri=QueryItems.OR(uriList)
						)
	
	q.setRequestedResult(RequestArticlesInfo(page=1, count=20, sortBy="rel",
		returnInfo=ReturnInfo(articleInfo=ArticleInfoFlags(concepts=True, categories=True, image=True))))


	response = client.execQuery(q)
		
	articles = response["articles"]["results"]

	for article in articles:
		print(article["title"])

def main():
	client = EventRegistry(apiKey="4c927d75-f35a-4646-910a-9f071768c8b1")
	keywords = ["google"]
	queryKeywords(client, keywords)

main()