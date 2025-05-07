
Nwatch is a lightweight IP logger disguised as a ping pong game. It collects visitor data upon interaction and sends it to a Discord webhook.

⚙️ Setup
Clone the repo:

bash
Copy
Edit
git clone https://github.com/Zenxoxz/nwatch.git
cd nwatch
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Configure webhook:

Edit config.py and set your Discord webhook URL:

python
Copy
Edit
WEBHOOK_URL = 'https://discord.com/api/webhooks/your_webhook_url'
Run the app:

bash
Copy
Edit
python app.py
Access it locally:

Open your browser and go to http://localhost:5000 to play the game and log data.

⚠️ Disclaimer
This tool is intended for educational and ethical use only. Unauthorized use to collect personal data without consent may violate privacy laws and Discord's terms of service. Use responsibly.
