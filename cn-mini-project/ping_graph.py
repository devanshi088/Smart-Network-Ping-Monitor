import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.dates as mdates
import seaborn as sns

# Use a modern style
sns.set(style="whitegrid")

csv_file = "ping_log.csv"

def animate(i):
    try:
        data = pd.read_csv(csv_file)
        online_data = data[data["Status"] == "Online"]

        plt.cla()  # Clear old plot

        # Plot each IP separately
        for ip in online_data["IP Address"].unique():
            ip_data = online_data[online_data["IP Address"] == ip]
            plt.plot(pd.to_datetime(ip_data["Timestamp"]), ip_data["Response Time (ms)"], 
                     label=ip, linewidth=2)

        # Format and style
        plt.xlabel("Time", fontsize=10)
        plt.ylabel("Response Time (ms)", fontsize=10)
        plt.title("📊 Smart Network Ping Monitor Dashboard", fontsize=14, fontweight='bold')
        plt.legend(loc="upper right", fontsize=8)
        
        # Format timestamps (show fewer labels)
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))
        plt.gcf().autofmt_xdate(rotation=30)
        
        # Set limits for smoother scale
        plt.ylim(0, max(300, online_data["Response Time (ms)"].max() + 50))
        plt.tight_layout()

    except Exception as e:
        print(f"Error reading file: {e}")

# Refresh every 3 seconds
ani = animation.FuncAnimation(plt.gcf(), animate, interval=3000)
plt.show()
