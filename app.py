from flask import Flask, render_template
from prometheus_client import Counter, generate_latest
from datetime import datetime
import pytz

app = Flask(__name__)

gandalf_counter = Counter("gandalf_requests_total", "Total requests to /gandalf")
colombo_counter = Counter("colombo_requests_total", "Total requests to /colombo")


@app.route("/")
def home():
    return "<h1>Welcome to the Flask server!</h1><p>Endpoints: /gandalf, /colombo, /metrics</p>"


@app.route("/gandalf")
def gandalf():
    gandalf_counter.inc()
    return render_template("gandalf.html")

@app.route("/colombo")
def colombo():
    colombo_counter.inc()
    tz = pytz.timezone('Asia/Colombo')
    return f"Colombo Time: {datetime.now(tz).strftime('%Y-%m-%d %H:%M:%S')}"

@app.route("/metrics")
def metrics():
    return generate_latest(), 200, {'Content-Type': 'text/plain; version=0.0.4; charset=utf-8'}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
