from parse import *
from events import *
from sms import *


def main():
	er_client = getERClient()
	language_client = getLanguageClient()
	companies = ['apple', 'microsoft','google','amazon',
        'facebook','samsung', 'verizon','at&t']

	data_path = 'data.pickle'
	data = getData(data_path)
	data = parseCompanies(er_client, language_client, data, companies)
	saveData(data_path, data)

	twilio_client = getTwilioClient()
	number_from = "+14804000465"
	number_to = "+14806944346"

	for company in companies:
		keywords = data[company]
		for keyword in keywords:
			pairing = [company, keyword]
			articles = getArticles(er_client, pairing, 1)
			if articles:
				for article in articles:
					message_body = ''
					message_body += '------------------------Article------------------------' + '\n'
					message_body += "Title: " + article["title"] + '\n'
					message_body += "Date: " + article["date"] + '\n'
					message_body += "Time: " + article["time"] + '\n'
					message_body += "URL: " + article["url"] + '\n'
					message = sendMessage(twilio_client, number_from, number_to, message_body)

if __name__ == "__main__":
    main()
