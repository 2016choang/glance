import sys
from parse import *
from events import *
from stocks import *
from sms import *


def main():
	er_client = getERClient()
	language_client = getLanguageClient()
	# companies = ['apple', 'microsoft','google','amazon',
    #     'facebook','samsung', 'verizon','at&t']
	# ticker_dict = {'apple': 'AAPL', 'microsoft':'MSFT', }
	
	articleQuota = int(sys.argv[1])
	companies = sys.argv[2:]

	data_path = 'data.pickle'
	data = getData(data_path)
	data = parseCompanies(er_client, language_client, data, companies)
	saveData(data_path, data)

	twilio_client = getTwilioClient()
	number_from = "+14804000465"
	number_to = "+14806944346"

	articlePool = []
	companyArticleCount = 5

	for company in companies:
		keywords, salience  = zip(*data[company])
		articles = getArticles(er_client, company, keywords, companyArticleCount)
		if articles:
			for article in articles:
				importance = 100
				if article["source"]:
					if 'ranking' in article["source"]:
						if 'importanceRank' in article["source"]["ranking"]:
							importance = article["source"]["ranking"]["importanceRank"]
				articlePool.append((importance, article, company))

	articlePool = sorted(articlePool, key=lambda x: x[0])
	
	# for importance, article, company in articlePool:
	# 	print(importance, article['url'], company)

	for importance, article, company in articlePool[:articleQuota]:
		message_body = "\n"
		stock = getStock(company, article['date'])
		message_body += "----------Article----------" + '\n'
		message_body += "Company: " + company + '\n'
		message_body += "Stock: " + str(stock) + '\n'
		message_body += "Title: " + article["title"] + '\n'
		message_body += "Date: " + article["date"] + '\n'
		message_body += "Time: " + article["time"] + '\n'
		message_body += "URL: " + article["url"] + '\n'
		message = sendMessage(twilio_client, number_from, number_to, message_body)

if __name__ == "__main__":
    main()
