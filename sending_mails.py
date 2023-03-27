import requests
import os

def send_simple_message():
	return requests.post(
		"https://api.mailgun.net/v3/sandboxeb51d933c6d8471f8957d35237426477.mailgun.org/messages",
		auth=("api", "a0aa784032bb887cf9cf7122b8b9cce3-30344472-bb92df6b"),
		data={"from": "Excited User <mailgun@sandboxeb51d933c6d8471f8957d35237426477.mailgun.org/messages>",
			"to": ["siddhanttyagi432@gmail.com", "YOU@sandboxeb51d933c6d8471f8957d35237426477.mailgun.org"],
			"subject": "Hello",
			"text": "Testing some Mailgun awesomness!"})


send_simple_message()