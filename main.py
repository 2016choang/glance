from wiki import *
from nlp import *
from events import *
from sms import *


def main():
	er_client = getERClient()
	text = getWiki(er_client, 'apple')
	language_client = getLanguageClient()
	entities = getEntities(language_client, text)
	keywords = getKeywords(language_client, entities, 5)

	twilio_client = getTwilioClient()
	number_from = "+14804000465"
	number_to = "+14806944346"

	for keyword in keywords:
		pairing = ['apple', keyword]
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
