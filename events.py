from eventregistry import *
from datetime import datetime, timedelta

def getArticles(client, keywords, count):
	timeNow = datetime.utcnow()
	timeRange = timedelta(days=7)
	timeStart = timeNow - timeRange

	uriList = []
	for keyword in keywords:
		uri = client.getConceptUri(keyword)
		uriList.append(uri)


	q = QueryArticlesIter( 
						dateStart=timeStart,
						lang="eng",
						conceptUri=QueryItems.AND(uriList)
						)
	
	q.setRequestedResult(RequestArticlesInfo(page=1, count=count, sortBy="rel",
		returnInfo=ReturnInfo(articleInfo=ArticleInfoFlags(concepts=True, categories=True, image=True))))


	response = client.execQuery(q)

	articles = None

	if "articles" in response :
		articles = response["articles"]["results"]

	return articles

def main():
	client = EventRegistry(apiKey="4c927d75-f35a-4646-910a-9f071768c8b1")
	keywords = ["google", "deepmind"]
	articleCount = 20;
	articles = getArticles(client, keywords, articleCount)

	for article in articles:
		print("------------------------Article------------------------")
		print("Title: ", article["title"])
		print("Date: ", article["date"])
		print("Time: ", article["time"])
		print("URL: ", article["url"])
		print("Source: ", article["source"])

if __name__=='__main__':
	main()