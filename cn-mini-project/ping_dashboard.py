from flask import Flask, render_template_string, jsonify
from ping3 import ping
import threading
import time
import random

app = Flask(__name__)

# List of IPs to monitor
devices = ["8.8.8.8", "1.1.1.1", "192.168.1.1"]

# Store response times
ping_data = {ip: [] for ip in devices}

# HTML Template (live dashboard)
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Smart Network Ping Monitor</title>
<script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
<style>
  body { background-color: #0d1117; color: #fff; font-family: 'Segoe UI', sans-serif; text-align: center; }
  h1 { color: #58a6ff; }
  #chart { width: 90%; margin: auto; height: 500px; }
  .status-box { display: flex; justify-content: center; margin-top: 20px; gap: 20px; }
  .device {
    padding: 10px 20px; border-radius: 12px; color: white; font-weight: bold;
    transition: all 0.4s; background-color: #30363d;
  }
  .online { background-color: #238636; }
  .offline { background-color: #da3633; }
</style>
</head>
<body>
<h1>🌐 Smart Network Ping Monitor</h1>
<div class="status-box" id="deviceStatus"></div>
<div id="chart"></div>

<script>
async function fetchData() {
    const res = await fetch('/data');
    const data = await res.json();

    let traces = [];
    let statusHTML = "";

    for (let ip in data) {
        let values = data[ip].map(x => x[1]);
        let times = data[ip].map(x => x[0]);
        traces.push({
            x: times,
            y: values,
            mode: 'lines+markers',
            name: ip,
            line: { shape: 'spline' }
        });

        let last = values[values.length - 1];
        let cls = (last > 0) ? 'online' : 'offline';
        statusHTML += `<div class="device ${cls}">${ip} - ${cls.toUpperCase()}</div>`;
    }

    document.getElementById('deviceStatus').innerHTML = statusHTML;

    Plotly.newPlot('chart', traces, {
        title: 'Real-time Ping Simulation Dashboard',
        paper_bgcolor: '#0d1117',
        plot_bgcolor: '#0d1117',
        font: { color: 'white' },
        xaxis: { title: 'Time' },
        yaxis: { title: 'Ping (ms)' }
    });
}

// Update every 2 seconds
setInterval(fetchData, 2000);
fetchData();
</script>
</body>
</html>
"""

# Background ping thread
def ping_loop():
    while True:
        timestamp = time.strftime("%H:%M:%S")
        for ip in devices:
            try:
                response = ping(ip, timeout=2)
                if response is None:
                    response = 0
                ping_data[ip].append((timestamp, round(response * 1000, 2)))
                if len(ping_data[ip]) > 30:
                    ping_data[ip].pop(0)
            except:
                ping_data[ip].append((timestamp, 0))
        time.sleep(2)

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

@app.route('/data')
def data():
    return jsonify(ping_data)

if __name__ == '__main__':
    threading.Thread(target=ping_loop, daemon=True).start()
    app.run(debug=False)
