import events.py
import nlp.py

def main() :

	client = EventRegistry(apiKey="4c927d75-f35a-4646-910a-9f071768c8b1")
	keywords = "Google";
	queryKeywords(client)

if __name__ == "__main__":
    main()
