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

	articleQuota = 10

	for company in companies:
		keywords = data[company]
<<<<<<< HEAD
		for keyword, salience in keywords:
			pairing = [company, keyword]
			articles = getArticles(er_client, pairing, 1)
			if articles:
				for article in articles:
					message_body = ''
					message_body += '------------------------Article------------------------' + '\n'
=======
		articles = getArticles(er_client, company, keywords, articleQuota)
		message_Body = "----------" + company + "----------"
		message = sendMessage(twilio_client, number_from, number_to, message_body)

		if articles:
			for article in articles:
					message_body = ""
					message_body += '----------Article----------' + '\n'
>>>>>>> 9bcebb3f300c675d4cc68947c2266aa7ecfc69af
					message_body += "Title: " + article["title"] + '\n'
					message_body += "Date: " + article["date"] + '\n'
					message_body += "Time: " + article["time"] + '\n'
					message_body += "URL: " + article["url"] + '\n'
					message = sendMessage(twilio_client, number_from, number_to, message_body)

if __name__ == "__main__":
    main()
