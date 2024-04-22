from twilio.rest import Client

account_sid = 'ACdc0cc880c06289995d56b0e9b7908c8c'
auth_token = '6436c5c349b0281ceac0b06ab4c7e65f'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from ='+12513222845',
  body ='This SMS was sent using Python',
  to = """Write your Phone Number here"""
)

print(message.sid)