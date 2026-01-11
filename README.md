Smart Network Ping Monitor
Overview

Smart Network Ping Monitor is a Python-based network monitoring system that continuously checks the availability and response time of multiple devices using ICMP ping. The project provides real-time monitoring, CSV logging, graphical visualization, and a live web dashboard, making it suitable for academic mini-projects and basic network diagnostics.

Features

Continuous ping monitoring of multiple IP addresses

Real-time device status detection (Online / Offline)

Response time measurement in milliseconds

Automatic CSV logging for analysis

Live animated graphs using Matplotlib

Interactive web-based dashboard using Flask and Plotly


Technologies Used

Python 3

ping3 – ICMP ping utility

Flask – Web server

Plotly.js – Interactive charts

Matplotlib & Seaborn – Graph visualization

Pandas – Data processing

Colorama – Colored console output

Installation & Setup
1. Clone or Download the Project
git clone <repository-url>
cd smart-network-ping-monitor

2. Install Required Dependencies
pip install ping3 flask pandas matplotlib seaborn plotly colorama


⚠️ Note:
On Windows, run the terminal as Administrator to allow ICMP ping operations.
How to Run the Project
1. Start Network Monitoring (CSV Logger)
python smart_ping_monitor.py


Continuously pings devices

Writes logs to ping_log.csv

2. View Live Graph Dashboard
python ping_graph.py


Displays real-time response time graphs

Updates automatically every few seconds

3. Launch Web Dashboard
python ping_dashboard.py


Open browser and go to:

http://127.0.0.1:5000/


Shows live ping chart and device status indicators

Customization

To monitor different devices, update the IP list in the scripts:

devices = ["8.8.8.8", "1.1.1.1", "192.168.1.1"]

Use Cases

Computer Networks mini project

Basic network diagnostics

Learning ICMP, ping, and latency monitoring

Demonstrating real-time dashboards

Future Enhancements

Email or Telegram alerts on downtime

Database storage instead of CSV

Authentication for dashboard access

Docker deployment

Cloud-hosted monitoring service

Conclusion

This project demonstrates a complete end-to-end network monitoring solution, combining backend data collection, logging, visualization, and a modern web dashboard. It is simple, effective, and ideal for academic as well as practical learning purposes.
