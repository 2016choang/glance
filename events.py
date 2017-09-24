from eventregistry import *
from datetime import datetime, timedelta

def getArticles(client, company, keywords, quota):

	concepts = client.suggestConcepts(company, ["org"])
	companyUri = ""
	if concepts:
		companyUri = concepts[0]["uri"]

	timeNow = datetime.utcnow()
	timeRange = timedelta(days=7)
	timeStart = timeNow - timeRange

	uriList = []
	for keyword in keywords:
		uri = client.getConceptUri(keyword)
		uriList.append(uri)

	uriListIndex = 0;
	articleCount = 0;
	articles = []

	while articleCount != quota and uriListIndex < len(uriList):
		conceptList = [companyUri, uriList[uriListIndex]]
		print(conceptList)

		q = QueryArticlesIter( 
						dateStart=timeStart,
						lang="eng",
						conceptUri=QueryItems.AND(conceptList)
						)
		q.setRequestedResult(RequestArticlesInfo(page=1, count=3, sortBy="rel",
			returnInfo=ReturnInfo(articleInfo=ArticleInfoFlags(concepts=True, categories=True, image=True))))
		
		response = client.execQuery(q)

		if "articles" in response :
			articleCount += response["articles"]["count"]
			currentArticles = response["articles"]["results"]

			for article in currentArticles :
				articles.append(article)

		uriListIndex+=1

	return articles

def main():
	client = EventRegistry(apiKey="4c927d75-f35a-4646-910a-9f071768c8b1")
	company = "google"
	keywords = ["deepmind", "apple", "home", "AI", "phone"]
	articleQuota = 10;
	articles = getArticles(client, company, keywords, articleQuota)

	for article in articles:
		print("------------------------Article------------------------")
		print("Title: ", article["title"])
		print("Date: ", article["date"])
		print("Time: ", article["time"])
		print("URL: ", article["url"])
		print("Source: ", article["source"])

if __name__=='__main__':
	main()