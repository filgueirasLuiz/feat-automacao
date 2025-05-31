from twilio.rest import Client

account_sid = 'AC534c31c33c3f33846edc8c275db78b2b'
auth_token = 'b86876ead9404c26570a731e4c62b036'
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='whatsapp:+14155238886',  # Número do Sandbox do WhatsApp do Twilio
    body='Olá! Testando integração!',
    to='whatsapp:+5511999999999'     # Seu número verificado (E.164 format)
)

print(message.sid)