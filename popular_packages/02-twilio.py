import os
from twilio.rest import Client

sid = os.environ.get("TWILIO_SID")
token = os.environ.get("TWILIO_TOKEN")
number = os.environ.get("TWILIO_N")

client = Client(sid, token)
message = client.messages.create(
    body="Hola mundo!",
    from_=number,
    to="+525561424559"
)
