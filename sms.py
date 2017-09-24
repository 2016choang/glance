from twilio.rest import Client

def get_twilio_client():
    account="ACe21476c227f42ea6835905e4413ba052"
    token="716e6f84b182da55d61aa01998be7411"
    print("Created Twilio client")
    return Client(account, token)

def send_message(client, number_from, number_to, text):
    print("Sent the following message from {0} to {1}:".format(number_from, number_to))
    print(text)
    message = client.messages.create(to=number_to, from_=number_from, body=text)

def main():
    client = get_twilio_client()
    number_from = "+14804000465"
    number_to = "+14806944346"
    text = "This is a text"
    send_message(client, number_from, number_to, text)

if __name__=='__main__':
    main()