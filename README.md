📲 Feat Suítes - Assistente Virtual no WhatsApp
Este projeto é um chatbot simples feito em Python usando Flask e Twilio para responder automaticamente a mensagens do WhatsApp. Ele simula um assistente virtual para um motel chamado Feat Suítes, oferecendo opções como ver suítes disponíveis, valores e falar com um atendente.

🚀 Tecnologias utilizadas
Python 3

Flask

Twilio WhatsApp API

💡 Funcionalidades
O chatbot responde às seguintes opções:

1️⃣ Ver suítes disponíveis

2️⃣ Falar com um atendente

3️⃣ Ver valores das suítes

menu Repetir as opções

Exemplo de mensagem:
menu
1
2
3
🛠️ Como usar
Clone o repositório:
git clone https://github.com/seu-usuario/automacao-whatsapp.git

Acesse a pasta:
cd automacao-whatsapp

Crie um ambiente virtual (opcional, mas recomendado):
python -m venv env
.\env\Scripts\activate # no Windows

Instale as dependências:
pip install flask twilio

Execute o servidor Flask:
python app.py

Inicie um túnel com o ngrok:
./ngrok http 5000

Configure seu webhook no painel da Twilio com a URL fornecida pelo ngrok, ex:
https://abcd-1234.ngrok.io/webhook

Envie uma mensagem para o número do WhatsApp Sandbox da Twilio e interaja com o bot!

📞 Exemplo de envio de mensagem via código
O código também inclui um exemplo de envio de mensagem pelo client da Twilio:

python
Copiar
Editar

Substitua SEU_SID, SEU_TOKEN e SEU_NUMERO com suas credenciais e número verificado.
