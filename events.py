from eventregistry import *

def queryKeywords(client, keywords):
	q = QueryEventsIter(conceptUri = er.getConceptUri("Google"))
	for event in q.execQuery(er, sortBy = "date"):
		print(event)
