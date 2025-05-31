from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/webhook", methods=['POST'])
def whatsapp_webhook():
    incoming_msg = request.values.get('Body', '').strip().lower()
    resp = MessagingResponse()
    msg = resp.message()

    if 'menu' in incoming_msg or 'oi' in incoming_msg or 'olá' in incoming_msg:
        response = (
            "🏩 Bem-vindo ao Assistente Virtual da Feat Suítes!\n"
            "Como posso te ajudar?\n\n"
            "1️⃣ - Ver suítes disponíveis\n"
            "2️⃣ - Falar com atendente\n"
            "3️⃣ - Ver valores das suítes\n\n"
            "Digite o número da opção ou 'menu' para repetir."
        )
    elif incoming_msg == '1':
        response = (
            "🛏️ Suítes disponíveis no momento:\n"
            "- Suíte Luxo\n"
            "- Suíte Master\n"
            "- Suíte Temática\n\n"
            "Digite 'menu' para voltar."
        )
    elif incoming_msg == '2':
        response = (
            "📞 Um atendente será chamado para te atender em instantes.\n"
            "Digite 'menu' para voltar."
        )
    elif incoming_msg == 'suítes' or incoming_msg == 'Valor' or incoming_msg == '3':
        response = (
            "💰 Valores das suítes (3 horas):\n"
            "- Suíte Luxo: R$ 120,00\n"
            "- Suíte Master: R$ 180,00\n"
            "- Suíte Temática: R$ 220,00\n\n"
            "Digite 'menu' para voltar." 
        )
    else:
        response = (
            "❓ Desculpe, não entendi sua mensagem.\n"
            "Digite 'menu' para ver as opções novamente."
        )

    msg.body(response)
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
